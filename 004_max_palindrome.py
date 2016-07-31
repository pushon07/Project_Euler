def isPalindrome(num):
	is_palindrome = True
	for i in range(1, (len(num) / 2) + 1):
		if (num[i - 1] != num[-i]):
			is_palindrome = False

	return is_palindrome


max_product = 0

for num_1 in range(1000, 100, -1):
	for num_2 in range(1000, 100, -1):
		product = num_1 * num_2
		if isPalindrome(str(product)) and product > max_product:
			max_product = product
			print ('%d, %d' % (num_1, num_2))

print (max_product)	#Ans: 906609