import tm1637
import time
import datetime

tm = tm1637.TM1637(clk=5, dio=4)

dict_num_to_bin = {
	' ': 0b00000000,
	'0': 0b00111111,
	'1': 0b00000110,
	'2': 0b01011011,
	'3': 0b01001111,
	'4': 0b01100110,
	'5': 0b01101101,
	'6': 0b01111101,
	'7': 0b00000111,
	'8': 0b01111111,
	'9': 0b01101111,
	' :': 0b10000000,
	'0:': 0b10111111,
	'1:': 0b10000110,
	'2:': 0b11011011,
	'3:': 0b11001111,
	'4:': 0b11100110,
	'5:': 0b11101101,
	'6:': 0b11111101,
	'7:': 0b10000111,
	'8:': 0b11111111,
	'9:': 0b11101111,	
}

while True:
	timestamp = datetime.datetime.now()
	hour = timestamp.hour
	minute = timestamp.minute

	if hour > 12:
		hour -= 12
	if hour >= 10:
		digit1 = str(1)
		digit2 = str(hour - 10)
	else:
		digit1 = ' '
		digit2 = str(hour)

	if minute >= 10:
		digit3 = str(minute // 10)
		digit4 = str(minute % 10)
	else:
		digit3 = str(0)
		digit4 = str(minute)

	tm.write([
		dict_num_to_bin[digit1],
		dict_num_to_bin[digit2 + ':'],
		dict_num_to_bin[digit3],
		dict_num_to_bin[digit4]
		])
	time.sleep(1)
	tm.write([
		dict_num_to_bin[digit1],
		dict_num_to_bin[digit2],
		dict_num_to_bin[digit3],
		dict_num_to_bin[digit4]
		])
	time.sleep(1)
