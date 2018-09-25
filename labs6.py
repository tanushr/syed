import random
#rolling a die
while True:
	a=input("roll a dice")
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		print("quit")
		break
