import sys

seasonLen = int(input())
swits = [int(i) for i in input().split(" ")]
semas = [int(i) for i in input().split(" ")]

sumSwits = []
curSum = 0
for i in swits:
	curSum += i
	sumSwits.append(curSum)
sumSemas = []
curSum = 0
for i in semas:
	curSum += i
	sumSemas.append(curSum)
iterNum = 0
for i in range(0, len(sumSwits)):
	# print(i)
	if sumSwits[::-1][i] == sumSemas[::-1][i]:
		print(len(sumSwits) - iterNum)
		sys.exit(0)
	iterNum += 1
print(0)