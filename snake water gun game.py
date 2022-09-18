print("computers turn: snake(s), water(w) or gun(g)")
print("computer already choosen between s,w or g  randomly now yours turn")
yoursturn=input("please select(player's turn) snake(s),water(w) or gun(g)")

import random
randno = random.randint(1,3)
print(randno)
if (randno==1):
    computer='s'
elif (randno==2):
    computer='w'
elif (randno==3):
    computer='g'

# check for all possibilities when computer choose s
def gamewin(computer,yoursturn):
    if(computer==yoursturn):
        return None
    elif(computer=='s'):
        if(yoursturn=='w'):
            return False
        elif(yoursturn=='g'):
            return True

# check for all possibilities when computer choose w
    elif(computer=='w'):
        if(yoursturn=='g'):
            return False
        elif(yoursturn=='s'):
            return True

# check for all possibilities when computer choose g
    elif(computer=='g'):
        if(yoursturn=='s'):
            return False
        elif(yoursturn=='w'):
            return True
            
print(f"computer selected{computer}\n")
print(f"you selected{yoursturn}\n")
    
a=gamewin(computer,yoursturn)
if (a == None):
    print("the game is tie\n")
elif(a):
    print("you win\n")
else:
    print('''you lose,
computer win\n''')
print("The game is over !!")


