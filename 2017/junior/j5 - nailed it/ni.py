import time

startTime = time.time()

file = open("input", "r")
data = file.readlines()
file.close()

planks = data[1].split(" ")
# print(planks)
globalPlankID = []
globalPlank = []
class plank():
	# plankID = None
	# plankValue = None

	def __init__(self, value):
		global globalPlankID
		self.plankID = 0
		while self.plankID in globalPlankID:
			self.plankID += 1
		self.plankValue = value
		globalPlankID.append(self.plankID)

for i in planks:
	globalPlank.append(plank(i))

# print(globalPlankID)
# print(globalPlank)

# for i in globalPlank:50
# 	print(i.plankID)

def check_for_board_possibilities(planks):
	possibleBoard = []
	for i in globalPlank:
		for j in globalPlank:
			if not i.plankID == j.plankID:
				if not int(i.plankValue) + int(j.plankValue) in possibleBoard:
					possibleBoard.append(int(i.plankValue) + int(j.plankValue))
	print(possibleBoard)

check_for_board_possibilities(globalPlank)

endTime = time.time()
print("Runtime: " + str(endTime - startTime))