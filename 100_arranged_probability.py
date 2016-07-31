#Prob-100: Arranged probability
#Ans: total_disc=1000000002604, blue_disc=707106783028 | [Finished in 0.1s]

total_disc = 1000000000000#10 ** 12
while  True:
	blue_disc = ((total_disc * (total_disc - 1)) / 2.0) ** 0.5
	blue_disc = blue_disc // 1
	blue_disc += 1
	if ((blue_disc * (blue_disc - 1) * 1.0)  / (total_disc * (total_disc -1))) == 0.50:
		break

	total_disc += 1

print ("total_disc=%f, blue_disc=%f" % (total_disc, blue_disc))