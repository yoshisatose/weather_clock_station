import subprocess
from datetime import datetime
from random import random, choice

def get_time():
	now = datetime.now()
	hour, minute = now.hour, now.minute
	if hour > 12:
		hour -= 12
	return hour, minute


def clock_jp():
	# Japanese
	hour, minute = get_time()

	subprocess.run(['aplay', 'voice_data/wav/jp_ima_wa.wav', '-q'])

	if hour < 10:
		subprocess.run(['aplay', 'voice_data/wav/jp_0%dh.wav' % hour, '-q'])
	else:
		subprocess.run(['aplay', 'voice_data/wav/jp_%dh.wav' % hour, '-q'])

	if minute == 0:
		pass
	elif minute < 10:
		subprocess.run(['aplay', 'voice_data/wav/jp_0%dm.wav' % minute, '-q'])
	elif minute % 10 == 0:
		subprocess.run(['aplay', 'voice_data/wav/jp_%dm.wav' % minute, '-q'])
	else:
		subprocess.run(['aplay', 'voice_data/wav/jp_%d.wav' % (minute // 10 * 10), '-q'])
		subprocess.run(['aplay', 'voice_data/wav/jp_0%dm.wav' % (minute % 10), '-q'])
	subprocess.run(['aplay', 'voice_data/wav/jp_desu.wav', '-q'])

	# r = random()
	# if r < 0.25:
	# 	subprocess.run(['aplay', 'voice_data/wav/extra/utangenkigenki.wav', '-q'])
	# elif r < 0.5:
	# 	subprocess.run(['aplay', 'voice_data/wav/extra/tsumiki.wav', '-q'])
	# elif r < 0.75:
	# 	subprocess.run(['aplay', 'voice_data/wav/extra/muzumuzu.wav', '-q'])
	# else:
	# 	subprocess.run(['aplay', 'voice_data/wav/extra/chicchi.wav', '-q'])

	voice_list = [
		'voice_data/wav/extra/utangenkigenki.wav',
		'voice_data/wav/extra/tsumiki.wav',
		'voice_data/wav/extra/muzumuzu.wav',
		'voice_data/wav/extra/chicchi.wav'
	]
	chosen = choice(voice_list)
	subprocess.run(['aplay', chosen, '-q'])


def clock_sv():
	# Swedish
	hour, minute = get_time()

	if hour < 10:
		subprocess.run(['aplay', 'voice_data/wav/sv_0%dh.wav' % hour, '-q'])
	else:
		subprocess.run(['aplay', 'voice_data/wav/sv_%dh.wav' % hour, '-q'])

	if minute == 0:
		pass
	elif minute < 10:
		subprocess.run(['aplay', 'voice_data/wav/sv_0%dm.wav' % minute, '-q'])
	elif minute < 20:
		subprocess.run(['aplay', 'voice_data/wav/sv_%dm.wav' % minute, '-q'])
	elif minute % 10 == 0:
		subprocess.run(['aplay', 'voice_data/wav/sv_%dm.wav' % minute, '-q'])
	else:
		subprocess.run(['aplay', 'voice_data/wav/sv_%d.wav' % (minute // 10 * 10), '-q'])
		subprocess.run(['aplay', 'voice_data/wav/sv_0%dm_following.wav' % (minute % 10), '-q'])

	#subprocess.run(['aplay', 'voice_data/wav/omaru.wav', '-q'])