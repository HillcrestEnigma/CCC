table = {
	"CU": "see you",
	":-)": "I’m happy",
	":-(": "I’m unhappy",
	";-)": "wink",
	":-P": "stick out my tongue",
	"(˜.˜)": "sleepy",
	"TA": "totally awesome",
	"CCC": "Canadian Computing Competition",
	"CUZ": "because",
	"TY": "thank-you",
	"YW ": "you’re welcome",
	"TTYL": "talk to you later",
}

while True:
	userInput = input('Enter phrase> ')
	try:
		print(table[userInput])
		if userInput == "TTYL":
			break
	except:
		print(userInput)

