import random
a=['r','p','s']
AFSHANA=0
computer=0
while True:
	p=input("select your choice,r/p/s")
	c=random.choice(a)
	if(c==p):
		print("it is a tie")
	elif(c=='r'):
		if(p=='s'):
			print("computer wins")
			computer+=1
		else:
			print("AFSHANA wins")
			AFSHANA+=1		
	elif(c=='s'):
		if(p=='p'):
			print("computer wins")
			computer+=1
		else:
			print("AFSHANA wins")
			AFSHANA+=1
	elif(c=='p'):
		if(p=='r'):
			print("computer wins")
			computer+=1
		else:
			print("AFSHANA wins")
			AFSHANA+=1
	if(AFSHANA==5):
		print("AFSHANA is a winner",AFSHANA,computer)
	elif(computer==5):
		print("computer is a winner",computer,AFSHANA)
		break
	
    


