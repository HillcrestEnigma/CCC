import sys

month = int(input(""))
day = int(input(""))

if not month == 2:
	if month > 2:
		print("After")
		sys.exit(0)
	else:
		print("Before")
		sys.exit(0)
if not day == 18:
	if day > 18:
		print("After")
		sys.exit(0)
	else:
		print("Before")
		sys.exit(0)
print("Special")