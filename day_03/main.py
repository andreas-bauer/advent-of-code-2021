input = open('input.txt','r').read().split('\n')

line_size = len(input[0])	
half = len(input) / 2

axial_sum = [0] * line_size

for line in input:
	for i in range(line_size):
		as_num = line[i]
		axial_sum[i] += int(line[i])

gamma_bool_arr = [int(n > half) for n in axial_sum]
epsilon_bool_arr = [int(not b) for b in gamma_bool_arr]

gamma = int("".join(str(b) for b in gamma_bool_arr), 2) 
epsilon = int(''.join([str(b) for b in epsilon_bool_arr]),2)

print('Gamma: ' + str(gamma))
print('Epsilon: ' + str(epsilon))
