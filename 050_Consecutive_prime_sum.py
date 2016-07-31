#Longest consecutive prime sum
#Ans: Sum=997651 (7 to 3931); num_primes=543 | [Finished in 28.2s]


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

consecutive_prime_sum = 0
longest_streak = 0
max_prime_sum = 1000000
for i in xrange(1, max_prime_sum/200, 2):
	if consecutive_prime_sum >= max_prime_sum:
		break
	prime_sum = 0
	if isPrime(i):
		prime_sum += i
		n_chance = 0
		streak = 1
		for j in xrange(i+2, max_prime_sum/200, 2):
			if prime_sum >= max_prime_sum or n_chance > 1000:
				break
			if isPrime(j):
				prime_sum += j
				streak += 1
				if isPrime(prime_sum):
					if streak > longest_streak and prime_sum < max_prime_sum:
						longest_streak = streak
						consecutive_prime_sum = prime_sum
						print ("sum=%d, max_streak=%d, i=%d, j=%d" % (prime_sum, longest_streak, i, j))
				else:
					n_chance += 1

print consecutive_prime_sum
print longest_streak