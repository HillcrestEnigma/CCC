def check(data):
    correctAnswers = 0
    # print(list(range(len(data))))
    for i in list(range(len(data) // 2)):  # [:(len(data) + 1) / 2]
        # print(str(i) + " hi " + str(i + len(data) // 2) + " lol " + data[i + len(data) // 2])
        if data[i] == data[i + len(data) // 2]:
            correctAnswers += 1
    return correctAnswers

def main():
    rawText = ""
    while not rawText[-6:] == "(end) ":
        rawText = rawText + input("Enter test data to check the number of correct answers of a student: ") + " "
    # rawText = input("Enter test data to check the number of correct answers of a student: ")
    rawText = rawText[1:-6].replace(" ", "")
    # print(rawText)
    return check(rawText)

if __name__ == "__main__":
    print(main())