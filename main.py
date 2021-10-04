import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def on_pushdown(channel):
    print ("Button Pushed.")

# only add the detection call once!
gpio.add_event_detect(26, gpio.RISING, callback=on_pushdown, bouncetime=200)

try:  
    while True : pass  
except:
    GPIO.cleanup()
