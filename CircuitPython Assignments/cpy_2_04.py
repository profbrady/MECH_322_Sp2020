#
# cpy_2_04.py
# Simulated Motor Control with Buttons
#
# Created and tested using the VS Code CPX Device Emulator
#
# By: your name here
#



#import the modules you need


# create a function to get the motor speed using from cp.light
def get_motor_speed():
    return cp.light

# it would be good idea to make a function to turn on/off NeoPixels


motor_speed = 0

while True:
    # check if the slide switch is left
        # use get_motor_speed() to read the light sensor
        # and scale it from 0-255 to 0-100 in steps of 10
        # and assign to motor-speed
        
        # scale motor_speed value from 0-100 to 0-65535
        # to determine motor_duty_cycle
        
        # print 0-100% and duty cycle
        
        # turn on NeoPixels based on motor_speed
    
    # check if the slide switch is right
        # check if only button A is pressed
            # if so, reduce speed by 10 but
            # don't set lower than 0
            
            # print 0-100% and duty cycle
            # turn on NeoPixels base don motor_speed
            # delay 0.25 seconds
            
        # check if only button B is pressed
            # if so, increase speed by 10
            # don't set higher than 100
            
            # print 0-100% and duty cycle
            # turn on NeoPixels based on motor_speed
            # delay 0.25 seconds
