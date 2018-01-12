import json
numbers=[11,48,3245,524,45]
with open("number.json",'w') as write_object:
	json.dump(numbers,write_object)
