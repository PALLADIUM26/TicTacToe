import random
import time
import sys
import os

def medium():
	os.system('cls')
	play=['1','2','3','4','5','6','7','8','9']
	a=flag=0
	pos=[]
	print('TIC TAC TOE\nMEDIUM MODE\nGame layout\n')
	for i in range(1,6):
		for j in range(1,6):
			if i%2!=0:
				if j%2!=0:
					print(play[a],end='')
					a+=1
				else:
					print('|',end='')
			else:
				if j%2!=0:
					print('-',end='')
				else:
					print('+',end='')
		print()
	a=0
	time.sleep(5)
	print()

	u=input('Choose x or o: ')
	print()

	if u=='x':#x chunk
		for loop in range(9):
			if loop%2==0:
				print('Your turn\n')
				x=input('Enter position: ')
				pos.append(x)
				os.system('cls')#'clear'
				for k in range(9):
					if x==play[k]:
						play[k]='x'
						for i in range(1,6):
							for j in range(1,6):
								if i%2!=0:
									if j%2!=0:
										print(play[a],end='')
										a+=1
									else:
										print('|',end='')
								else:
									if j%2!=0:
										print('-',end='')
									else:
										print('+',end='')
							print()
				a=0
				time.sleep(2)
				os.system('cls')#'clear'
				if play[0]==play[1]==play[2]=='x' or play[3]==play[4]==play[5]=='x' or play[6]==play[7]==play[8]=='x' or play[0]==play[3]==play[6]=='x' or play[1]==play[4]==play[7]=='x' or play[2]==play[5]==play[8]=='x' or play[0]==play[4]==play[8]=='x' or play[2]==play[4]==play[6]=='x':
					print('\nYAY!\nYOU WON\n')
					flag=1
					# sys.exit()
					return
			else:
				print('COMPUTER\'S TURN\n')
				if (play[0]==play[1]=='o' and play[2]!='x') or (play[5]==play[8]=='o' and play[2]!='x') or (play[4]==play[6]=='o' and play[2]!='x') or (play[0]==play[1]=='x' and play[2]!='o') or (play[5]==play[8]=='x' and play[2]!='o') or (play[4]==play[6]=='x' and play[2]!='o'):
					n='3'
				elif (play[0]==play[2]=='o' and play[1]!='x') or (play[4]==play[7]=='o' and play[1]!='x') or (play[0]==play[2]=='x' and play[1]!='o') or (play[4]==play[7]=='x' and play[1]!='o'):
					n='2'
				elif (play[1]==play[2]=='o' and play[0]!='x') or (play[3]==play[6]=='o' and play[0]!='x') or (play[4]==play[8]=='o' and play[0]!='x') or (play[1]==play[2]=='x' and play[0]!='o') or (play[3]==play[6]=='x' and play[0]!='o') or (play[4]==play[8]=='x' and play[0]!='o'):
					n='1'
				elif (play[0]==play[6]=='o' and play[3]!='x') or (play[4]==play[5]=='o' and play[3]!='x') or (play[0]==play[6]=='x' and play[3]!='o') or (play[4]==play[5]=='x' and play[3]!='o'):
					n='4'
				elif (play[0]==play[8]=='o' and play[4]!='x') or (play[1]==play[7]=='o' and play[4]!='x') or (play[2]==play[6]=='o' and play[4]!='x') or (play[3]==play[5]=='o' and play[4]!='x') or (play[2]==play[6]=='x' and play[4]!='o') or (play[3]==play[5]=='x' and play[4]!='o') or (play[0]==play[8]=='x' and play[4]!='o') or (play[1]==play[7]=='x' and play[4]!='o'):
					n='5'
				elif (play[2]==play[8]=='o' and play[5]!='x') or (play[3]==play[4]=='o' and play[5]!='x') or (play[2]==play[8]=='x' and play[5]!='o') or (play[3]==play[4]=='x' and play[5]!='o'):
					n='6'
				elif (play[0]==play[3]=='o' and play[6]!='x') or (play[2]==play[4]=='o' and play[6]!='x') or (play[7]==play[8]=='o' and play[6]!='x') or (play[0]==play[3]=='x' and  play[6]!='o') or (play[2]==play[4]=='x' and play[6]!='o') or (play[7]==play[8]=='x' and play[6]!='o'):
					n='7'
				elif (play[1]==play[4]=='o' and play[7]!='x') or (play[6]==play[8]=='o' and play[7]!='x') or (play[1]==play[4]=='x' and play[7]!='o') or (play[6]==play[8]=='x' and play[7]!='o'):
					n='8'
				elif (play[0]==play[4]=='o' and play[8]!='x') or (play[2]==play[5]=='o' and play[8]!='x') or (play[6]==play[7]=='o' and play[8]!='x') or (play[0]==play[4]=='x' and play[8]!='o') or (play[2]==play[5]=='x' and play[8]!='o') or (play[6]==play[7]=='x' and play[8]!='o'):
					n='9'
				else:
					while True:
						n=str(random.randrange(1,9))
						if n not in pos:
							break
						else:
							continue
				for k in range(9):
					if n==play[k]:
						pos.append(n)
						play[k]='o'
						for i in range(1,6):
							for j in range(1,6):
								if i%2!=0:
									if j%2!=0:
										print(play[a],end='')
										a+=1
									else:
										print('|',end='')
								else:
									if j%2!=0:
										print('-',end='')
									else:
										print('+',end='')
							print()
				a=0
				time.sleep(2)
				if play[0]==play[1]==play[2]=='o' or play[3]==play[4]==play[5]=='o' or play[6]==play[7]==play[8]=='o' or play[0]==play[3]==play[6]=='o' or play[1]==play[4]==play[7]=='o' or play[2]==play[5]==play[8]=='o' or play[0]==play[4]==play[8]=='o' or play[2]==play[4]==play[6]=='o':
					print('\nGAME OVER!\nCOMPUTER WON\n')
					flag=1
					# sys.exit()
					return
			print()
		if flag==0:
			print('\nDRAW / TIE\n')

	elif u=='o':#o chunk
		for loop in range(9):
			if loop%2!=0:
				print('Your turn\n')
				n=input('Enter position: ')
				pos.append(n)
				os.system('cls')#'clear'
				for k in range(9):
					if n==play[k]:
						play[k]='x'
						for i in range(1,6):
							for j in range(1,6):
								if i%2!=0:
									if j%2!=0:
										print(play[a],end='')
										a+=1
									else:
										print('|',end='')
								else:
									if j%2!=0:
										print('-',end='')
									else:
										print('+',end='')
							print()
				a=0
				time.sleep(2)
				os.system('cls')#'clear'
				if play[0]==play[1]==play[2]=='x' or play[3]==play[4]==play[5]=='x' or play[6]==play[7]==play[8]=='x' or play[0]==play[3]==play[6]=='x' or play[1]==play[4]==play[7]=='x' or play[2]==play[5]==play[8]=='x' or play[0]==play[4]==play[8]=='x' or play[2]==play[4]==play[6]=='x':
					print('\nYAY!\nYOU WIN\n')
					flag=1
					# sys.exit()
					return
			else:
				print('COMPUTER\'S TURN\n')
				if (play[0]==play[1]=='x' and play[2]!='o') or (play[5]==play[8]=='x' and play[2]!='o') or (play[4]==play[6]=='x' and play[2]!='o') or (play[0]==play[1]=='o' and play[2]!='x') or (play[5]==play[8]=='o' and play[2]!='x') or (play[4]==play[6]=='o' and play[2]!='x'):#
					n='3'
				elif (play[0]==play[2]=='x' and play[1]!='o') or (play[4]==play[7]=='x' and play[1]!='o') or (play[0]==play[2]=='o' and play[1]!='x') or (play[4]==play[7]=='o' and play[1]!='x'):#
					n='2'
				elif (play[1]==play[2]=='x' and play[0]!='o') or (play[3]==play[6]=='x' and play[0]!='o') or (play[4]==play[8]=='x' and play[0]!='o') or (play[1]==play[2]=='o' and play[0]!='x') or (play[3]==play[6]=='o' and play[0]!='x') or (play[4]==play[8]=='o' and play[0]!='x'):#
					n='1'
				elif (play[0]==play[6]=='x' and play[3]!='o') or (play[4]==play[5]=='x' and play[3]!='o') or (play[0]==play[6]=='o' and play[3]!='x') or (play[4]==play[5]=='o' and play[3]!='x'):#
					n='4'
				elif (play[0]==play[8]=='x' and play[4]!='o') or (play[1]==play[7]=='x' and play[4]!='o') or (play[2]==play[6]=='x' and play[4]!='o') or (play[3]==play[5]=='x' and play[4]!='o') or (play[2]==play[6]=='o' and play[4]!='x') or (play[3]==play[5]=='o' and play[4]!='x') or (play[0]==play[8]=='o' and play[4]!='x') or (play[1]==play[7]=='o' and play[4]!='x'):
					n='5'
				elif (play[2]==play[8]=='x' and play[5]!='o') or (play[3]==play[4]=='x' and play[5]!='o') or (play[2]==play[8]=='o' and play[5]!='x') or (play[3]==play[4]=='o' and play[5]!='x'):#
					n='6'
				elif (play[0]==play[3]=='x' and play[6]!='o') or (play[2]==play[4]=='x' and play[6]!='o') or (play[7]==play[8]=='x' and play[6]!='o') or (play[0]==play[3]=='o' and  play[6]!='x') or (play[2]==play[4]=='o' and play[6]!='x') or (play[7]==play[8]=='o' and play[6]!='x'):#
					n='7'
				elif (play[1]==play[4]=='x' and play[7]!='o') or (play[6]==play[8]=='x' and play[7]!='o') or (play[1]==play[4]=='o' and play[7]!='x') or (play[6]==play[8]=='o' and play[7]!='x'):#
					n='8'
				elif (play[0]==play[4]=='x' and play[8]!='o') or (play[2]==play[5]=='x' and play[8]!='o') or (play[6]==play[7]=='x' and play[8]!='o') or (play[0]==play[4]=='o' and play[8]!='x') or (play[2]==play[5]=='o' and play[8]!='x') or (play[6]==play[7]=='o' and play[8]!='x'):#
					n='9'
				else:
					while True:
						n=str(random.randrange(1,9))
						if n not in pos:	
							break
						else:
							continue
				for k in range(9):
					if n==play[k]:
						pos.append(n)
						play[k]='o'
						for i in range(1,6):
							for j in range(1,6):
								if i%2!=0:
									if j%2!=0:
										print(play[a],end='')
										a+=1
									else:
										print('|',end='')
								else:
									if j%2!=0:
										print('-',end='')
									else:
										print('+',end='')
							print()
				a=0
				time.sleep(2)
				if play[0]==play[1]==play[2]=='o' or play[3]==play[4]==play[5]=='o' or play[6]==play[7]==play[8]=='o' or play[0]==play[3]==play[6]=='o' or play[1]==play[4]==play[7]=='o' or play[2]==play[5]==play[8]=='o' or play[0]==play[4]==play[8]=='o' or play[2]==play[4]==play[6]=='o':
					print('\nGAME OVER!\nCOMPUTER WON\n')
					flag=1
					# sys.exit()
					return
			print()
		if flag==0:
			print('\nDRAW / TIE\n')

	else:
		print('Invalid Choice')

# medium()