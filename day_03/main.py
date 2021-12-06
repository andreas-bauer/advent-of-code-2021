input = open('input.txt','r').read().split('\n')

def determine_most_common(input_arr):
	line_size = len(input[0])	
	ones = [0] * line_size
	zeros = [0] * line_size

	for line in input_arr:
		for i in range(line_size):
			if line[i] == '1':
				ones[i] += 1
			elif line[i] == '0': 
				zeros[i] += 1

	bool_arr = [0] * line_size
	for i in range(line_size):
		bool_arr[i] = ones[i] >= zeros[i]
	
	return bool_arr

def bool_arr_to_int(bool_arr):
	return int(''.join(str(int(b)) for b in bool_arr), 2)

def invert_bool_arr(bool_arr):
	return [(not b) for b in bool_arr]

gamma_bool_arr = determine_most_common(input)
epsilon_bool_arr = invert_bool_arr(gamma_bool_arr)

gamma = bool_arr_to_int(gamma_bool_arr)
epsilon = bool_arr_to_int(epsilon_bool_arr)

print('Gamma: ' + str(gamma))
print('Epsilon: ' + str(epsilon))

# Part 2

print('Part 2')

def search_in_code(input_arr, least_common = False):
	line_size = len(input_arr[0])
	filter_term = ''
	filtered = input_arr
	for i in range(line_size):
		filtered = [x for x in filtered if x.startswith(filter_term)]
		if len(filtered) <= 1:
			return filtered[0]
		gamma_arr = determine_most_common(filtered)
		next_term = gamma_arr[i]
		if least_common:
			next_term = not next_term
		filter_term += str(int(next_term))

	return filter_term

oxygen_bool_arr = search_in_code(input)
oxygen = bool_arr_to_int(oxygen_bool_arr)
co2_bool_arr = search_in_code(input, True)
co2 = bool_arr_to_int(co2_bool_arr)

print('Oxygen: ' + str(oxygen))
print('CO2: ' + str(co2))
print('Sum: ' + str(oxygen * co2))
