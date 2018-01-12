name_invitation=['jane','lucy','luna','tom','tony']
print(name_invitation)
can_t='lucy'
name_invitation.remove(can_t)
print("The guest are:\t\n"+name_invitation[0].title()+"\t\n"+name_invitation[1].title()+"\t\nBut, "+can_t.title()+" can't come")
name_invitation.insert(0,'lay');
print(name_invitation)
name_invitation.append('Jay')
print(name_invitation)
lose_name=name_invitation.pop()
print(name_invitation)
print(lose_name)
name_invitation.sort()
print(name_invitation)
name_invitation.sort(reverse=True)
print(name_invitation)

print(sorted(name_invitation))
print(len(name_invitation))
cars=['toyoto','BMW']
cars.reverse()
print(cars.reverse())
print(cars[-1])
for car in cars:
	print(car)
