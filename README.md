# VoiceMonitor

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![PyPI](https://img.shields.io/pypi/v/voiceMonitor)
![License](https://img.shields.io/badge/license-MIT-green)
![Downloads](https://img.shields.io/pypi/dm/voiceMonitor)
![Status](https://img.shields.io/badge/status-research--grade-success)

**Real-Time Vocal Fatigue Monitoring for Continuous Speech Analytics**

VoiceMonitor is a Python library for **real-time vocal fatigue monitoring** built on top of the **auralis_vfs** vocal fatigue scoring framework. It enables continuous microphone monitoring, fatigue scoring using sliding audio windows, and session-level analytics for voice health monitoring.

The system is designed for **researchers, speech engineers, and voice professionals** who require automated analysis of vocal strain during prolonged speech activity.

VoiceMonitor processes live microphone input, extracts standardized audio segments, computes fatigue scores, and produces real-time alerts and session analytics.

---

## Overview

Prolonged speaking can lead to **vocal fatigue**, a condition characterized by strain, reduced vocal efficiency, and potential long-term damage to vocal health.

VoiceMonitor provides a **real-time monitoring pipeline** that:

* captures microphone audio streams
* processes sliding audio windows
* computes vocal fatigue scores
* tracks fatigue progression over time
* generates session analytics and warnings

The system leverages the **ECAPA-TDNN-VHE vocal fatigue estimation model** and the `auralis_vfs` scoring framework developed as part of ongoing research in speech health monitoring.

---

## Key Features

* Real-time microphone audio monitoring
* Continuous vocal fatigue scoring
* Sliding window fatigue analysis
* Fatigue threshold warnings
* Session-level analytics and reports
* Chunk-based audio processing pipeline
* JSON session export for downstream analysis
* Lightweight CLI interface for quick experiments

---

## Architecture

VoiceMonitor uses a **sliding window inference pipeline** for continuous analysis.

```
Microphone Input
        │
        ▼
Audio Stream Buffer
        │
        ▼
Sliding Window Segmentation (5s)
        │
        ▼
auralis_vfs Preprocessing
        │
        ▼
Vocal Fatigue Scoring
        │
        ▼
Session Analytics Engine
        │
        ▼
Fatigue Alerts + Reports
```

Each processed window produces a **fatigue score**, enabling real-time tracking of vocal strain progression during speech sessions.

---

## Installation

### Requirements

* Python ≥ 3.10
* FFmpeg installed on system
* Microphone access

### Install from PyPI

```bash
pip install voicemonitor
```

### Install from source

```bash
git clone https://github.com/Khubaib8281/voiceMonitor.git
cd voicemonitor
pip install -e .
```

---

## Dependencies

VoiceMonitor relies on the following core libraries:

* `auralis_vfs`
* `numpy`
* `sounddevice`
* `soundfile`
* `pydub`
* `tqdm`

FFmpeg must be installed for audio processing.

---

## Quick Start

### CLI Usage

Start real-time vocal fatigue monitoring:

```bash
voicemonitor
```

Monitor for a fixed duration:

```bash
voicemonitor --duration 120
```

Set a custom fatigue warning threshold:

```bash
voicemonitor --threshold 65
```

Example output:

```
[20260312_182001] Score: 22.51
[20260312_182006] Score: 31.02
[20260312_182011] Score: 45.44
[20260312_182016] Score: 72.90

⚠ fatigue threshold crossed
```

After the session completes, a report is generated:

```
session_report.json
```

---

## Python API

VoiceMonitor can also be used directly in Python applications.

```python
from voicemonitor import VoiceMonitor

monitor = VoiceMonitor(threshold=70)

session = monitor.start(duration_sec=120)

session.export_json("session_report.json")
```

---

## Session Analytics

Each monitoring session records:

* average fatigue score
* maximum fatigue score
* timestamps of processed windows
* processed audio chunk paths
* fatigue warning events

Example report:

```json
{
  "summary": {
    "average_fatigue": 38.2,
    "max_fatigue": 74.1,
    "readings": 25
  },
  "records": [
    {
      "timestamp": "20260312_182001",
      "chunk": "chunks/20260312_182001.wav",
      "score": 22.51
    }
  ]
}
```

---

## Configuration

- Audio overlap is of `1 sec`
- default threshold is 70

---

## Research Background

VoiceMonitor is built upon the **auralis_vfs vocal fatigue scoring framework**, which was developed as part of research on automated vocal fatigue detection.

The underlying fatigue estimation model is based on an **ECAPA-TDNN architecture adapted for vocal health estimation**.

Research paper:

> [Modeling Vocal Fatigue as Embedding-Space Deviation Using Contrastively Trained ECAPA-TDNNs](https://doi.org/10.5281/zenodo.18366305)

Model repository:

> [huggingface.co/Khubaib01/ECAPA-TDNN-VHE](https://huggingface.co/Khubaib01/ECAPA-TDNN-VHE)

The model estimates vocal fatigue levels from short speech segments and provides a continuous fatigue score representing vocal strain.

VoiceMonitor extends this work by enabling **real-time fatigue monitoring and session analytics**.

---

## Applications

VoiceMonitor can be used in a variety of speech-intensive environments:

* speech research
* voice health monitoring
* call center voice analytics
* teacher vocal load monitoring
* podcast and streaming voice tracking
* speech therapy experiments
* human-computer interaction studies

---

## Project Structure

```
voicemonitor/
├── voicemonitor/
│   ├── audio_stream.py
│   ├── analytics.py
│   ├── session.py
│   ├── utils.py
│   ├── config.py
│   └── cli.py
│
├── examples/
│   └── live.py
│
├── tests/
│   └── test_session.py
│
├── LISENCE
├── setup.cfg
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Future Development

Planned enhancements include:

* real-time visualization dashboard
* web API for remote monitoring
* desktop GUI interface
* voice activity detection integration
* fatigue trend prediction models
* speaker-aware monitoring

---

## Citation

If you use VoiceMonitor in research, please cite the underlying work:

```bibtex
Ahmad, M. K. (2026). Modeling Vocal Fatigue as Embedding-Space Deviation Using Contrastively Trained ECAPA-TDNNs. Zenodo. https://doi.org/10.5281/zenodo.18366305
```

---

## License

This project is released under the MIT License.

---

## Author

Muhammad Khubaib Ahmad
AI / ML Engineer
Speech Intelligence and Audio AI Systems
