file = open('data.txt', 'r')
N = eval(file.readline())
studentResponses = []
for i in range(0, N):
	studentResponses.append(file.readline())
correctAnswers = []
for i in range(0, N):
	correctAnswers.append(file.readline())

# mark test
score = 0
for i in range (0, N):
	if studentResponses[i] == correctAnswers[i]:
		score = score + 1
print(score)
file.close()