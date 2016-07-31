#Takes too much time

#import gmpy

import math

# i = 1
# n = 1
# while True:
# 	print i
# 	i += 2 * n + 1
# 	n += 1
# 	if i > 225:
# 		break

def is_sqrt(num):
	value = int(round(math.sqrt(num)))

	if value ** 2 == num:
		return True
	else:
		return False

def perfect_squares():
	for z in xrange(1, 50000):
		if z % 1000 == 0:
			print z
		for y in xrange(z+1, 100001):
			if is_sqrt(y + z) and is_sqrt(y - z):
				for x in xrange(y+1, 500002):
					if is_sqrt(x + y) and is_sqrt(x - y) and is_sqrt(x + z) and is_sqrt(x - z):
						return x, y, z
				
	return 0, 0, 0


x, y, z = perfect_squares()
print x
print y
print z