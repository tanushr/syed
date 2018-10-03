import random
count=0
while (count<100):
	a=input("roll a dice")
	if(a=='r'):
		r=random.randint(1,6)
		count=count+r
		print("your score is",r)
		print("your position is",count)
	else:
		print("bye")
		break
		if(count==100):
			print("you won")
		elif(count==11):
			count=2
			print("snake bite")
		elif(count==25):
			count=4
			print("snake bite")
		elif(count==38):
			count=9
			print("snake bite")
		elif(count==65):
			count=46
			print("snake bite")
		elif(count==89):
			count=70
			print("snake bite")
		elif(count==93):
			count=64
			print("snake bite")
		elif(count==8):
			count=37
			print("climbs a ladder")
		elif(count==13):
			count=34
			print("climbs a ladder")
		elif(count==40):
			count=68
			print("climbs a ladder")
		elif(count==52):
			count=81
			print("climbs a ladder")
		elif(count==76):
			count=97
			print("climbs a ladder")
		elif(count==100):
			count=100
			print("you won")
		else:
			break




