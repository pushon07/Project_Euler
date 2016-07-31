
import random

board_state = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, '11':0, '12':0, '13':0,\
 '14':0, '15':0, '16':0, '17':0, '18':0, '19':0, '20':0, '21':0, '22':0, '23':0, '24':0, '25':0, '26':0, '27':0,\
 '28':0, '29':0, '30':0, '31':0, '32':0, '33':0, '34':0, '35':0, '36':0, '37':0, '38':0, '39':0}

cc_options = ['Jail', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'GO']
ch_options = ['Jail', '11', '24', '39', '5', 'NR', 'NR', 'NU', 'B3', '_', '_', '_', '_', '_', '_', 'GO']
random.shuffle(cc_options)
random.shuffle(ch_options)

position = 0
num_double = 0

for num_move in xrange(100000):
	dice1 = random.choice([1, 2, 3, 4, 5, 6])
	dice2 = random.choice([1, 2, 3, 4, 5, 6])

	move = dice1 + dice2
	if move == 2:
		num_double += 1
	else:
		num_double == 0

	position += move
	if position == 40:
		position = 0
	elif position > 40:
		position = position - 40

	#Game rules
	def communityChestPosition(position):
		cc_move = cc_options[0]
		for i in range(len(cc_options)):
			cc_options[i] = cc_options[i - 1]
		if cc_move == 'GO':
			position = 0
		elif cc_move == 'Jail':
			position = 10
		else:
			position = position

		return position

	def chancesPosition(position):
		ch_move = ch_options[0]
		for i in range(len(ch_options)):
			ch_options[i] = ch_options[i - 1]
		if ch_move == 'GO':
			position = 0
		elif ch_move == 'Jail':
			position = 10
		elif ch_move == '5':
			position = 5
		elif ch_move == '11':
			position = 11
		elif ch_move == '24':
			position = 24
		elif ch_move == '39':
			position = 39
		elif ch_move == 'NR':
			if position == 7:
				position = 15
			elif position == 22:
				position = 25
			elif position == 36:
				position = 5
		elif ch_move == 'B3':
			position = position - 3
			if position == 33:
				position = communityChestPosition(position)
		elif ch_move == 'NU':
			if position == 7:
				position = 12
			elif position == 22:
				position = 28
			elif position == 36:
				position = 12
		else:
			position = position		

		return position

	if num_double == 3:	#if three consecutive double, go to Jail
		position = 10
		num_double = 0
	if position == 30:	#If Go to Jail, go to jail
		position = 10

	if position in (2, 17, 33):	#if community chest
		position = communityChestPosition(position)

	if position in (7, 22, 36):	#if chance
		position = chancesPosition(position)

	board_state[str(position)] += 1

sq_1 = 0
sq_2 = 0
sq_3 = 0
top_three = {'1st':0, '2nd':0, '3rd':0}
for key, val in board_state.iteritems():
	if val > sq_1 and val > sq_2 and val > sq_3:
		top_three['1st'] = key
		sq_1 = val
	elif val < sq_1 and val > sq_2 and val > sq_3:
		top_three['2nd'] = key
		sq_2 = val
	elif val < sq_1 and val < sq_2 and val > sq_3:
		top_three['3rd'] = key
		sq_3 = val

print board_state
print "\nTop three=%s" %top_three