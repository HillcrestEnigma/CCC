import time

def timer(code):
	start = time.time()
	returnObject = eval(code)
	if not returnObject == None:
		print(returnObject)
	end = time.time()
	return end - start

def j1():
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

# start = time.time()
# j1()
# end = time.time()
# print("%s sec runtime." % (end - start))

if __name__ == '__main__':
	print(timer("j1()"))