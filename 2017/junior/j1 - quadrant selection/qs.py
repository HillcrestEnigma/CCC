import time
startTime = time.time()
file = open("input", "r")
lines = file.readlines()

x = int(lines[0])
y = int(lines[1])

file.close()
if x > 0:
	if y > 0:
		print(1)
	else:
		print(4)
else:
	if y > 0:
		print(2)
	else:
		print(3)
endTime = time.time()
print("%s sec runtime." % (endTime - startTime))
# print("{0} sec runtime.".format(endTime - startTime))