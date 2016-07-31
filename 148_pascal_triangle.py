#Pascal's triangle: takes too much time

num_div = 0
row_num = 2
prev_row_values = [1, 1]
while  True:
	
	row_values = [1] * (row_num + 1)
	if row_num > (10 * 2) - 1:
		break

	for i in xrange(1, row_num):
		row_values[i] = prev_row_values[i - 1] + prev_row_values[i]
		if row_values[i] % 7 == 0:
			#print row_values[i]
			num_div += 1
	prev_row_values = row_values
	print prev_row_values

	row_num += 1

print num_div# + ((2 * row_num) - 3)
total  = (row_num * (row_num + 1) / 2)
num_not_div_7 = total - num_div
print num_not_div_7