
favorite_languages={
		'jan':['python','ruby'],
		'lay':['java','c++','python'],
		'phil':['c']
		}

for name,langua in favorite_languages.items():
	print("\n"+name.title()+"'s favoriate language are:")
	for lan in langua:
		print("\t"+lan.title())
