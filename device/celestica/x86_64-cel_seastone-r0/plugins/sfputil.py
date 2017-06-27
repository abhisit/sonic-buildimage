#!/usr/bin/env python

try:
    from sonic_sfp.sfputilbase import sfputilbase
except ImportError, e:
    raise ImportError (str(e) + "- required module not found")


class sfputil(sfputilbase):
    """Platform specific sfputil class"""

    port_start = 1
    port_end = 32
    ports_in_block = 33

    port_to_eeprom_mapping = {}
    port_to_i2c_mapping = {
        1: 26,
        2: 27,
        3: 28,
        4: 29,
        5: 30,
        6: 31,
        7: 32,
        8: 33,
        9: 34,
        10: 35,
        11: 36,
        12: 37,
        13: 38,
        14: 39,
        15: 40,
        16: 41,
        17: 42,
        18: 43,
        19: 44,
        20: 45,
        21: 46,
        22: 47,
        23: 48,
        24: 49,
        25: 50,
        26: 51,
        27: 52,
        28: 53,
        29: 47,
        30: 48,
        31: 49,
        32: 50
    }

    _qsfp_ports = range(0, ports_in_block + 1)

    def __init__(self, port_num):
        # Override port_to_eeprom_mapping for class initialization
        eeprom_path = '/sys/bus/i2c/devices/i2c-{0}/{0}-0050/eeprom'
        for x in range(1, self.port_end + 1):
            port_eeprom_path = eeprom_path.format(self.port_to_i2c_mapping[x])
            self.port_to_eeprom_mapping[x] = port_eeprom_path
        sfputilbase.__init__(self, port_num)
