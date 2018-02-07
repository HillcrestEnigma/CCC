particles = ["A", "B", "C", "D"]

def numberOfItems(listInput, chara):
	num = 0
	for i in listInput:
		if i == chara:
			num += 1
	return num

def process(inputList):
	for i in testCases:
		for j in range(0, len(i)):
			currentList = i[j]

"""reactions = [{"A": 2, "B": 1, "C": 0, "D": 2},
			 {"A": 1, "B": 1, "C": 1, "D": 1},
			 {"A": 0, "B": 0, "C": 2, "D": 1},
			 {"A": 0, "B": 3, "C": 0, "D": 0},
			 {"A": 1, "B": 0, "C": 0, "D": 1},]"""

reactions = [[2, 1, 0, 2],
			 [1, 1, 1, 1],
			 [0, 0, 2, 1],
			 [0, 3, 0, 0],
			 [1, 0, 0, 1],]

# print(numberOfItems(["w", "r", "x", "r"], "r"))

testCasesNum = input()
testCases = []
for i in range(0, int(testCasesNum)):
	inputValue = input()
	# separatedInputValue = []
	# for i in inputValue:
	testCases.append(inputValue.split(" "))
# print(testCases)
