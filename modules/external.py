# Adopted from https://github.com/ControlEverythingCommunity/MPL3115A2

from smbus2 import SMBus
import time
import board
import busio
import adafruit_ccs811

# Get I2C bus
bus = SMBus(1)
i2c_bus = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c_bus)


def get_temp():
    # MPL3115A2 address, 0x60(96)
    # Select control register, 0x26(38)
    #		0xB9(185)	Active mode, OSR = 128, Altimeter mode
    bus.write_byte_data(0x60, 0x26, 0xB9)
    # MPL3115A2 address, 0x60(96)
    # Select data configuration register, 0x13(19)
    #		0x07(07)	Data ready event enabled for altitude, pressure, temperature
    bus.write_byte_data(0x60, 0x13, 0x07)
    # MPL3115A2 address, 0x60(96)
    # Select control register, 0x26(38)
    #		0xB9(185)	Active mode, OSR = 128, Altimeter mode
    bus.write_byte_data(0x60, 0x26, 0xB9)

    time.sleep(1)

    # MPL3115A2 address, 0x60(96)
    # Read data back from 0x00(00), 6 bytes
    # status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
    data = bus.read_i2c_block_data(0x60, 0x00, 6)

    # Convert the data to 20-bits
    temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
    cTemp = temp / 16.0

    return cTemp


def get_pressure():
    # MPL3115A2 address, 0x60(96)
    # Select control register, 0x26(38)
    #		0x39(57)	Active mode, OSR = 128, Barometer mode
    bus.write_byte_data(0x60, 0x26, 0x39)

    time.sleep(1)

    # MPL3115A2 address, 0x60(96)
    # Read data back from 0x00(00), 4 bytes
    # status, pres MSB1, pres MSB, pres LSB
    data = bus.read_i2c_block_data(0x60, 0x00, 4)

    # Convert the data to 20-bits
    pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    pressure = (pres / 4.0) / 1000.0

    return pressure


def get_altitude():
    # MPL3115A2 address, 0x60(96)
    # Select control register, 0x26(38)
    #		0xB9(185)	Active mode, OSR = 128, Altimeter mode
    bus.write_byte_data(0x60, 0x26, 0xB9)
    # MPL3115A2 address, 0x60(96)
    # Select data configuration register, 0x13(19)
    #		0x07(07)	Data ready event enabled for altitude, pressure, temperature
    bus.write_byte_data(0x60, 0x13, 0x07)
    # MPL3115A2 address, 0x60(96)
    # Select control register, 0x26(38)
    #		0xB9(185)	Active mode, OSR = 128, Altimeter mode
    bus.write_byte_data(0x60, 0x26, 0xB9)

    time.sleep(1)

    # MPL3115A2 address, 0x60(96)
    # Read data back from 0x00(00), 6 bytes
    # status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
    data = bus.read_i2c_block_data(0x60, 0x00, 6)

    # Convert the data to 20-bits
    tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
    altitude = tHeight / 16.0

    return altitude


def get_eco2():
    return ccs811.eco2


def get_tvoc():
    return ccs811.tvoc


