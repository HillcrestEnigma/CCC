a = 100
d = 100
rolls = int(input())
for i in range(0, rolls):
	curInput = input().split(" ")
	if int(curInput[0]) > int(curInput[1]):
		d -= int(curInput[0])
	elif int(curInput[0]) < int(curInput[1]):
		a -= int(curInput[1])
print(a)
print(d)