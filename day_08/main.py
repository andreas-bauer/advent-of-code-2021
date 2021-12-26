input = open('simple.txt', 'r').read().split('\n')
input_lines =  [s.split(' | ')[0] for s in input]
output_lines = [s.split(' | ')[1] for s in input]

ones = 0
fours = 0
sevens = 0
eights = 0
for line in output_lines:
	line_arr = line.split(' ')
	for element in line_arr:
		if len(element) == 2:
			ones += 1
		elif (len(element)) == 4:
			fours += 1
		elif (len(element)) == 3:
			sevens += 1
		elif (len(element)) == 7:
			eights += 1

print('Part 1 Total: ' + str(ones + fours + sevens + eights))
