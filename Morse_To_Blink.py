import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)



def ConvertToBlink(textToBlink, LED, unit):
    for i in range(len(textToBlink)):
        if textToBlink[i] == '.':
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(unit)
        elif textToBlink[i] == '-':
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(unit*3)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(unit)



