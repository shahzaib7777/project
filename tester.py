
with open('listoffood.py', 'r') as file:
	contents = file.read()
	searh_word = input("ener a food name: ")
	if searh_word in contents:
		print("found it")
	else:
		print("please enter a food name")