import sounddevice as sd
import numpy as np
import os
from tqdm import tqdm
from auralis.processing import preprocess_audio
from auralis.scorer import score_audio

from .config import Config
from .utils import timestamp, ensure_dir
from .session import SessionReport

class VoiceMonitor:

    def __init__(self, threshold=None, chunk_dir=None):
        self.threshold = threshold or Config.DEFAULT_THRESHOLD
        self.chunk_dir = chunk_dir or f"{Config.CHUNK_DIR}_{timestamp()}"
        ensure_dir(self.chunk_dir)
        self.session = SessionReport()

    def _save_chunk(self, audio_arr: np.ndarray, ts: str):
        """Write raw audio to temporary wav"""
        fname = f"{self.chunk_dir}/{ts}.wav"
        import soundfile as sf
        sf.write(fname, audio_arr, Config.SAMPLE_RATE)
        return fname

    def _process_chunk(self, wav_path: str, ts: str):
        # run auralis preprocessing (standardize)
        out_files = preprocess_audio(wav_path, self.chunk_dir)
        if not out_files:
            return None
        processed = out_files[-1]
        score = score_audio(processed)
        self.session.add_record(ts, processed, score)
        return score

    def start(self, duration_sec=None):
        """Start real-time monitoring"""
        # compute sample count for window/step
        win_samples = Config.SAMPLE_RATE * Config.WINDOW_SEC
        step_samples = Config.SAMPLE_RATE * Config.STEP_SEC

        # grab raw audio buffer
        buffer = np.zeros((0,), dtype="float32")

        # backfill for live view
        remaining = duration_sec or float("inf")
        print("Start Speaking...")
        with sd.InputStream(channels=1, samplerate=Config.SAMPLE_RATE) as stream:
            while remaining > 0:
                block, _ = stream.read(step_samples)
                buffer = np.concatenate([buffer, block.flatten()])

                if len(buffer) >= win_samples:
                    ts = timestamp()
                    # write raw to wav
                    raw_file = self._save_chunk(buffer[:win_samples], ts)
                    score = self._process_chunk(raw_file, ts)

                    # slide buffer
                    buffer = buffer[int(step_samples):]

                    # warnings & prints
                    print(f"[{ts}] Score: {score:.2f}")
                    if score >= self.threshold:
                        print("⚠ fatigue threshold crossed")

                    remaining -= Config.STEP_SEC

        print("Session ended.")
        return self.session