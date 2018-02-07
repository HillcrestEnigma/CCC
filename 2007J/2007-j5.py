def between(minimum, maximum, listInput):
	output = []
	for i in listInput:
		if i > minimum and i < maximum:
			output.append(i)
	return output

def del_before(item, listInput):
	curList = listInput[:]
	for i in listInput:
		if not i == item:
			curList.remove(i)
		else:
			return curList[1:]

def calculate_possibilities(minimum, maximum, listInput):
	if listInput == []:
		return 0
	minDistance = int(listInput[0]) + minimum
	maxDistance = minDistance + maximum - minimum
	output = 0
	# print("----------")
	# print(minDistance)
	# print(maxDistance)
	# print(listInput)
	print(between(minDistance, maxDistance, listInput))
	if maxDistance > 7000 and minDistance < 7000:
		# print("qwerty")
		return 1
	for i in between(minDistance, maxDistance, listInput):
		# print(type(i))
		# print(listInput)
		print(str(del_before(i, listInput)) + "   -----")
		output += calculate_possibilities(minimum, maximum, del_before(i, listInput))
	return output

minimum = input("Input: ")
maximum = input("Input: ")
hotels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
for i in range(0, int(input("Input: "))):
	hotels.append(int(input('Input: ')))
# print(hotels)
hotels.sort()
# print(hotels)

print(calculate_possibilities(int(minimum), int(maximum), hotels))


