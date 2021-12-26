input = open('input.txt', 'r').read().split('\n')

heatmap = [[int(c) for c in s] for s in input]
x_max = len(heatmap[0])
y_max = len(heatmap) 

print("X range: 0.." + str(x_max))
print("Y range: 0.." + str(y_max))

is_in_range = lambda x,y: (0 <= x < x_max) and (0 <= y < y_max)

def is_lowest(heatmap, x, y):
	depth = heatmap[y][x]
	if is_in_range(x-1,y) and heatmap[y][x-1] <= depth:
		return False		
	if is_in_range(x+1,y) and heatmap[y][x+1] <= depth:
		return False
	if is_in_range(x,y-1) and heatmap[y-1][x] <= depth:
		return False
	if is_in_range(x,y+1) and heatmap[y+1][x] <= depth:
		return False
	return True	

found = []
for y in range(y_max):
	for x in range(x_max):
		if is_lowest(heatmap,x,y):
			found.append(heatmap[y][x] +1)

print("Deep spots found (+1): " + str(found))
print("Sum: " + str(sum(found)))