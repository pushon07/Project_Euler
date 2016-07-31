#200: 200th prime sqube
#Solved: Takes too much time

import math

def is_square(num):
	value = int(round(math.sqrt(num)))

	if value ** 2 == num:
		return True
	else:
		return False

def is_cube(num):
	value = int(round(num ** (1.0/3)))

	if value ** 3 == num:
		return True
	else:
		return False

def is_prime(num):
	is_prime = True
	for i in xrange(2, int(num ** 0.5) + 2):
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

def is_sqube(num):
	i = 2
	j = 0
	p = 0
	q = 0
	while i <= int(num/8):
		if num % i == 0:
			j = num / i

			if is_square(i) and is_cube(j) and is_prime(math.sqrt(i)) and is_prime(int(round(j ** (1.0/3)))):
				p = math.sqrt(i)
				q = int(round(j ** (1.0/3)))
			 	if p != q:
					return True
				

			elif is_square(j) and is_cube(i) and is_prime(math.sqrt(j)) and is_prime(int(round(i ** (1.0/3)))):			
				p = math.sqrt(j)
				q = int(round(i ** (1.0/3)))
				if p != q:
					return True

		i += 1
		#print i
	return False


def is_prime_proof_squib(num):
	num_str = str(num)
	for d in xrange(len(num_str)-2):
		three_digits = num_str[d:d+3]
		if three_digits == '200':
			return True

	return False



n = 40328
prev_sqube = 72
num_sqube = 85
num_prime_proof_squib = 0
min_incr = 500
while True:
	if is_sqube(n):
		#print n
		increment = n - prev_sqube
		if min_incr > increment:
			min_incr = increment
			print increment
		prev_sqube = n
		num_sqube += 1
		# if is_prime_proof_squib(n):
		# 	print n
		# 	num_prime_proof_squib += 1
		if num_sqube >= 87:
			break

	if is_sqube(n):
		n += 1#increment
	else:
		n += 1

print ''
print num_prime_proof_squib
print n
