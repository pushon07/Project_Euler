#4-digit prime permutations
#Answer: 2969-6299-9629 [Finished in 5.5s]

def isPrime(num):
	is_prime = True
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			is_prime = False
			break

	return is_prime

def threePrimes(primes):
	for i in xrange(0, len(primes) - 2):
		prime_1 = primes[i]
		for j in xrange(i + 1, len(primes) - 1):
			prime_2 = primes[j]
			prime_3 = prime_2 + (prime_2 - prime_1)
			if isPrime(prime_3) and prime_3 != 8147:
				list_prime1 = list(str(prime_1))
				list_prime1.sort()
				list_prime2 = list(str(prime_2))
				list_prime2.sort()
				list_prime3 = list(str(prime_3))
				list_prime3.sort()
				if (list_prime1 == list_prime2 == list_prime3):
					return str(prime_1) + str(prime_2) + str(prime_3)

prime_nums = []
#sum_p = 0
for num in xrange(1000, 10000):
	if isPrime(num):
		#sum_p += num
		prime_nums.append(num)
	
output_str = threePrimes(prime_nums)
#print prime_nums
#print sum_p
print output_str

