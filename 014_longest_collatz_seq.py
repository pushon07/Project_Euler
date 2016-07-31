#14: Longest Collatz sequence
#Ans: 525

def get_collatz_seq_length(num):
	length_seq = 1
	while True:
		if num == 1:
			break
		elif num % 2 == 0:
			num = num / 2
		elif num %2 != 0:
			num = (3 * num) + 1

		length_seq += 1

	return length_seq


num_start = 800000
max_length_seq = 400

while True:
	if num_start > 1000000:
		break
	length_seq = get_collatz_seq_length(num_start)
	if length_seq > max_length_seq:
		max_length_seq = length_seq
		print "max_length=%d; num=%d" % (max_length_seq, num_start)

	num_start += 1

print max_length_seq