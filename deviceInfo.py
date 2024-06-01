import sys
import time
from localTime import getLocalTimeCurrent


def getDeviceTime(deviceConnection):
        try:
                timeDevice = time.mktime(deviceConnection.get_time().timetuple())
                sys.stderr.write("timeCurrent: " + str(timeDevice) + "\n")
                return timeDevice
        except Exception as e:                
                print("getDeviceTimeException : {}".format(e))
                return None


def getDeviceTimeOffset(deviceConnection):
        try:
                timeOffset = getDeviceTime(deviceConnection) - getLocalTimeCurrent()
                sys.stderr.write("timeOffset: " + str(timeOffset) + "\n")
                return timeOffset
        except Exception as e:                
                print("getTimeOffsetException : {}".format(e))
                return None


def getDeviceSerial(deviceConnection):
        try:
                deviceSerial = deviceConnection.get_serialnumber()
                sys.stderr.write("deviceSerial: " + deviceSerial + "\n")
                return deviceSerial                  
        except Exception as e:                
                print("getDeviceSerial : {}".format(e))
                return None
