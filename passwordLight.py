import RPi.GPIO as gpio
import threading 
import time

BUTTON_PIN = [24, 23, 27]
LED_PIN = 17

PASSWORD = [1, 2, 3]

gpio.setmode(gpio.BCM)
gpio.setup(BUTTON_PIN, gpio.IN, pull_up_down=gpio.PUD_DOWN)


gpio.setup(LED_PIN, gpio.OUT)

led_state = False

def blink_led():
    global led_state
    while True:

        if not PASSWORD and led_state:
            gpio.output(LED_PIN, gpio.HIGH)
            time.sleep(0.1) 
            gpio.output(LED_PIN, gpio.LOW)
            time.sleep(0.1)
        elif PASSWORD and led_state :
            gpio.output(LED_PIN, gpio.HIGH)
        else :
            gpio.output(LED_PIN, gpio.LOW) 

if __name__ == "__main__" :
    try:
       pass

    except KeyboardInterrupt:
        pass





