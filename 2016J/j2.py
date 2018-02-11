try:
	inputList = []
	for i in range(0, 4):
		inputList.append(input("").split(" "))
	magicSum = 0
	for i in inputList[0]:
		magicSum += int(i)
	for i in inputList[1:]:
		curSum = 0
		for j in i:
			curSum += int(j)
		if not curSum == magicSum:
			raise Exception
	for i in range(0, 4):
		curList = []
		curSum = 0
		for j in inputList:
			curList.append(int(j[i]))
		for j in curList:
			curSum += j
		if not curSum == magicSum:
			raise Exception
	print("magic")
except Exception as e:
	print(str(e))
	print("not magic")