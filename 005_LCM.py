#LCM

num_digits = 20 #Answer: 232792560
lcm = num_digits * (num_digits - 1) #20 --> slow

while True:
	num_factors = 0
	for i in range(11, num_digits + 1): #same result with range(1, 21) --> slow
		if lcm % i != 0:
			break
		else:
			num_factors += 1

	if num_factors == 10:
		break

	lcm += num_digits * (num_digits - 1) #num_digits --> slow

print lcm