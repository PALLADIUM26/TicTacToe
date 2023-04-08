from easy2 import *
from medium2 import *
import os
import sys

os.system('cls')

while(True):
    
    print("WELCOME TO THE GAME\n")
    print("TIC TAC TOE\nThere are 3 levels of the game:\n\tEasy\n\tMedium\n\tHard\n")

    print('Enter\n1. for Easy\n2. for Medium\n3. Hard\n0. to Exit')
    ch = int(input("Your Choice: "))

    if ch == 1:
        easy()

    elif ch==2:
        medium()

    elif ch==3:
        print('Coming Soon !!!\nPlay Easy and Medium Levels\n')

    elif ch==0:
        sys.exit()
    
    else:
        print("Invalid Choice! Enter again")
        continue