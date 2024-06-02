import time
from localTime import getLocalTimeCurrent, getLocalTimeCurrentObject
from logger import debug, error


def getDeviceTime(deviceConnection):
    try:
        timeDevice = time.mktime(deviceConnection.get_time().timetuple())
        debug("timeDevice", timeDevice)
        return timeDevice
    except Exception as e:
        error("getDeviceTimeException", e)
        return None


def setDeviceTime(deviceConnection):
    try:
        localCurrentTimeObject = getLocalTimeCurrentObject()
        deviceConnection.set_time(localCurrentTimeObject)
        debug("setDeviceTime", localCurrentTimeObject)
        return True
    except Exception as e:
        error("setDeviceTimeException", e)
        return False


def getDeviceTimeOffset(deviceConnection):
    try:
        timeOffset = getDeviceTime(deviceConnection) - getLocalTimeCurrent()
        debug("timeOffset", timeOffset)
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
