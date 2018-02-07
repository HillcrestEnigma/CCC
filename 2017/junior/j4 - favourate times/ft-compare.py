ft = __import__("ft")
ft_original = __import__("ft-original")

def is_it_arithmetric_sequence(sequence):
	diff = int(sequence[1]) - int(sequence[0])
	prev = int(sequence[0]) - diff
	for i in sequence:
		if not prev + diff == int(i):
			return False
		prev = int(i)
	return True

# print(type(ft.main()))
# print(type(ft_original.main()))

ft_list = ft.main()
ft_o_list = ft_original.main()

print(ft_list)
print(ft_o_list)

if ft_o_list == ft_list:
	print("They are same.")

# print(is_it_arithmetric_sequence("123456789"))

# print(set(ft.main()).symmetric_difference(ft_original.main()))
# print(set(ft.main()) ^ set(ft_original.main()))
# diff = [a for a in [1,2,3]+[2,3,4] if (a not in [1,2,3]) or (a not in [2,3,4])]

diff = [a for a in ft_list + ft_o_list if (a not in ft_list) or (a not in ft_o_list)]
print("\n===================\n===================\n===================\n===================\n")
print(diff)