#Sum of primes below 2000000
#Answer: 142913828922 [Finished in 114.4s]

def isPrime(num):
	is_prime = True
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			is_prime = False
			break

	return is_prime

sum_primes = 2	#Since excluded 2 from the prime_list, added it ahead of time	
for i in xrange(3, 2000000, 2):	
	if isPrime(i):
		sum_primes += i

print sum_primes
