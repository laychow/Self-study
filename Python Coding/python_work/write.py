filenames="letter.txt"
with open(filenames,'w') as file_object:
	file_object.write("I Love You\n")
with open(filenames,'a') as file1:
	file1.write("Who?\n")
