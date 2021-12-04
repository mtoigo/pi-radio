#!/usr/bin/python
# This file should be placed at /home/pi/radio/button.py

#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#  RetroPie Shutdown Button Script
#
# This script enables a RetroPie based
# system to shutdown by pressing a button
# without needing to use the menu.
#
# It uses the GpioZero library and is based on:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#shutdown-button
#
# Please see https://www.raspberrypi-spy.co.uk/
# for more information.
#
# Author : Matt Hawkins
# Date   : 18/03/2018
#
#--------------------------------------

from gpiozero import Button
from subprocess import check_call
from signal import pause

# Define GPIO number
myGPIO=4

# Define number of seconds button should be pressed
myHoldTime=1

def buttonPress():
  check_call(['/home/pi/radio/play.sh'])

button=Button(myGPIO,pull_up=False,hold_time=myHoldTime)
button.when_pressed=buttonPress

pause ()