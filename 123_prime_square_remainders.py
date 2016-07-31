#Prime square remainder
#Ans: 21035 (237737)

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


def getRemainder(num, n):
	remainder = (((num - 1) ** n) + ((num + 1) ** n)) % (num ** 2)
	return remainder

current_prime = 224897
n = 20011 #9 * (10 ** 9)
while True:
	remainder = getRemainder(current_prime, n)
	if remainder > 1 * (10 ** 10):
		print n
		print current_prime
		break
	else:
		while True:
			current_prime += 2
			if isPrime(current_prime):
				n += 1
				break

# current_prime = 211369
# n = 18925 #8 * (10 ** 9)

# current_prime = 224897
# n = 20011 #9 * (10 ** 9)