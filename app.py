from logger import debug, error, fatal
from device import deviceInit, deviceConnect, deviceDisconnect
import sys


def main():

    host = sys.argv[len(sys.argv)-1]

    device = deviceInit(host)
    if device is None:
        return 1

    deviceConnection = deviceConnect(device)
    if deviceConnection is None:
        return 2

    deviceDisconnect(deviceConnection)
    return 0
