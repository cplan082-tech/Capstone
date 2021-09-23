import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer_obj = adafruit_adxl34x.ADXL345(i2c)
 
if __name__ == "__main__":
    accelerometer_obj.enable_freefall_detection(threshold=10, time=25)
    accelerometer_obj.enable_motion_detection(threshold=18)
    accelerometer_obj.enable_tap_detection(tap_count=1, threshold=20, duration=50, latency=20, window=255)

    while True:
        print("%f %f %f"%accelerometer_obj.acceleration)
        print("Dropped: %s"%accelerometer_obj.events["freefall"])
        print("Tapped: %s"%accelerometer_obj.events['tap'])
        print("Motion detected: %s"%accelerometer_obj.events['motion'])
        time.sleep(0.5)
