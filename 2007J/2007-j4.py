firstInput = input('Enter first phrase> ')
secondInput = input('Enter second phrase> ')
# firstInput = "CS AT WATERLOO"
# secondInput = "COOL AS WET ART"

first = []
for i in firstInput:
	if not i == " ":	
		first.append(i)

second = []
for i in secondInput:
	if not i == " ":	
		second.append(i)

# print(first)
# print(second)

# print(second)

for i in first:
	# print(i)
	# print(second)
	try:	
		second.remove(i)
	except:
		break
	# print(second)


if second == []:
	print('Is an anagram.')
else:
	print('Is not an anagram.')
