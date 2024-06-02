from logger import debug, fatal
from device import deviceInit, deviceConnect, deviceDisconnect, deviceDisable, deviceEnable
from deviceInfo import getDeviceTimeOffset, getDeviceSerial
from deviceData import getDeviceUsers, getDeviceRecords
import json


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
            deviceTimeOffset = getDeviceTimeOffset(deviceConnection)
        else:
            deviceTimeOffset = None

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

        res = json.dumps({
            "device": {
                "serial": deviceSerial,
                "time": {
                    "offset": deviceTimeOffset
                }},
            "users": deviceUsers,
            "records": deviceRecords
        })

        print(res)

    except Exception as e:
        fatal("main", e)

    deviceEnable(deviceConnection)
    deviceDisconnect(deviceConnection)

    return 0
