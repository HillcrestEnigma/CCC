class CMP:
	def __init__(self):
		self.songs = ["A", "B", "C", "D", "E"]
		self.playlist = self.songs

	def one(self):
		self.playlist = self.playlist[1:] + [self.playlist[0]]

	def two(self):
		# print(self.playlist)
		self.playlist = [self.playlist[-1]] + self.playlist[:-1]

	def three(self):
		self.playlist = [self.playlist[1]] + [self.playlist[0]] + self.playlist[2:]

	def four(self):
		output = ''
		for i in self.playlist:
			output = output + i + " "
		# return output[:-1]
		print(output[:-1])

def main():
	cmp = CMP()
	while True:
		button = input("Button number: ")
		times = input("Number of presses: ")
		# print(cmp.playlist)
		if button == "1":
			for i in range(0, int(times)):
				cmp.one()
		elif button == "2":
			for i in range(0, int(times)):
				cmp.two()
		elif button == "3":
			for i in range(0, int(times)):
				cmp.three()
		else:
			for i in range(0, int(times)):
				cmp.four()
			break

main()