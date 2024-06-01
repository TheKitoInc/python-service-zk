import time
from localTime import getLocalTimeCurrent
from logger import debug, error


def getDeviceTime(deviceConnection):
    try:
        timeDevice = time.mktime(deviceConnection.get_time().timetuple())
        debug("timeCurrent", str(timeDevice))
        return timeDevice
    except Exception as e:
        error("getDeviceTimeException", e)
        return None


def getDeviceTimeOffset(deviceConnection):
    try:
        timeOffset = getDeviceTime(deviceConnection) - getLocalTimeCurrent()
        debug("timeOffset", str(timeOffset))
        return timeOffset
    except Exception as e:
        error("getTimeOffsetException", e)
        return None


def getDeviceSerial(deviceConnection):
    try:
        deviceSerial = deviceConnection.get_serialnumber()
        debug("deviceSerial", deviceSerial)
        return deviceSerial
    except Exception as e:
        error("getDeviceSerial", e)
        return None
