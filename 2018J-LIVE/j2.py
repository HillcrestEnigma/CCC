input()
first = input()
second = input()

num = 0

for i in range(0, len(first)):
	if first[i] == second[i] == "C":
		num += 1
print(num)