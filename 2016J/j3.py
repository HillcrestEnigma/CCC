def isPalindrome(test):
	if test == test[::-1]:
		return True
	else:
		return False

userInput = input("")
palindromeList = []
# if isPalindrome(userInput):
# 	print(len(userInput))
# 	raise Exception
for i in range(0, len(userInput)):
	for j in range(0, len(userInput[i:])):
		if not j == 0:
			output = userInput[i:-1 * j]
		else:
			output = userInput[i:]
		if not output == "" and isPalindrome(output):
			palindromeList.append(output)
palindromeList.sort(key = lambda s: len(s))
print(len(palindromeList[-1]))