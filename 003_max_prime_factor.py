#003: Find the maximum prime factor of 600851475143
#Ans: 6857


def isPrime(num):
	is_prime = True
	for i in xrange(2, int(num ** 0.5) + 2):
		if num == 1:
			is_prime = False
			break
		elif num == 2:
			break
		else:
			if num % i == 0:
				is_prime = False
				break

	return is_prime


num = 600851475143	#Ans: 6857
max_prime_factor = 1

if isPrime(num):	#if the number is a prime, the number itself will be the largest prime factor
	max_prime_factor = num

else:				#if the number is not a prime
	for i in xrange(1, int(num ** 0.5) + 2):
		if num % i == 0:
			if isPrime(i) and i > max_prime_factor:
				max_prime_factor = i

			j = num / i
			if isPrime(j) and j > max_prime_factor:
				max_prime_factor = j

print ("Maximum prime factor of %d is %d." % (num, max_prime_factor))


# #Nawrin's solution:
# n = 600851475143
# for i in xrange(1, int(n/2) + 1):
# 	if n % i == 0:
# 		n = int(n / i)
# 		print i
# 		if n < i:
# 			break
