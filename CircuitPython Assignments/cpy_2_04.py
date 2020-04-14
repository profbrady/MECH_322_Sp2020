#
# cpy_2_04.py
# Simulated Motor Control with Buttons
#
# Created and tested using the VS Code CPX Device Emulator
#
# By: your name here
#

#import the modules you need


# create a function to get the motor speed from cp.light
def get_motor_speed():
    return cp.light

# it would be good idea to make a function to turn on/off NeoPixels


motor_speed = 0

while True:
    # check if the slide switch is False
        # use `get_motor_speed()` to read the light sensor
        # then scale it from 0-255 to 0-100 in steps of 10
        # and assign the scaled value to `motor_speed`
        
        # scale the `motor_speed` value from 0-100 to 0-65535
        # to and assign to the variable `motor_duty_cycle`
        
        # print `motor_speed` and `motor_duty_cycle` as integers
        
        # turn on NeoPixels based on `motor_speed`
        # delay for 0.25 seconds
    
    # check if the slide switch is True
        # check if only button A is pressed
            # if so, reduce `motor_speed` by 10 (but
            # don't set it lower than 0)
            # calculate `motor_duty_cycle`
            
            # print `motor_speed` and `motor_duty_cycle` as integers
            # turn on NeoPixels based on `motor_speed`
            # delay 0.25 seconds
            
        # check if only button B is pressed
            # if so, increase `motor_speed` by 10  (but
            # don't set higher than 100)
            # calculate `motor_duty_cycle`
            
            # print `motor_speed` and `motor_duty_cycle` as integers
            # turn on NeoPixels based on `motor_speed`
            # delay 0.25 seconds
