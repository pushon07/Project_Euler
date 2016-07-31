#First four consecutive numbers having four distinct prime factors
#Ans: 134043 (3, 7, 13, 491); 134044 (2, 23, 31, 47); 134045 (5, 17, 19, 83); 134046 (2, 3, 11, 677)

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


def hasFourPrimeFactor(num):

	num_prime_factor = 0

	if isPrime(num):
		return False

	else:
		for i in xrange(1, int(num ** 0.5) + 2):
			if num % i == 0:
				if isPrime(i) and i < j:
					#print "num=%d, factor=%d" % (num, i)
					num_prime_factor += 1

				j = num / i
				if isPrime(j) and j > i:
					#print "num=%d, factor=%d" % (num, j)
					num_prime_factor += 1

			if num_prime_factor == 4:
				return True
	return False


first_prime = 0
for num1 in xrange(644, 10000000):
	#if (isPrimeFactor(num1) and isPrimeFactor(num1+1) and isPrimeFactor(num1+2) and isPrimeFactor(num1+3)):
	if (hasFourPrimeFactor(num1) and hasFourPrimeFactor(num1+1) and hasFourPrimeFactor(num1+2) and hasFourPrimeFactor(num1+3)):
		first_prime = num1
		break


print first_prime