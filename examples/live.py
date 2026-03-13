from voiceMonitor import VoiceMonitor

vm = VoiceMonitor(threshold=70)
session = vm.start(duration_sec=10)
session.export_json("session2min.json")