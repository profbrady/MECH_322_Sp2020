#
# cpy_1_02.py
# NeoPixel Patterns
#
# Created and tested using the VS Code CPX Device Emulator
#
# By: your name here
#

import time
import random
from adafruit_circuitplayground import cp

COLOR = (0, 255, 0)  # Change this to any color you wish
OFF = (0, 0, 0)

cp.pixels.auto_write = False
cp.pixels.brightness = 0.25

# complete each of the function definitions and delete `pass`
def one_at_a_time(on_time, off_time):
    pass

def one_after_another(on_time, off_time):
    pass

def ping_pong(on_time, off_time):
    pass

def marquee(on_time, off_time):
    pass

def random_lights(on_time, off_time):
    for i in range(10):
        cp.pixels[random.choice(range(10))] = COLOR
        cp.pixels.show()
        time.sleep(on_time)
        cp.pixels.fill(OFF)
        cp.pixels.show()
        time.sleep(off_time)

while True:
    #one_at_a_time(0.5, 0.25)
    #one_after_another(0.5, 0.25)
    #ping_pong(0.5, 0.25)
    #marquee(0.5, 0.25)
    random_lights(0.5, 0.25)

