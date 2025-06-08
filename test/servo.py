import pigpio
import time
import numpy as np

GPIO_PIN = 21

pi = pigpio.pi()


def set_position(degree):
	pi.set_servo_pulsewidth(GPIO_PIN, degree)
	
	
def move_between_positions(start_degree, end_degree):
	move_sec = abs(end_degree - start_degree) / 1600 * 10

	start_time = time.monotonic()
	end_time = start_time + move_sec

	time_to_degree = np.poly1d(np.polyfit([start_time, end_time], [start_degree, end_degree], 1))

	while True:
		now_time = time.monotonic()
		if now_time >= end_time:
			break
		degree = time_to_degree(now_time)
		print(degree)
		set_position(degree)


if __name__ == "__main__":
	set_position(1000)
	time.sleep(2)
	set_position(1300)
	time.sleep(2)
	set_position(1600)
	time.sleep(2)
	set_position(1900)
	time.sleep(2)
	move_between_positions(700, 2100)