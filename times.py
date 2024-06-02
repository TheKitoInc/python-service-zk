from logger import debug, error
from localTime import getLocalTimeCurrent
from deviceInfo import getDeviceTime


def getTimes(deviceConnection):
    try:
        deviceTime = getDeviceTime(deviceConnection)
        localTime = getLocalTimeCurrent()
        times = {
            "device": deviceTime,
            "local": localTime,
            "offset": deviceTime - localTime
        }
        debug("times", times)
        return times
    except Exception as e:
        error("getTimesException", e)
        return None
