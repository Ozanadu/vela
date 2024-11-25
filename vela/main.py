import csv
import datetime
import time
import board
import adafruit_bh1750


def main():
    i2c = board.I2C()
    sensor = adafruit_bh1750.BH1750(i2c)

    while True:
        currentTime = datetime.datetime.now()
        luxReading = ('%.2f Lux' % sensor.lux)

        with open('./data/lux.csv', 'a+') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(currentTime, luxReading)
        
        time.sleep(1)

if __name__ == "__main__":
    main()