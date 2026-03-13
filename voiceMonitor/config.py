class Config:
    # audio capture
    SAMPLE_RATE = 16000
    WINDOW_SEC = 5
    STEP_SEC = 4

    # fatigue warnings
    DEFAULT_THRESHOLD = 70  # out of 0‑100 scale

    # session metadata    
    SAVE_CHUNKS = True
    CHUNK_DIR = "chunks"