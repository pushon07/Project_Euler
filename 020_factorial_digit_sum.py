#20: Factorial digit sum
#Ans: 648

def get_factorial(num):
	factorial = 1
	for i in xrange(num, 1, -1):
		factorial *= i

	return factorial

num = 100000
factorial = get_factorial(num)
sum_digit = 0
for d in str(factorial):
	sum_digit += int(d)

#print factorial
print sum_digit