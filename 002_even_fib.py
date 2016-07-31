a = 0
b = 1
fib_sum = 0

while True:
	num = a + b
	a = b
	b = num

	if num % 2 == 0:
		print ("%d" % num)
		fib_sum += num
	if num > 4000000:	#if a value the series exceeds 4000000, terminate the series
		break

print ("\nThe sum of even Fibonacci series is: %d" %fib_sum) #Ans: 4613732