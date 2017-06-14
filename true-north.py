from microbit import *

compass.calibrate()

def check_if_north()
    if compass.is_calibrated()
        return compass.heading()

def notify_if_north()
    if check_if_north() == 0
        display.show(Image.HEART)
    elif
        display.show(Image.ANGRY)


while True:
    notify_if_north()