import subprocess
import pickle
from time import sleep
from random import random, choice

from modules_forecast.servo_rotation import move_to_position


def read_forecast_loudly():

	forecast = pickle.load(open('data/forecast.pkl', 'rb'))
	#forecast = {}
	#print(forecast)
	if not forecast:
		subprocess.run(['aplay', 'voice_data/wav/weather_error.wav', '-q'])
		return

	target = forecast['target']
	weather = forecast['result']
	max_temperature = forecast['max_temperature']
	min_temperature = forecast['min_temperature']

	#print(target, weather, max_temperature, min_temperature)
	move_to_position(weather)

	if target == 'today':
		subprocess.run(['aplay', 'voice_data/wav/weather_kyounonicchuunotenkiwa.wav', '-q'])
	else:
		subprocess.run(['aplay', 'voice_data/wav/weather_ashitanonicchuunotenkiwa.wav', '-q'])

	if weather == 'sunny':
		subprocess.run(['aplay', 'voice_data/wav/weather_sunny.wav', '-q'])
	elif weather == 'cloudy_sunny':
		subprocess.run(['aplay', 'voice_data/wav/weather_cloudy_sunny.wav', '-q'])
	elif weather == 'cloudy':
		subprocess.run(['aplay', 'voice_data/wav/weather_cloudy.wav', '-q'])
	elif weather == 'rain_sunny':
		subprocess.run(['aplay', 'voice_data/wav/weather_rain_sunny.wav', '-q'])
	elif weather == 'rain':
		subprocess.run(['aplay', 'voice_data/wav/weather_rain.wav', '-q'])
	elif weather == 'heavy_rain':
		subprocess.run(['aplay', 'voice_data/wav/weather_heavy_rain.wav', '-q'])
	elif weather == 'snow_sunny':
		subprocess.run(['aplay', 'voice_data/wav/weather_snow_sunny.wav', '-q'])
	elif weather == 'snow':
		subprocess.run(['aplay', 'voice_data/wav/weather_snow.wav', '-q'])
	elif weather == 'thunder':
		subprocess.run(['aplay', 'voice_data/wav/weather_thunder.wav', '-q'])
	sleep(1)

	subprocess.run(['aplay', 'voice_data/wav/weather_max_temp.wav', '-q'])
	if max_temperature == 0:
		subprocess.run(['aplay', 'voice_data/wav/weather_0.wav', '-q'])
	else:
		if max_temperature < 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_minus.wav', '-q'])
		max_temperature_abs = abs(max_temperature)
		max_temperature_abs_d2 = max_temperature_abs // 10
		max_temperature_abs_d1 = max_temperature_abs % 10
		if max_temperature_abs_d2 > 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_%d0.wav' % max_temperature_abs_d2, '-q'])
		if max_temperature_abs_d1 > 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_%d.wav' % max_temperature_abs_d1, '-q'])
	subprocess.run(['aplay', 'voice_data/wav/weather_degree_desu.wav', '-q'])

	sleep(0.5)

	subprocess.run(['aplay', 'voice_data/wav/weather_min_temp.wav', '-q'])
	if min_temperature == 0:
		subprocess.run(['aplay', 'voice_data/wav/weather_0.wav', '-q'])
	else:
		if min_temperature < 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_minus.wav', '-q'])
		min_temperature_abs = abs(min_temperature)
		min_temperature_abs_d2 = min_temperature_abs // 10
		min_temperature_abs_d1 = min_temperature_abs % 10
		if min_temperature_abs_d2 > 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_%d0.wav' % min_temperature_abs_d2, '-q'])
		if min_temperature_abs_d1 > 0:
			subprocess.run(['aplay', 'voice_data/wav/weather_%d.wav' % min_temperature_abs_d1, '-q'])

	subprocess.run(['aplay', 'voice_data/wav/weather_degree_desu.wav', '-q'])

	voice_list = [
		'voice_data/wav/extra/saboon.wav',
		'voice_data/wav/extra/tsuide.wav',
        'voice_data/wav/extra/himiko.wav'
	]
	chosen = choice(voice_list)
	subprocess.run(['aplay', chosen, '-q'])

	return weather