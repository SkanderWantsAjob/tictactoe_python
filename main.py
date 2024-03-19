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


def someonelost():
        for row in gameboard:
            if(all(cell == row[0] for cell in row )):
                return (True,row[0])
        for x in range(3):
            if (all(gameboard[x][i] == gameboard[x][0] for i in range(3))):
                return (True,gameboard[x][0])
        if (all(gameboard[i][2-i] == gameboard[0][2] for i in range(3))):
            return (True, gameboard[0][2])
        if (all(gameboard[i][i] == gameboard[0][0] for i in range(3))):
            return (True, gameboard[0][0])
        return(False, "")




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



def chooseWhoGoesFirst():
    order = 0
    while(int(order) not in (2,1)):
        order= input ("\nwho is first you or pc ? type 2 for you and type 1 for PC\n")
    return (int(order))

gameover= someonelost()

turncounter = chooseWhoGoesFirst()
print(gameover[0])
while (not gameover[0]):
    if(turncounter % 2 == 0):
    #X turn
        printgameboard()
        playerturn()
    else:
        #O turn
        computerturn()
    turncounter += 1
    gameover = someonelost()
if (gameover[0] == True):
    print("SOMEONE WON I THINK AND IT IS ")
    print (f"this guy won : {gameover[1]}")

print("FOR THE FINAL OUTPUT")
printgameboard()



