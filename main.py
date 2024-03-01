import random

def printgameboard():
    for x in range(rows):
        print("+---+---+---+---+")
        for y in range (cols):
            print("|", end="")
            print(" ", gameboard[x][y], end= " |")
        print()
    print("+---+---+---+---+")

print("welcome to Tic Tac Toe")
print("****************************************")
numbersleft=list(range(1,10))
gameboard=[[1,2,3],[4,5,6],[7,8,9]]
rows=3
cols=3


def modifyboard(num, turn):
    num-=1
    gameboard[int(num / 3)][int(num % 3)]= turn

leaveloop= False
turn = 'X'
turncounter=0
def playerturn():
    while (True):
        playerchoice = int(input("\n Choose a number from 1 to 9\n"))
        if (playerchoice > 9 or playerchoice < 1 or playerchoice not in numbersleft):
            print("invalid, you gotta choose from ", numbersleft)
            continue
        numbersleft.remove(playerchoice)
        modifyboard(playerchoice, 'X')
        break

def computerturn():
    while (True):
        cpuchoice = random.choice(numbersleft)
        if (cpuchoice in numbersleft):
            print("THE ALMIGHTY COMPUTER HAS CHOSEN ", cpuchoice)
            numbersleft.remove(cpuchoice)
            modifyboard(cpuchoice, 'O')
            break

while (turncounter < 9):
    if(turncounter % 2 == 0):
    #X turn
        printgameboard()
        playerturn()
    else:
        #O turn
        computerturn()
    print(turncounter)
    turncounter += 1
print("FOR THE FINAL OUTPUT")
printgameboard()



