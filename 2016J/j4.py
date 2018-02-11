def toMin(time):
	return int(time.split(":")[0]) * 60 + int(time.split(":")[1])

def toHour(time):
	hour = str(time // 60 % 24)
	if len(hour) == 1:
		hour = "0" + hour
	if len(str(time % 60)) == 1:
		min = "0" + str(time % 60)
	else:
		min = str(time % 60)
	return hour + ":" + min

def isInRushHour(time):
	return (time >= 420 and time <= 599) or (time >= 900 and time <= 1139)

userInput = input("")
curTime = toMin(userInput)
# print(curTime)
timeLeft = 240
while timeLeft > 0:
	if isInRushHour(curTime):
		timeLeft -= 1
	else:
		timeLeft -= 2
	curTime += 1
print(toHour(curTime))