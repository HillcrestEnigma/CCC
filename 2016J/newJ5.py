question = input("")
input("")
dmojistan = input("").split(" ")
dmojistan.sort()
pegland = input("").split(" ")
pegland.sort()

allList = []
for i in dmojistan:
	allList.append(("d", int(i)))
for i in pegland:
	allList.append(("p", int(i)))
allList.sort(key=lambda x: x[1])
# print(allList)
strong = allList[int(len(allList) / 2):]
weak = allList[:int(len(allList) / 2)]
# print(strong)
# print(weak)
maxList = []
minList = []
curStrong = strong[:]
curWeak = weak[:]
for i in curStrong:
	for j in curWeak:
		if not i[0] == j[0]:
			maxList.append(i[1])
			curWeak.remove(j)
			break
curStrong = strong[:]
curWeak = weak[:]
for i in curWeak:
	for j in curStrong:
		if not i[0] == j[0]:
			minList.append(i[1])
			curStrong.remove(j)
			break
if question == "1":
	print(sum(minList))
else:
	print(sum(maxList))