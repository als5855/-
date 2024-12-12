import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

buttonPin = 23

gpio.setup(17, gpio.OUT)
gpio.output(17, gpio.LOW)
gpio.setup(22, gpio.OUT)
gpio.output(22, gpio.LOW)

gpio.setup(buttonPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

while True:
    if gpio.input(buttonPin):
        gpio.output(17, gpio.HIGH)
        time.sleep(0.1)
        gpio.output(17, gpio.LOW)
        time.sleep(0.1)

    elif not gpio.input(buttonPin):
            gpio.output(22, gpio.HIGH)
            time.sleep(0.1)
            gpio.output(22, gpio.LOW)
            time.sleep(0.1)

    
    # if gpio.input(buttonPin): #-버튼누르면 불빛이 교대로 왔다갔다한다.
    #     gpio.output(17, gpio.HIGH)
    #     gpio.output(22, gpio.LOW)
    # elif gpio.input(buttonPin) == False:
    #    gpio.output(22, gpio.HIGH)
    #    gpio.output(17, gpio.LOW)
    
    # if gpio.input(buttonPin): #-버튼누르면 불이켜진다.
    #    gpio.output(17, gpio.HIGH)
    #    gpio.output(17, gpio.LOW)
    #    gpio.output(22, gpio.HIGH)
    #    gpio.output(22, gpio.LOW)

    
    # if not gpio.input(buttonPin): #-버튼누르면 불이꺼진다.
    #    gpio.output(17, gpio.HIGH)
    #    gpio.output(17, gpio.LOW)
    #    gpio.output(22, gpio.HIGH)
    #    gpio.output(22, gpio.LOW)
        
 

    
 

        
   
    