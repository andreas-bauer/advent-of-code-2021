from collections import namedtuple
import numpy as np

input = open('input.txt','r').read().split('\n')
input = [[int(c) for c in lines] for lines in input]
x_max = len(input[0])
y_max = len(input) 

energies = np.array(input)
will_flash = lambda arr : len(np.where(arr >= 9)[0]) > 0

Point = namedtuple('Point', ['x', 'y'])
Range = namedtuple('Range', ['x_from','x_to', 'y_from','y_to'])
def first_flash(arr):
	all = np.where(arr >= 9)
	return Point(x=all[1][0], y=all[0][0])	

def flash_range(x,y):
	return Range(
		x_from= x - (x > 0),
		x_to= x + (x < x_max),
		y_from= y - (y > 0),
		y_to= y + (y < y_max)
	)

total_flashes = 0
for i in range(1,101):
	step_flashes = 0
	while will_flash(energies):
		first = first_flash(energies)
		r = flash_range(first.x, first.y)
		energies[first.y][first.x] = -9_000
		energies[r.y_from:r.y_to + 1,r.x_from:r.x_to + 1] += 1
		step_flashes += 1
	print('[' + str(i) + '] Flashed ' + str(step_flashes) + ' times')
	energies += 1
	energies[energies < 0] = 0
	total_flashes += step_flashes
print('Total flashes: ' + str(total_flashes))