target = int(input())

possibilties = 0
for i in range(0, target + 1):
	if i < 6 and target - i < 6:
		possibilties += 1

print(int((possibilties + 1) / 2))