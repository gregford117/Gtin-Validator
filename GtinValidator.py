from math import ceil

def RoundUp(x):
	return ceil(x / 10.0) * 10

def ValidInput(input_length):
	allowed_lengths = [7, 11, 12, 13, 16, 17]
	return input_length in allowed_lengths

def Gtin(digitsToCalculate):
	input_len = len(str(digitsToCalculate))

	if ValidInput(input_len):
		loop_num = 0 
		for char in list(str(digitsToCalculate)):							
			if loop_num % 2 == ( input_len % 2 ):
				print(char)			
			#else:
			#	print('loop num = %s\ncurrent char = %s' % (loop_num, char))				

			loop_num += 1
	else:
		raise ValueError('Incorrect Input Length')

if __name__ == '__main__':	
	Gtin(1234567)