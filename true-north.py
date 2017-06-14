from microbit import *

compass.calibrate()

def check_if_north()
    if compass.is_calibrated()
        return compass.heading()

def notify()
    if check_if_north() == 0
        display.show(Image.HAPPY)

while True:
    notify()