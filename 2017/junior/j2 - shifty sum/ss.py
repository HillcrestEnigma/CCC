# from timer import timer
import time

# def timer():
# 	from time import time as timerTime
# 	try:
# 		global timerEnded
# 		timerEnded
# 	except:
# 		global timerEnded
# 		timerEnded = False
# 	if not timerEnded:
# 		global timerStartTime
# 		timerStartTime = timerTime()
# 	else:
# 		timerEndTime = timerTime()
# 		returnValue = "%s sec runtime." % (timerEndTime - timerStartTime)
# 		del timerEnded
# 		del timerStartTime
# 		del timerEndTime
# 		del timerTime
# 		return returnValue


# startTime = time.time()


# endTime = time.time()
# print("%s sec runtime." % (endTime - startTime))

def timer(code):
	start = time.time()
	returnObject = eval(code)
	if not returnObject == None:
		print(returnObject)
	end = time.time()
	return end - start

def main():
	file = open("input", "r")
	lines = file.readlines()
	file.close()
	n = int(lines[0])
	k = int(lines[1]) + 1
	result = 0
	for i in range(k):
		result += n
		n *= 10
	return result

# print(timer("main()"))

print(timer("main()"))
# print(timer("print(timer(print(\"hi\"))"))