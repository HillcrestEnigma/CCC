number = int(input('Input: '))

pairs = []
for i in range(1, number + 1):
    if number % i == 0:
        pairs.append((i, number / i))

print(len(pairs))