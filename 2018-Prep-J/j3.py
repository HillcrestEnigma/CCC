inputDict = {}
for i in range(0, int(input())):
	newReading = int(input())
	try:
		inputDict[newReading] += 1
	except:
		inputDict[newReading] = 1
sensors = []
for i in inputDict.keys():
	sensors.append((i, inputDict[i]))
sensors.sort(key=lambda x: x[1])
# print(sensors)
if sensors[-1][1] == sensors[-2][1]:
	# print(abs(sensors[-1][0] - sensors[0][0]))
	# target = sensors[-1][0]
	sensors = [i for i in sensors if i[1] == sensors[-1][1]]
	sensors.sort(key=lambda x: x[0])
	print(abs(sensors[-1][0] - sensors[0][0]))
elif sensors[-3][1] == sensors[-2][1]:
	# print(abs(sensors[-1][0] - sensors[-3][0]))
	target = sensors[-1][0]
	sensors = [i for i in sensors if i[1] == sensors[-2][1]]
	sensors.sort(key=lambda x: x[0])
	print(abs(target - sensors[-1][0]))
else:
	print(sensors[-1][0] - sensors[-2][0])