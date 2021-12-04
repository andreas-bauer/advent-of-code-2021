input = open('input.txt','r').read().split('\n')

def determine_most_common(input_arr):
	axial_sum = [0] * line_size
	line_size = len(input[0])	
	half = len(input_arr) / 2

	for line in input_arr:
		for i in range(line_size):
			as_num = line[i]
			axial_sum[i] += int(line[i])

	gamma_bool_arr = [int(n > half) for n in axial_sum]
	epsilon_bool_arr = [int(not b) for b in gamma_bool_arr]
	return gamma_bool_arr, epsilon_bool_arr


gamma_bool_arr, epsilon_bool_arr = determine_most_common(input)

gamma = int("".join(str(b) for b in gamma_bool_arr), 2) 
epsilon = int(''.join([str(b) for b in epsilon_bool_arr]),2)

print('Gamma: ' + str(gamma))
print('Epsilon: ' + str(epsilon))
