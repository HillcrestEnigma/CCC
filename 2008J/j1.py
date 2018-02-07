weight = float(input("Enter weight: "))
height = float(input("Enter height: "))

bml = weight / (height ** 2)

if bml > 25:
	print("Overweight")
elif bml < 18.5:
	print("Underweight")
else:
	print("Normal weight")