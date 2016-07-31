#Product of the pythagorean triplet
#Answer: 31875000 (200, 375, 425)

found_pythagorean = False

for num_1 in xrange(1, 333):
	for num_2 in xrange(num_1 + 1, 667 - num_1):
		num_3 = 1000 - (num_1 + num_2)
		if ((num_1 ** 2) + (num_2 ** 2) == (num_3 ** 2)):
			found_pythagorean = True
			break
	if found_pythagorean:
		break

print ("%d, %d, %d" % (num_1, num_2, num_3))

product_pythagorean = num_1 * num_2 * num_3
print ("Product of the pythagorean = %d" % product_pythagorean)