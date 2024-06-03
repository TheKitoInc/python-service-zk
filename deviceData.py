import time
from logger import debug, error
from pairing import pair


def getDeviceRecords(deviceConnection):
    try:
        deviceRecords = []
        for record in deviceConnection.get_attendance():
            recordTime = int(time.mktime(record.timestamp.timetuple()))
            deviceRecords.append({'id': pair(record.uid, recordTime), 'idUser': record.uid,
                                 'time': recordTime, 'status': record.status, 'punch': record.punch})
        debug("deviceRecords", len(deviceRecords))
        return deviceRecords
    except Exception as e:
        error("getDeviceRecordsException", e)
        return None


def getDeviceUsers(deviceConnection):
    try:
        deviceUsers = []
        for user in deviceConnection.get_users():
            deviceUsers.append({'id': user.uid, 'privilege': user.privilege, 'name': user.name,
                               'password': user.password, 'idCustom': user.user_id, 'idGroup': user.group_id})
        debug("deviceUsers", len(deviceUsers))
        return deviceUsers
    except Exception as e:
        error("getDeviceUsersException", e)
        return None
