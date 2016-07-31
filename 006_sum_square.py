max_num = 100
sum_squares = 0

for i in xrange(1, max_num + 1):
	sum_squares += i ** 2

square_sums = (max_num * (max_num + 1) / 2.0) ** 2

print ("Sum_of_squares=%d; Square_of_sums=%d" % (sum_squares, square_sums))
print ("The difference = %d" % (square_sums - sum_squares))