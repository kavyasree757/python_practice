import time
import serial

ser = serial.Serial("/dev/ttyUSB0", 115200)

while True:
    line = ser.readline().decode()

    if "login:" in line:
        print("Board Booted Successfully")
        break

    time.sleep(1)
