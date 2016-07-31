

def isPrime(num):
	is_prime = True
	for i in range(2, int(num ** 0.5) + 2):
		if num == 1:
			is_prime = False
			break
		elif num == 2:
			is_prime = True
			break
		else:
			if num % i == 0:
				is_prime = False
				break

	return is_prime

num_digit = 0
digit = '6'
max_digit = 0
sum_digits = 0

for i in xrange((10 ** 3) + 1, 10 ** 4, 2):
	
	if isPrime(i):
		if digit in str(i):
			count = str(i).count(digit)
			if count > max_digit:
				max_digit = count
				sum_digits = i
				num_digit = 1
			elif count == max_digit:
				sum_digits += i
				num_digit += 1

print max_digit
print num_digit
print sum_digits