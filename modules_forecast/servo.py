import pigpio
import time
import numpy as np

GPIO_PIN = 21

pi = pigpio.pi()

weather_to_degree = {
	'thunder':       783,
	'snow':          970,
	'snow_sunny':   1157,
	'heavy_rain':   1344,
	'rain':         1530,
	'rain_sunny':   1717,
	'cloudy':       1904,
	'cloudy_sunny': 2090,
	'sunny':        2277
}

def move_to_position(weather):
	#pi.set_servo_pulsewidth(GPIO_PIN, 1530)

	start_deg = 700
	end_deg = weather_to_degree[weather]

	move_sec = abs(end_deg - start_deg) / 1600 * 10

	start_time = time.monotonic()
	end_time = start_time + move_sec

	time_to_deg = np.poly1d(np.polyfit([start_time, end_time], [start_deg, end_deg], 1))

	while True:
		now_time = time.monotonic()
		if now_time >= end_time:
			break
		deg = time_to_deg(now_time)
		#print(deg)
		pi.set_servo_pulsewidth(GPIO_PIN, deg)

def keep_position(weather=None):
	if weather:
		pi.set_servo_pulsewidth(GPIO_PIN, weather_to_degree[weather])


# for weather in weather_to_degree.keys():
# 	keep_position(weather)
# 	time.sleep(1)