from time import sleep
import RPi.GPIO as GPIO

from modules_forecast.read_forecast_loudly import read_forecast_loudly
from modules_forecast.servo_rotation import keep_position
from modules_clock.read_clock import clock_jp, clock_sv

#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.OUT)

weather = None

try:
	while True:
		if GPIO.input(23) == GPIO.HIGH:
			print('read_forecast_loudly')
			GPIO.output(26, GPIO.HIGH)
			weather = read_forecast_loudly()
			GPIO.output(26, GPIO.LOW)
		if GPIO.input(24) == GPIO.HIGH:
			print('clock_jp')
			GPIO.output(26, GPIO.HIGH)
			clock_jp()
			GPIO.output(26, GPIO.LOW)
		if GPIO.input(25) == GPIO.HIGH:
			print('clock_sv')
			GPIO.output(26, GPIO.HIGH)
			clock_sv()
			GPIO.output(26, GPIO.LOW)
		keep_position(weather)
		sleep(0.2)


except KeyboardInterrupt:
	pass

GPIO.cleanup()