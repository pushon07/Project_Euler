#171: Sum of digits-squares-sum-->perfect square below 10**20
#Takes too much time 

import math

def is_square(num):
	value = int(math.sqrt(num))

	if value ** 2 == num:
		return True
	else:
		return False

sum_n = 0
for i in xrange(1, 10**10):
	val_str = str(i)
	val_sum = 0
	for val in val_str:
		val_sum += int(val) ** 2
	if is_square(val_sum):
		#print i
		sum_n += i

print sum_n