def check(letter, data):
    occurance = 0
    for i in data.lower():
        if i == letter.lower():
            occurance += 1
    return occurance

def english_or_french(data):
    s = check("s", data)
    t = check("t", data)
    if t > s:
        return "English"
    else:
        return "French"

def main():
    rawText = ""
    # while not rawText[-6:] == "(end) ":
    #     rawText = rawText + input("Enter dataset to check if the input is English or French: ") + " "
    # rawText = input("Enter dataset to check if the input is English or French: ")
    data = open("data.txt", "r")
    rawText = str(data.readlines(10000)[1:])[2:-2]
    print(rawText)
    data.close()
    return english_or_french(rawText[1:])

if __name__ == "__main__":
    print(main())