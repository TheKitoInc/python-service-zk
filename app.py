from logger import debug, error, fatal
from device import deviceInit, deviceConnect, deviceDisconnect, deviceDisable, deviceEnable
from deviceInfo import getDeviceTimeOffset, getDeviceSerial
from deviceData import getDeviceUsers, getDeviceRecords


def main(args):

    print(args)

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

    if args.time:
        deviceTimeOffset = getDeviceTimeOffset(deviceConnection)
    else:
        deviceTimeOffset = 0

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

    deviceEnable(deviceConnection)
    deviceDisconnect(deviceConnection)

    return 0
