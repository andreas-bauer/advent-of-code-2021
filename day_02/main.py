input = open('input.txt', 'r').read().split("\n")

# Part 1
x = 0
depth = 0

for line in input:
	line_elements = line.split(' ')
	cmd = line_elements[0]
	distance = int(line_elements[1])
	
	if cmd == 'forward':
		x += distance
	elif cmd == 'down':
		depth += distance
	else:
		depth += -distance

print('X: ' + str(x))
print('Depth: ' + str(depth))


# Part 2
aim = 0
horizontal = 0
depth = 0

for line in input:
	line_elements = line.split(' ')
	cmd = line_elements[0]
	value = int(line_elements[1])
	if cmd == 'forward':
		horizontal += value
		depth += aim * value
	elif cmd == 'down':
		aim += value
	else:
		aim += -value

print('Part 2')		
print('X: ' + str(x))
print('Depth: ' + str(depth))
print('Answer: ' + str(x * depth))