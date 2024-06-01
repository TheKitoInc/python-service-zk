from zk import ZK
from logger import debug, error, fatal


def deviceInit(host, port=4370, timeout=5, password=0, modeUDP=False, noPing=False):
    try:
        debug('Host', host)
        debug('Port', port)
        debug('Timeout', timeout)
        debug('UDP', modeUDP)
        debug('NoPING', noPing)
        device = ZK(host, port, timeout, password, modeUDP, noPing)
        debug("Status", "Device created")
        return device
    except Exception as e:
        fatal("getDeviceException", e)
        return None


def deviceConnect(device):
    try:
        deviceConnection = device.connect()
        debug("Status", "Device connected")
        return deviceConnection
    except Exception as e:
        error("deviceConnectionException", e)
        return None


def deviceDisconnect(deviceConnection):
    try:
        deviceConnection.disconnect()
        debug("Status", "Device disconnected")
    except Exception as e:
        error("deviceDisconnectException", e)
