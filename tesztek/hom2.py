import time
import board
import adafruit_sht31d

i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

loopcount = 0
while True:
    print("\nHőmérséklet: %0.1f C" % sensor.temperature)
    print("Páratartalom: %0.1f %%" % sensor.relative_humidity)
    loopcount += 1
    time.sleep(4)

    if loopcount == 15:
        loopcount = 0
        sensor.heater = True
        print("Szenzor melegítő =", sensor.heater)
        time.sleep(1)
        sensor.heater = False
        print("Szenzor melegítő =", sensor.heater)

