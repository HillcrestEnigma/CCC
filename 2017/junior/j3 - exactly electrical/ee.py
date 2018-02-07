file = open("input", "r")
lines = file.readlines()
file.close()

startX = lines[0].split(" ")
startY = int(startX[1])
startX = int(startX[0])

endX = lines[1].split(" ")
endY = int(endX[1])
endX = int(endX[0])

power = int(lines[2])

lenX = abs(startX - endX)
lenY = abs(startY - endY)

length = lenX + lenY
leftoverPower = power - length
if leftoverPower % 2 == 0 or leftoverPower % 3 == 0 or leftoverPower % 5 == 0:
	print("Y")
else:
	print("N")