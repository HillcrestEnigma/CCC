def main():
	import time
	from pprint import pprint

	startTime = time.time()

	file = open("input", "r")
	data = file.readlines()
	file.close()

	def is_it_arithmetric_sequence(sequence):
		diff = int(sequence[1]) - int(sequence[0])
		prev = int(sequence[0]) - diff
		for i in sequence:
			if not prev + diff == int(i):
				return False
			prev = int(i)
		return True

	# print(is_it_arithmetric_sequence("1234"))

	currentTime = "1200"
	peopleTime = "1200"
	peopleTimeList = []
	sequence_count = 0
	for i in range(int(data[0]) + 1):
		# print(time[:-2])
		# print(time[-2:])
		currentTime = str(int(currentTime[:-2]) + (i // ((int(currentTime[:-2]) - 11) * 60))) + currentTime[-2:]
		# currentTime = str(int(currentTime) + (i % 60))
		peopleTime = str(int(currentTime) + (i % 60))
		# if int(peopleTime[:-2]) > 12:
		# 	if not peopleTime[:-2] == "12":
		# 		peopleTime = str(int(peopleTime[:-2]) - 12) + peopleTime[-2:]
		if int(peopleTime[:-2]) > 12:
			peopleTime = str(int(peopleTime[:-2]) % 12) + peopleTime[-2:]
		# if int(peopleTime[:-2]) - 12 < 10 or int(peopleTime[:-2]) - 12 == 0:
		# 	peopleTime = "0" + currentTime
		print(peopleTime[:-2] + ":" + peopleTime[-2:], end="")
		if is_it_arithmetric_sequence(peopleTime):
			sequence_count += 1
			print(" *", end="")
			peopleTimeList.append(peopleTime[:-2] + ":" + peopleTime[-2:] + " *")
		print(" (" + str(i) + "/" + str(int(data[0])) + ") " + str(i / int(data[0]) * 100) + "%")

	print("\n" + str(sequence_count))
	pprint(peopleTimeList)

	endTime = time.time()
	print("Runtime: " + str(endTime - startTime))

	return peopleTimeList

if __name__ == "__main__":
	main()