#
# cpy_3_03.py
# NeoPixel Timer
#
# Created and tested using the VS Code CPX Device Emulator
#
# By: your name here
#



from adafruit_circuitplayground import cp
import time

# set a state variable for timer completion to `False`
# and initially set timer setting variable to 0


def reset_timer():
    # Call this function any time to reset timer info
    # <-- Turn off NeoPixels
    # <-- Stop tone if used
    global # put names of timer completion and timer value variables here
    # <-- reset timer value to 0
    # <-- set timer completion state variable to `False`
    

# create tuples for your colors (include the OFF color)

# set NeoPixel brightness and turn off all NeoPixels


while True:
    # if switch is `True` (left)
    if cp.switch:
        # if timer complete variable is `True` perform reset
        # and sleep 0.1 to 0.2 seconds
        
        # otherwise, check if buttons are pressed and set the timer
        # good idea to sleep for 0.2 seconds after performing tasks
        # to give time for fingers to get off buttons

        
        
    # if switch is `False` (right)
    if not cp.switch:
        # check if button A is pressed and timer complete is set to `False`
        # if so, perform looping to display NeoPixel countdown
        # check if button B or switch become `True` in the loops and
        # reset and break if they are.
        # set timer complete to `True` if loops finish without breaking
        
        
        # check if timer complete variable is `True`
        # if so, blink the lights (and play the buzzer if possible)
        # check the slide switch and button B states so you
        # can call the reset function when needed
        
        
        # check the state of button B to reset the timer
        
        