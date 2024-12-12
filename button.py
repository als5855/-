import RPi.GPIO as GPIO
import threading 
import time


BUTTON_PIN = 23
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = False

def blink_led():
    global led_state
    while True:
     
        if led_state:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.1)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)



if __name__=="__main__":
    try:
        threadBtn1 = threading.Thread(target=blink_led, daemon=True)
        threadBtn1.start()

        while True:
            button_input = GPIO.input(BUTTON_PIN)
            time.sleep(0.2)
            if button_input == GPIO.HIGH:
                led_state = not led_state
    except KeyboardInterrupt:
        pass 