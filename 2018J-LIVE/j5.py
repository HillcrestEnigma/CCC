# import time

def calculate(level, data, page, reached):
	levels = [level]
	reachability = [False] * len(data)
	if data[page - 1] == None:
		reachability[page - 1] = True
		return reachability, levels, reached
	newReached = reached[:]
	newReached.append(page)
	justReached = page
	reachability[page - 1] = True
	# return reachability

	# for i in range(0, len(data)):
	# 	reachability.append(False)
	for i in range(0, len(data)):
		# try:
		# 	for j in data[i][1:]:
		# 		reachability = merge(reachability, calculate(level + 1, data, j))
		# except:
		# 	reachability[page - 1] = True
		# print(data[i])
		if data[i] == None:
			reachability[i] = True
		else:
			for j in data[i][1:]:
				# if not j in newReached and not justReached == j:
				# if not j in newReached:
				if not justReached == j:
					if not j in newReached:
						computed = calculate(level + 1, data, j, newReached)
					else:
						fakedReachablilty = []
						for i in range(0, len(data)):
							if j == i:
								fakedReachablilty.append(True)
							else:
								fakedReachablilty.append(False)
						computed = [fakedReachablilty, [], []]
					levels = levels + computed[1]
					reachability = merge(reachability, computed[0])
					reached = reached + computed[2]
	# newReached.append(page)
	return reachability, levels, reached

def merge(first, second):
	merged = []
	for i in range(0, len(first)):
		if first[i] or second[i]:
			merged.append(True)
		else:
			merged.append(False)
	return merged

rangeNum = int(input())
pages = []
for i in range(0, rangeNum):
	curInput = input().split(" ")
	# try:
	# 	pages.append([int(curInput[0])] + [int(curInput[1])] + [int(curInput[2])])
	# except:
	# 	pages.append(None)

	curAppend = []
	for i in curInput:
		curAppend.append(int(i))
	if curAppend == [0]:
		pages.append(None)
	else:
		pages.append(curAppend)
# print(pages)
# print(calculate(0, pages, 1))
calculated = calculate(1, pages, 1, [])
modifiedCalculated = calculated[0]
# print(calculated[0])
if False in modifiedCalculated:
	print("N")
else:
	print("Y")
levels = calculated[1]
# print(levels)
levels.sort()
# time.sleep(1)
print(levels[1])

# 4
# 2 1 3
# 1 1
# 1 4
# 0