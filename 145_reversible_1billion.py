#Reversible number below 1 billion
#Done: takes too much time

def is_reversible(num):
	is_reversible = True
	num_copy = num
	for i in range(len(num_copy)):
		num = num[:i] + num_copy[-i - 1] + num[i+1:]
		
	sum_nums = int(num) + int(num_copy)
	#print num
	#print num_copy
	for k in str(sum_nums):
		if int(k) % 2 == 0:
			return False 

	return is_reversible

num_reversible = 0#68720#10**7
for i in xrange(1, 1000):
	if (i % 10 != 0) and (is_reversible(str(i))):
		num_reversible += 1
		#print i

print num_reversible