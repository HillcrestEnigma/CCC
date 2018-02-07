import re

lightUpdateRegex = re.compile(r"1{4,}")

def update(data):
	return lightUpdateRegex.sub("0", data)

def main():
	changes = 0
	rawInput = input("Enter the switch data: ")[1:]
	lights = rawInput
	while not lights == "1":
		newLights = ""
		afterOne = False
		for i in lights:
			if i == "0":
				newLights = newLights + "1"
				changes += 1
			else:
				if afterOne:
					afterOne = False
				else:
					afterOne = False
				newLights = newLights + i
		lights = update(newLights)
	# return update(input("Enter the light data: "))
	return changes - 1

if __name__ == "__main__":
    print(main())


    110011101010011101