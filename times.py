from logger import debug, error
from localTime import getLocalTimeCurrent, getLocalTimeZoneOffset
from deviceInfo import getDeviceTime


def getTimes(deviceConnection):
    try:
        deviceTime = getDeviceTime(deviceConnection)
        localTime = getLocalTimeCurrent()
        times = {
            "local": localTime,
            "localOffset": getLocalTimeZoneOffset(),
            "device": deviceTime,
            "deviceOffset": deviceTime - localTime
        }
        debug("times", times)
        return times
    except Exception as e:
        error("getTimesException", e)
        return None
