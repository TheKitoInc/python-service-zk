import sys
import time


def getDeviceRecords(deviceConnection):
    try:
        deviceRecords = []
        for record in deviceConnection.get_attendance():
            recordTime = time.mktime(record.timestamp.timetuple())
            deviceRecords.append({'userId': record.uid, 'recordTime': recordTime,
                                 'recordStatus': record.status, 'recordPunch': record.punch})
        sys.stderr.write("deviceRecords: " + str(len(deviceRecords)) + "\n")
        return deviceRecords
    except Exception as e:
        print("getDeviceRecordsException : {}".format(e))
        return None


def getDeviceUsers(deviceConnection):
    try:
        deviceUsers = []
        for user in deviceConnection.get_users():
            deviceUsers.append({'userId': user.uid, 'userPrivilege': user.privilege, 'userName': user.name,
                               'userPassword': user.password, 'userCustomId': user.user_id, 'userGroupId': user.group_id})
        sys.stderr.write("deviceUsers: " + str(len(deviceUsers)) + "\n")
        return deviceUsers
    except Exception as e:
        print("getDeviceUsersException : {}".format(e))
        return None
