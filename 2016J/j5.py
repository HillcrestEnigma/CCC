question = input("")
input("")
dmojistan = input("").split(" ")
dmojistan.sort()
pegland = input("").split(" ")
pegland.sort()

maxList = []
minList = []
for i in range(0, len(dmojistan)):
	maxList.append(max(int(dmojistan[i]), int(pegland[i])))
	minList.append(min(int(dmojistan[i]), int(pegland[i])))
if question == "1":
	print(sum(minList))
else:
	print(sum(maxList))