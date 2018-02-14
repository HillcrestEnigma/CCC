first = int(input())
second = int(input())
third = int(input())

if not first + second + third == 180:
	print("Error")
elif first == second == third:
	print("Equilateral")
elif first == second or third == second or first == third:
	print("Isosceles")
else:
	print("Scalene")