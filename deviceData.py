import time
from logger import debug, error


def getDeviceRecords(deviceConnection):
    try:
        deviceRecords = []
        for record in deviceConnection.get_attendance():
            recordTime = time.mktime(record.timestamp.timetuple())
            deviceRecords.append({'userId': record.uid, 'recordTime': recordTime,
                                 'recordStatus': record.status, 'recordPunch': record.punch})
        debug("deviceRecords", str(len(deviceRecords)))
        return deviceRecords
    except Exception as e:
        error("getDeviceRecordsException", e)
        return None


def getDeviceUsers(deviceConnection):
    try:
        deviceUsers = []
        for user in deviceConnection.get_users():
            deviceUsers.append({'userId': user.uid, 'userPrivilege': user.privilege, 'userName': user.name,
                               'userPassword': user.password, 'userCustomId': user.user_id, 'userGroupId': user.group_id})
        debug("deviceUsers", str(len(deviceUsers)))
        return deviceUsers
    except Exception as e:
        error("getDeviceUsersException", e)
        return None
