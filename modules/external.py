import adafruit_dht
from board import D4

dht = adafruit_dht.DHT11(D4)


def get_temp():
    temp = dht.temperature
    return temp


def get_hum():
    humidity = dht.humidity
    return humidity
