#
# cpy_2_03.py
# NeoPixel Night light
#
# Created and tested using the VS Code CPX Device Emulator
#
# By: your name here
#

# import the modules you need


# initially set the NeoPixel brightness to 0.2
# create variables `ON` and `OFF` and turn all NeoPixels OFF
# set tracking variable `light_on` to `False`

cp.pixels.brightness = 0.2
ON = (255, 255, 255)
OFF = (0, 0, 0)
cp.pixels.fill(OFF)
light_on = False

while True:
    if cp.switch:
        # turn on all NeoPixels to 0.5 brightness and set `light_on` variable
    else:
        if light_on:  # lights are on, `light_on = True`
            cp.pixels.brightness = 0.2
            cp.pixels.fill(ON)
            
            # add code to turn off lights per requirements
            # and set `light_on` to correct value
        
        else:    # lights are off, `light_on = False`
            
            # add code to turn on lights if B is pressed
            # and set `light_on` to correct value
