import tm1637
import time

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

def display(digit1, digit2, digit3, digit4, colon):
	digit1 = ' ' if digit1 in ['', ' ', None] else str(digit1)
	digit2 = ' ' if digit2 in ['', ' ', None] else str(digit2)
	digit3 = ' ' if digit3 in ['', ' ', None] else str(digit3)
	digit4 = ' ' if digit4 in ['', ' ', None] else str(digit4)
	
	tm.write([
		dict_num_to_bin[str(digit1)],
		dict_num_to_bin[str(digit2) + (':' if colon else '') ],
		dict_num_to_bin[str(digit3)],
		dict_num_to_bin[str(digit4)]
	])	


if __name__ == "__main__":
	display(1, 2, 8, 9, True)
	time.sleep(5)
	display(9, 8, 5, 4, False)
	time.sleep(5)
	display('', 6, None, 7, False)
	time.sleep(5)
	display(0, None, 4, ' ', True)