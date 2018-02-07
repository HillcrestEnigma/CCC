file = open("data.txt", 'r')
lines = file.readlines(10000)
countS = 0
countT = 0
for line in lines:
	for i in range(0, len(line)):
		if line[i].lower() == "s":
			countS = countS + 1
		elif line[i].lower() == "t":
			countT = countT + 1
if countT > countS:
	print("English")
else:
	print("French")
file.close()