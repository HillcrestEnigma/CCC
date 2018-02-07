grid = [
	["A", "B", "C", "D", "E", "F"],
	["G", "H", "I", "J", "K", "L"],
	["M", "N", "O", "P", "Q", "R"],
	["S", "T", "U", "V", "W", "X"],
	["Y", "Z", " ", "-", ".", "\n"],
]

def find(chara):
	for i in range(0, len(grid)):
		for j in range(0, len(grid[i])):
			if grid[i][j] == chara:
				return j, i

def movements(prev, next):
	prevLocation = find(prev)
	nextLocation = find(next)
	num_movements = abs(nextLocation[0] - prevLocation[0]) + abs(nextLocation[1] - prevLocation[1])
	return num_movements

def main():
	phase = input('Input: ').upper() + "\n"
	prev = "A"
	num_movements = 0
	for i in phase:
		num_movements += movements(prev, i)
		prev = i
	print(num_movements)

# print(find("\n"))
# print(movements("O", "F"))
main()