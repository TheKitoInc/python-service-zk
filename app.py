from logger import debug, fatal, error
from device import deviceInit, deviceConnect, deviceDisconnect, deviceDisable, deviceEnable
from deviceInfo import getDeviceSerial, syncDeviceTime
from deviceData import getDeviceUsers, getDeviceRecords
import requests
from times import getTimes


def callServer(url, data=None):
    try:
        response = requests.post(url, json=data)
        return response.status_code == 200
    except Exception as e:
        error("callServer", e)
        return False


def main(args):

    debug("args", args)

    if not callServer(args.URL):
        return 11

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

    if args.timezone is not None:
        import os
        import time
        os.environ['TZ'] = args.timezone
        time.tzset()

    try:

        output = {
            'device': {}
        }

        if args.serial:
            output['device']['serial'] = getDeviceSerial(deviceConnection)
            callServer(args.URL, output)

        if args.time:
            output['time'] = getTimes(deviceConnection)
            callServer(args.URL, output)

        if args.users:
            output['users'] = getDeviceUsers(deviceConnection)
            callServer(args.URL, output)

        if args.records:
            output['users'] = getDeviceRecords(deviceConnection)
            callServer(args.URL, output)

        if callServer(args.URL, output):
            if args.time:
                if abs(output['time']['deviceOffset']) > 1:
                    if abs(output['time']['deviceOffset']) < 3600:
                        syncDeviceTime(deviceConnection)

    except Exception as e:
        fatal("main", e)

    deviceEnable(deviceConnection)
    deviceDisconnect(deviceConnection)

    return 0
