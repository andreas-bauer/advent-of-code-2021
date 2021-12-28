input = open('input.txt','r').read().split('\n')

def char_as_int(char):
	if char == "(":
		return -3
	if char == ")":
		return 3
	if char == "[":
		return -57
	if char == "]":
		return 57
	if char == "{":
		return -1197
	if char == "}":
		return 1197
	if char == "<":
		return -25137
	if char == ">":
		return 25137
	return 0

def corrupted_char(line, stack):
	for c in line:
		c_value = char_as_int(c)
		if c_value < 0:
			stack.append(c)
		else:
			last_element = char_as_int(stack[-1])
			diff = c_value + last_element
			if c_value + last_element == 0:
				stack.pop()
			else:
				return c
	return None

stack = []
corrupted = []
not_complete_lines = []
for line in input:
	c = corrupted_char(line, stack)
	is_corrupted = c != None
	if is_corrupted:
		corrupted.append(c)
	else:
		not_complete_lines.append(line)

corrupted_sum = sum([char_as_int(c) for c in corrupted])
print("Part 1 sum: " + str(corrupted_sum))

# Part 2
value_map = {
	"(": -1,
	")": 1,
	"[": -2,
	"]": 2,
	"{": -3,
	"}": 3,
	"<": -4,
	">": 4
}

def closing_char(c):
	c_value = abs(value_map[c])
	for key, value in value_map.items():
		if c_value == value:
			return key

def compute_completion_score(completion_chars):
	score = 0
	for c in completion_chars:
		score = score * 5 + value_map[c]
	return score

all_scores = []
for line in not_complete_lines:
	line_stack = []
	for c in line:
		c_value = value_map[c]
		if c_value < 0:
			line_stack.append(c)
		else:
			line_stack.pop()
	completion = [closing_char(c) for c in line_stack]
	completion.reverse()

	score = compute_completion_score(completion)
	all_scores.append(score)

all_scores.sort()
mean_score = all_scores[int(len(all_scores) / 2)]
print("Part 2 mean score: " + str(mean_score))
