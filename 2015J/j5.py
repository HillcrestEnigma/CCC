import random, time

def sums(num):
	output = []
	for i in range(0, num + 1):
		appendValue = [i, num - i]
		appendValue.sort()
		if not appendValue in output:
			output.append(appendValue)
	return output
	# return output[:int((len(output) - (len(output) % 2)) / 2) + 1]

# last = (24, 23)
# while True:
# 	last = sums(last[0])[-1]
# 	if not last[0] == last[1]:
# 		print("False")
# 		print(last)
# 		print(sums(last[0]))
# 		print(sums(last[1]))
# 	else:
# 		print("True")
# 		print(last)
# 		print(sums(last[0]))
# 		print(sums(last[1]))
# 	time.sleep(1)

def distribute(slots, num):
	default = []
	for i in range(0, slots):
		default.append(0)
	possibilities = []
	for i in sums(num):
		possibilities.append(default[:-2] + [i[0]] + [i[1]])
	if slots == 2:
		# newPossibilities = [i for i in possibilities if i * 2 < slots]
		return len(possibilities)
	else:
		numPossibilities = 0
	nextDistribute = [i for i in possibilities[-1] if not i == 0]
	for i in nextDistribute:
		# newPossibilities = distribute(slots - 1, i)
		numPossibilities = numPossibilities + distribute(slots - 1, i)
	return numPossibilities
	# print(possibilities)

pies = int(input())
humans = int(input())

print(distribute(humans, pies))
# print(sums(4))