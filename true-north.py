from microbit import *

compass.calibrate()

def notify_if_north():
    if compass.heading == 0:
        display.show(Image.HEART)
    else:
        display.show(Image.ANGRY)


while True:
    notify_if_north()