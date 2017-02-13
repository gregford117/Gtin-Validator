from math import ceil

def private RoundUp(x):
	return ceil(x / 10.0) * 10

def private ValidInput(input_length):
	allowed_lengths = [7, 11, 12, 13, 16, 17]
	return input_length in allowed_lengths

def private IsEven(x):
	return x % 2 == 0

def Gtin(digitsToCalculate):
	input_len = len(str(digitsToCalculate))

	if ValidInput(input_len):
		loop_num = 0 
		number_sum = 0
		for char in list(str(digitsToCalculate)):							
			if int(IsEven(loop_num)) == int(IsEven(input_len + 1)):
				number_sum += int(char) * 3
			else:
				number_sum += int(char)	
			loop_num += 1
		return RoundUp(number_sum) - number_sum
	else:
		raise ValueError('Incorrect Input Length')