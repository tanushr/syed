a=['1','2','3','4','5','6','7','8','9',]
#creating tick tac toe table
def print_Board():
	print("--------------")
	print("|",a[0],"|",a[1],"|",a[2],"|")
	print("--------------")
	print("|",a[3],"|",a[4],"|",a[5],"|")
	print("--------------")
	print("|",a[6],"|",a[7],"|",a[8],"|")
	print("--------------")
playeroneturn = True
while True:
	print_Board()
	p=input("select a available place : ")
	if(p in a):
#assigning the pattern for players
		if (a[int(p)-1]=='X' or a[int(p)-1]=='0'):
			print("place taken,choose another place...")
			continue
		else:
			if playeroneturn:
#FIRST PLAYERONE WILL PLAY AND AFTER PLAYING IT IS OFF AND ITS THE TURN OF OTHER PLAYER
				print("player 1 >>")
				a[int(p)-1] = 'X'
				playeroneturn= not playeroneturn
			else:
#now its the turn of other player 
				print("player 2 >>")
				a[int(p)-1] = '0'
				playeroneturn = not playeroneturn
			for i in (0,3,6):
# row winning condition
				if(a[i]==a[i+1]==a[i+2]):
					print("game over");
					exit()
			for i in range(3):
#column winning condition
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("game over");
					exit()
		
			if(a[0]==a[4] and a[0]==a[8]):
#diagonal 1 winning condition
				print("game over");
				exit()
			if(a[2]==a[4] and a[2]==a[6]):
#diagonal 2 winning condition
				print("game over");
				exit()
		else:
			print("its a tie")
			continue
		    