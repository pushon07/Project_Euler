#LARGEST PRODUCT IN A SERIES

number_string = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843'\
				+ '8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557'
num_adjacent_digit = 4
max_product = 1
for i in xrange(len(number_string) - num_adjacent_digit + 1):
	product = 1
	for j in xrange(num_adjacent_digit):
		product *= int(number_string[i + j])
	if product > max_product:
		max_product = product

print max_product
print len(number_string)