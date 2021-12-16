import numpy as np
input = open('input.txt','r').read().split('\n')

coords_str = [s.replace(' -> ', ',').split(',') for s in input]
coords = np.array(coords_str).astype(int)

m_size = 1000

overlaps = np.zeros((m_size,m_size))
def is_horizontal(vec):
	return vec[1] == vec[3]
def is_vertical(vec):
	return vec[0] == vec[2]
for vec in coords:
	if is_horizontal(vec):
		x1 = min(vec[0], vec[2])
		x2 = max(vec[0], vec[2])
		y = vec[1]
		overlaps[y,x1:x2+1] += 1
	elif is_vertical(vec):
		y1 = min(vec[1], vec[3])
		y2 = max(vec[1], vec[3])	
		x = vec[0]
		overlaps[y1:y2+1,x] += 1
	else:
		x1, y1, x2, y2 = vec
		x_factor = 1
		y_factor = 1
		if x1 > x2:
			x_factor = -1
		if y1 > y2:
			y_factor = -1
		while x1 != x2:
			overlaps[y1, x1] += 1
			x1 += x_factor
			y1 += y_factor
		overlaps[y1, x1] += 1

print(sum(sum(overlaps >= 2)))
