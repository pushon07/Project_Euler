#159: Maximum digital root sum
#Ans: 54 (for 3**12 --> (9 * 9 * 9 * 9 * 9 * 9) --> 54)

def get_factors(num):
	list_factor = []
	i = 2
	factor = num
	while i <= num/2:
		if factor % i == 0:

			factor = factor / i
			list_factor.append(i)
			#print i
			if factor < 2:
				break
		else:
			if i == 2:
				i += 1
			elif i > 2:
				i += 2

	return list_factor


num = 10**7
list_factor = get_factors(num)
print list_factor
print len(list_factor)
# list_composits = []
# list_composits.append(list_factor)
# for num_component in xrange(len(list_factor) - 1, 0, -1):
# 	new_composits = [0] * num_component
# 	for i in range(num_component):



