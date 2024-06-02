from logger import debug, fatal
from device import deviceInit, deviceConnect, deviceDisconnect, deviceDisable, deviceEnable
from deviceInfo import getDeviceSerial, setDeviceTime
from deviceData import getDeviceUsers, getDeviceRecords
from times import getTimes


def main(args):

    debug("args", args)

    device = deviceInit(args.host, args.port, args.timeout,
                        args.password, args.UDP, not args.ping)

    if device is None:
        return 1

    deviceConnection = deviceConnect(device)
    if deviceConnection is None:
        return 2

    if not deviceDisable(deviceConnection):
        deviceDisconnect(deviceConnection)
        return 3

    try:

        if args.time:
            time = getTimes(deviceConnection)
        else:
            time = None

        if args.serial:
            deviceSerial = getDeviceSerial(deviceConnection)
        else:
            deviceSerial = None

        if args.users:
            deviceUsers = getDeviceUsers(deviceConnection)
        else:
            deviceUsers = None

        if args.records:
            deviceRecords = getDeviceRecords(deviceConnection)
        else:
            deviceRecords = None

        output = {
            "device": {
                "serial": deviceSerial,
            },
            "time": time,
            "users": deviceUsers,
            "records": deviceRecords
        }

        print(res)

        if args.time:
            if abs(time['deviceOffset']) > 1:
                setDeviceTime(deviceConnection)

    except Exception as e:
        fatal("main", e)

    deviceEnable(deviceConnection)
    deviceDisconnect(deviceConnection)

    return 0
