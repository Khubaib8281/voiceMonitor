class SessionAnalytics:
    def __init__(self):
        self.scores = []
        self.timestamps = []

    def add(self, score, ts):
        self.scores.append(score)
        self.timestamps.append(ts)

    @property
    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    @property
    def maximum(self):
        return max(self.scores) if self.scores else 0

    @property
    def summary(self):
        return {
            "average_fatigue": self.average,
            "max_fatigue": self.maximum,
            "readings": len(self.scores)
        }