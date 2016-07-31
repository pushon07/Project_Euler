#10001st prime number

def isPrime(num):
	is_prime = True
	for i in range(2, int(num ** 0.5) + 2):
		if num % i == 0:
			is_prime = False
			break

	return is_prime

i = 3
count = 1
while True:	
	if isPrime(i):
		count += 1

	if count == 10001:	#to find 10001st prime number
		break

	i += 2

print i	#Ans: 104743
