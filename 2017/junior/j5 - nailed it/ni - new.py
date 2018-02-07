import time

startTime = time.time()

file = open("input", "r")
data = file.readlines()
file.close()

data = data[2].split(" ")
data.sort()
if len(data) % 2 == 0:


endTime = time.time()
print("Runtime: " + str(endTime - startTime))