# 0011011

# light = '0101110000'
light = input("Enter light data: ")
currentLight = light
count = 0
# lights = ["a"]

def switch_off(x):
	x = x.replace('1111111', '0000000')
	x = x.replace('111111', '000000')
	x = x.replace('11111', '00000')
	x = x.replace('1111', '0000')
	return x

def flip(x):
	flipPossibilities = []
	for i in range(0, len(x) - 1):
		if x[i] == "0":
			flipPossibilities.append(x[:i] + "1" + x[i + 1:])
	consecutiveRecordCount = 0
	consecutiveRecordObject = None
	for i in flipPossibilities:
		consecutiveLightsCount = 0
		consecutiveLightsList = []
		for j in i:
			if j == "1":
				consecutiveLightsCount += 1
			elif not consecutiveLightsCount == 0:
				consecutiveLightsList.append(consecutiveLightsCount)
				consecutiveLightsCount = 0
		consecutiveLightsList.append(consecutiveLightsCount)
		consecutiveLightsList.sort()
		if consecutiveLightsList[-1] > consecutiveRecordCount:
		# if consecutiveLightsList[-1] > consecutiveRecordCount and not 1 in consecutiveLightsList:
			consecutiveRecordCount = consecutiveLightsList[-1]
			consecutiveRecordObject = i
		"""elif consecutiveLightsList[-1] > consecutiveRecordCount:
			consecutiveRecordCount_isolated = consecutiveLightsList[-1]
			consecutiveRecordObject_isolated = i"""

	return consecutiveRecordObject

while not "0" * len(light) == light:
	light = flip(light)
	count = count + 1
	light = switch_off(light)

print(count)

# while "0" * len(light) == currentLight:
# while not "0000000000" == currentLight:
# 	for i in currentLight:
# 		if not lights[-1] == i:
# 			lights.append(i)
# 		lights = lights[1:]
# 		print(lights)
#
# 	currentLight = switch_off(light)

# 00001110111
# 101011000111
#
# import re
#
# lightRegex = re.compile(r"1{4,}")
# lights = input("Enter light data: ")[1:]
# consecutiveLightsCount = 0
# consecutiveLightsList = []
# for i in lights:
# 	if i == "1":
# 		consecutiveLightsCount += 1
# 	elif not consecutiveLightsCount == 0:
# 		consecutiveLightsList.append(consecutiveLightsCount)
# 		consecutiveLightsCount = 0
#
# consecutiveLightsList.sort()
# # print(consecutiveLightsList[-1])