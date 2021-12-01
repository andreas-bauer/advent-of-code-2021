input = open('input.txt', 'r').read().split("\n")
measurements = [int(i) for i in input]

# part 1
incs = []
for i in range(1, len(measurements)):
	is_increase = measurements[i] > measurements[i -1]
	incs.append(is_increase)

print("Part 1")
print("depth increased: " + str(sum(incs)))
print("depth decreased: " + str(len(incs) - sum(incs)))

# part 2
measurements = [int(i) for i in input]
def measure_with_window(values, window_size):
	counter_inc = -1
	counter_dec = 0
	last = 0

	for i in range(window_size -1, len(values)  ):
		window_sum = 0
		for j in range(window_size):
			window_sum += values[i - j]
		
		if window_sum > last:
			counter_inc += 1
		else:
			counter_dec += 1
		last = window_sum
	
	print("depth increased: " + str(counter_inc))
	print("depth decreased: " + str(counter_dec))


print("Part 2")
measure_with_window(measurements,3)