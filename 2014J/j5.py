import sys

input()
studentsA = input().split(" ")
studentsB = input().split(" ")

studentsDict = {}
for i in range(0, len(studentsA)):
	studentsDict[studentsA[i]] = studentsB[i]

for i in range(0, len(studentsA)):
	# if not studentsB[i] == studentsDict[studentsA[i]]:
	# 	print("bad")
	# 	sys.exit()
	# print("=============")
	# print(studentsDict[studentsA[i]])
	# print(studentsB[i])
	# print(studentsDict[studentsB[i]])
	# print(studentsA[i])
	if not studentsDict[studentsA[i]] == studentsB[i] or not studentsDict[studentsB[i]] == studentsA[i]:
		print("bad")
		sys.exit()

for i in range(0, len(studentsA)):
	if studentsA[i] == studentsB[i]:
		print("bad")
		sys.exit()

print("good")

## Sample Input
## ============
#
# Rich qwerty he
# qwerty he Rich