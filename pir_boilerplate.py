
from gpiozero import MotionSensor, LED
from time import sleep
from datetime import datetime
import smtplib
from email.message import EmailMessage
import pygame

pir = MotionSensor(4) # pir.when_motion = led.on # pir.when_motion = led.on
led = LED(14)

# change below to your own email.
# This script is set for use with a gmail account.
sender = "<sender email address>"
recipient= "<recipient email>"


def get_time():
    #TODO: return the current time, formatted.
    print("TODO")


def send_email():
    #TODO: Create an email object and send it.
    # Call get_date() to send a formatted date with your body/subject.
    print("TODO")


def play_sound():
     #TODO: Use pygame to play a sound. Make sure to get one first.
     print("TODO")

def log_incident():
     #TODO: open a text file and append new data. You can call get_date().
     print("TODO")

while True:
    if pir.motion_detected:
        led.on()
        #log_incident()
        #send_email()
        #play_sound()
        #get_time()

        sleep(4) #give a delay, to allow sensor to reset.
    else:
        print("no motion")
        led.off()
