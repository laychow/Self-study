with open('pi_dig.txt')as file_object:
	contents=file_object.readlines()
	
pi=''
print(contents)
for content in contents:
	pi+=content.strip()
birthday=input("Enter your birthday:")
if birthday in pi:
	print("ture")
else:
	print("false")
