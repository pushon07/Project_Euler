
def get_factorial(num):
	factorial = 1
	for i in xrange(num, 1, -1):
		factorial *= i

	return factorial


sum_num = 0

for num in xrange(1, 10 ** 6):
	sum_digit_factorial = 0
	for digit in str(num):
		sum_digit_factorial += get_factorial(int(digit))

	if num == sum_digit_factorial:
		sum_num += num
		print num