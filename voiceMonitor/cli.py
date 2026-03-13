import argparse
from .audio_stream import VoiceMonitor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=int, default=None)
    parser.add_argument("--threshold", type=float, default=None)
    args = parser.parse_args()

    vm = VoiceMonitor(threshold=args.threshold)
    report = vm.start(duration_sec=args.duration)
    report.export_json("session_report.json")
    print("Report saved as session_report.json")

if __name__ == "__main__":
    main()