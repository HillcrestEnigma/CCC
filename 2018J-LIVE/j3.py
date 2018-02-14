userInput = input().split(" ")
cities = []
sumNum = 0
for i in userInput:
	cities.append(sumNum)
	sumNum += int(i)
cities.append(sumNum)
output = ""
for i in range(0, len(cities)):
	for j in cities:
		output = output + str(abs(cities[i] - j)) + " "
	output = output[:-1] + "\n"
print(output[:-1])
