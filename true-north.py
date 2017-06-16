from microbit import *

compass.calibrate()

def notify_if_north():
    heading = compass.heading()
    if heading < 45:
        display.show(Image.HEART)
    else:
        display.show(Image.ANGRY)


while True:
    notify_if_north()