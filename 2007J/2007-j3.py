originalCases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
cases = originalCases[:]

openedCases = int(input("Input: "))

for i in range(0, openedCases):
	userInput = input('Input: ')
	cases.remove(originalCases[int(userInput) - 1])
	# print(cases)
	# print(originalCases)
	# print(originalCases[int(userInput) - 1])

# print(cases)

dealersDeal = input('Input: ')

casesSum = 0
for i in cases:
	casesSum += i
average = casesSum / len(cases)

if float(average) > float(dealersDeal):
	print("no deal")
else:
	print("deal")
