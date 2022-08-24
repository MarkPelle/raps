import board
import busio
import adafruit_sht31d
from time import time, sleep
from threading import Timer

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

def prints():
    para = print('Pára: {0}%'.format(sensor.relative_humidity))
    hom = print('Hőmérséklet: {0}C'.format(sensor.temperature))


def loopi():

    while True:
        sleep(5 - time() % 5)
        prints()

