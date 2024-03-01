import random

def printgameboard():
    for x in range(grows):
        print("+---+---+---+---+")
        for y in range (gcols):
            print("|", end="")
            print(" ", gameboard[x][y], end= " |")
        print()
    print("+---+---+---+---+")

print("welcome to Tic Tac Toe")
print("****************************************")
numbersleft=list(range(1,10))
gameboard=[[1,2,3],[4,5,6],[7,8,9]]
grows=3
gcols=3


def modifyboard(num, turn):
    num-=1
    gameboard[int(num / 3)][int(num % 3)]= turn

leaveloop= False
turn = 'X'
turncounter=0
def someonewon():
    for row in gameboard:
        if( all(cell == 'X' for cell in row ) or all (cell == 'O' for cell in row)):
            return True
    for x in range(3):
        if (all(row[x]=='X' for row in gameboard ) or all(row[x]== 'O' for row in gameboard)):
            return True
    if all(gameboard[i][i] == 'X' for i in range(3)) or all(gameboard[i][2 - i] == 'X' for i in range(3)):
        return True
    if all(gameboard[i][i] == 'O' for i in range(3)) or all(gameboard[i][2 - i] == 'O' for i in range(3)):
        return True

    return False


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

gameover= False
while (gameover == False):
    if(turncounter % 2 == 0):
    #X turn
        printgameboard()
        playerturn()
    else:
        #O turn
        computerturn()
    print(turncounter)
    turncounter += 1
    gameover= someonewon()
if (gameover == True):
    print("SOMEONE WON I THINK")
print("FOR THE FINAL OUTPUT")
printgameboard()



