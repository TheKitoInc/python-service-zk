import sys


def getDeviceRecords(deviceConnection):
    try:
        deviceRecords = deviceConnection.get_attendance()
        sys.stderr.write("deviceRecordsCount: " +
                         str(len(deviceRecords)) + "\n")
        return deviceRecords
    except Exception as e:
        print("getDeviceRecordsException : {}".format(e))
        return None


def getDeviceUsers(deviceConnection):
    try:
        deviceUsers = []
        for record in deviceConnection.get_users():
            deviceUsers.append({'userId': str(record.uid), 'userPrivilege': str(record.privilege), 'userName': str(
                record.name), 'userPassword': str(record.password), 'userCustomId': str(record.user_id), 'userGroupId': str(record.group_id)})
        sys.stderr.write("deviceUsers: " + str(len(deviceUsers)) + "\n")
        return deviceUsers
    except Exception as e:
        print("getDeviceUsersException : {}".format(e))
        return None
