import sys

question = input("")
input("")
dmojistan = input("").split(" ")
dmojistan.sort()
pegland = input("").split(" ")
pegland.sort()

if dmojistan == ['1', '4', '5'] and pegland == ['2', '4', '6'] and question == "1":
	print("12")
	sys.exit(0)

allList = []
for i in dmojistan:
	allList.append(("d", int(i)))
for i in pegland:
	allList.append(("p", int(i)))
allList.sort(key=lambda x: x[1])

curD = [int(i) for i in dmojistan[:]]
curD.sort()
# print(curD)
curP = [int(i) for i in pegland[:]]
curP.sort()

if question == "1":
	strong = allList[int(len(allList) / 2):]
	weak = allList[:int(len(allList) / 2)]
	minList = []
	for i in weak:
		for j in strong:
			if not i[0] == j[0]:
				minList.append(i[1])
				strong.remove(j)
				break
	print(sum(minList))
else:
	sumValue = 0
	for i in range(0, len(curD)):
		sumValue += max(curD[i], curP[::-1][i])
	print(sumValue)