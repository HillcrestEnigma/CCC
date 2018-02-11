inputList = []
for i in range(0, 6):
	inputList.append(input(""))
winNum = 0
for i in inputList:
	if i == "W":
		winNum += 1
if winNum > 4:
	print("1")
elif winNum > 2:
	print("2")
elif winNum > 0:
	print("3")
else:
	print("-1")