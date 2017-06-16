from microbit import *

compass.calibrate()

def notify_if_north():
    heading = compass.heading()
    display.scroll(heading)


while True:
    notify_if_north()