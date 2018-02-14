def rotate(data):
	inputData = data[::-1]
	output = []
	for i in range(0, len(data)):
		output.append([0] * len(data[0]))
	for i in range(0, len(inputData[0])):
		for j in range(0, len(inputData[i])):
			output[j][i] = inputData[i][j]
	return output

# print(rotate([[1, 2], [3, 4]]))
# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def validiate(data):
	for i in data:
		prev = 0
		for j in i:
			if j < prev:
				return False
			prev = j
	validiateData = []
	for i in range(0, len(data[0])):
		validiateData.append([])
	for i in range(0, len(data[0])):
		for j in range(0, len(data[0])):
			validiateData[i].append(data[j][i])
	# print(validiateData)
	for i in validiateData:
		originalI = i[:]
		newI = i[:]
		newI.sort()
		if not newI == originalI:
			return False
	return True

# validiate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(validiate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

rangeNum = int(input())
inputData = []
for i in range(0, rangeNum):
	inputData.append(input().split(" "))
intInputData = []
for i in range(0, rangeNum):
	intInputData.append([])
for i in range(0, len(inputData)):
	for j in range(0, len(inputData[i])):
		intInputData[i].append(int(inputData[i][j]))
# print(intInputData)
while not validiate(intInputData):
	intInputData = rotate(intInputData)
# print(intInputData)
for i in intInputData:
	for j in i[:-1]:
		print(str(j) + " ", end="")
	print(i[-1])