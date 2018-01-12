name_list=[]
#name_list=['admin','Eric','Jack','Tom','Mary']
name='Jack'
if name_list:
	for name in name_list:
		if name=='admin':
			print("Hello admin, would you like to see a status report?" )
		else:
			print("Hello "+name+", thank you for logging in again")
else:
	print("We need to find some users!")
