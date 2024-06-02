from logger import debug, error, fatal
from device import deviceInit, deviceConnect, deviceDisconnect
import sys


def main(args):

    print(args)

    device = deviceInit(args.host, args.port, args.timeout,
                        args.password, args.UDP, not args.ping)

    if device is None:
        return 1

    deviceConnection = deviceConnect(device)
    if deviceConnection is None:
        return 2

    deviceDisconnect(deviceConnection)
    return 0
