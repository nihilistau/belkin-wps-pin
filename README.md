# Belkin WPS PIN Generator

## Credits
* [Reversing Belkin’s WPS Pin Algorithm](http://www.devttys0.com/2015/04/reversing-belkins-wps-pin-algorithm/)
* [/dev/ttys0's WPS related utilities](https://github.com/devttys0/wps/blob/master/pingens/belkin/pingen.c)

## Description

WPS pin generator for some Belkin routers. Default pin is generated from the
BSSID and serial number. BSSIDs are not encrypted and the serial number is
included in the WPS information element contained in 802.11 probe response
packets.

## Known to work against:

* F9K1001v4         [Broadcom, Arcadyan, SuperTask!]
* F9K1001v5         [Broadcom, Arcadyan, SuperTask!]
* F9K1002v1         [Realtek, SerComm]
* F9K1002v2         [Ralink, Arcadyan]
* F9K1002v5         [Broadcom, Arcadyan]
* F9K1103v1         [Ralink, Arcadyan, Linux]
* F9K1112v1         [Broadcom, Arcadyan, Linux]
* F9K1113v1         [Broadcom, Arcadyan, Linux]
* F9K1105v1         [Broadcom, Arcadyan, Linux]
* F6D4230-4v2       [Ralink, Arcadyan, Unknown RTOS]
* F6D4230-4v3       [Broadcom, Arcadyan, SuperTask!]
* F7D2301v1         [Ralink, Arcadyan, SuperTask!]
* F7D1301v1         [Broadcom, Arcadyan, Unknown RTOS]
* F5D7234-4v3       [Atheros, Arcadyan, Unknown RTOS]
* F5D7234-4v4       [Atheros, Arcadyan, Unknown RTOS]
* F5D7234-4v5       [Broadcom, Arcadyan, SuperTask!]
* F5D8233-4v1       [Infineon, Arcadyan, SuperTask!]
* F5D8233-4v3       [Ralink, Arcadyan, Unknown RTOS]
* F5D9231-4v1       [Ralink, Arcadyan, SuperTask!]
 
## Known to NOT work against:
* F9K1001v1         [Realtek, SerComm, Unknown RTOS]
* F9K1105v2         [Realtek, SerComm, Linux]
* F6D4230-4v1       [Ralink, SerComm, Unknown RTOS]
* F5D9231-4v2       [Ralink, SerComm, Unknown RTOS]
* F5D8233-4v4       [Ralink, SerComm, Unknown RTOS]

## Usage

```
usage: belkin-wps-pin.py [-h] bssid serial

WPS pin generator for some Belkin routers.

positional arguments:
  bssid       BSSID of the target device (last 2 octets required)
  serial      Serial number of the target device, usually found in a probe response (last 4 digits required)

optional arguments:
  -h, --help  show this help message and exit
```

### Example
```
belkin-wps-pin.py fb99 8376
belkin-wps-pin.py ec1a598afb99 12310GC2508376
belkin-wps-pin.py ec:1a:59:8a:fb:99 12310GC2508376
```

### Output
```
Default WPS PIN: 19195223
```