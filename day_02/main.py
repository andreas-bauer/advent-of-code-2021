input = open('input.txt', 'r').read().split("\n")

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