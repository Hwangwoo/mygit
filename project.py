import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
GPUO.setup(23,GPIO.IN)

motor = GPIO.PWM(17,50)
motor.start(70)
duty=10

try:
	while True:
		inputValue1=GPIO.input(24)
		inputValue2=GPIO.input(23)
		if(inputValue1 == True):
			motor.ChangeDutyCycle(duty)
			time.sleep(0.1)
			duty = duty-1
		if(inputValue2 == True):
			motor.ChangeDutyCycle(duty)
			time.sleep(0.1)
			duty = duty+1
except KeyboardInterrupt:
	GPIO.cleanup()

















