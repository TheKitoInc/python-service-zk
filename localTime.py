import sys
import time
from datetime import datetime

def getTimeZoneOffset():
        try:
                timeZoneOffset = -time.timezone
                sys.stderr.write("timeZoneOffset: " + str(timeZoneOffset) + "\n")
                return timeZoneOffset
        except Exception as e:                
                print ("getTimeZoneOffsetException : {}".format(e))
                return None
        
def getTimeCurrent():
        try:                
                timeCurrent = time.mktime(datetime.today().timetuple())
                sys.stderr.write("timeCurrent: " + str(timeCurrent) + "\n")
                return timeCurrent
        except Exception as e:                
                print ("getTimeCurrentException : {}".format(e))
                return None