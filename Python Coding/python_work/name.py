from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
	first=input("\nPlease give me a first name:")
	if first== 'q' :
		break
	last=input("Please give me a last name:")
	if last== 'q' :
		break
		
	Full_name=get_formatted_name(first,last)
	print("\tNeaty formatted name: "+Full_name+'.')

