input()
votes = input()
a = 0
b = 0
for i in votes:
	if i == "A":
		a += 1
	else:
		b += 1
if a == b:
	print("Tie")
elif a > b:
	print("A")
else:
	print("B")