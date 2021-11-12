import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN=9
BUZZER_PIN=11
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

GPIO.output(LED_PIN,True)
GPIO.output(BUZZER_PIN,True)
time.sleep(2)
GPIO.output(LED_PIN,False)
GPIO.output(BUZZER_PIN,False)