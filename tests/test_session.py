from voiceMonitor.analytics import SessionAnalytics

def test_analytics_average_and_max():
    a = SessionAnalytics()
    a.add(10, "t1")
    a.add(30, "t2")
    a.add(20, "t3")
    assert a.average == 20
    assert a.maximum == 30