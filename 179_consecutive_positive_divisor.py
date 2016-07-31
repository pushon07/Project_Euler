#179: Consecutive positive divisors num
#Ans: Takes too much time

def get_num_factors(num):
	num_factors = 0
	i = 2
	factor = num
	while i <= num/2:
		if factor % i == 0:

			factor = factor / i
			num_factors += 1
			#print i
			if factor < 2:
				break
		else:
			if i == 2:
				i += 1
			elif i > 2:
				i += 2

	return num_factors


num = 13878#1*(10**5)-->13878

for i in xrange(1*(10**5), 2*(10**5)):
	if get_num_factors(i) == get_num_factors(i+1):
		num += 1

print num