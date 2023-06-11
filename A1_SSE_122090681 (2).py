def begin_and_greet():      #input the number and judge it 
    print("Welcome to my puzzle game!")
    print("Please type 8 if you want to play 3*3 puzzle")
    print("Please type 15 if you want to play 4*4 puzzle")
    print("If you want to stop playing, please type stop")
    gametype = input()     #i to judge the type of the game
    if gametype == "8":
        return 8
    if gametype == "15":
        return 15
    if gametype == "stop":
        return 0
    while 1==1:     #ask user to input until he types in the correct answer 
        gametype = input("Sorry please type the correct input like 8, 15 or stop ")
        if gametype == "8":
         return 8
        if gametype == "15":
            return 15
        if gametype == "stop":
            return 0

def keyboard_control():     #ask user to input the letter to control the puzzle
    while 1==1:
        key_string = input("Enter the four letters used for left, right, up and down move >")
        return_keyboard = key_string.split()
        judge = True        #judge if all the inputs are letters
        if len(return_keyboard) != 4:
            judge = False
        elif (return_keyboard[0]==return_keyboard[1])or(return_keyboard[0]==return_keyboard[2])or(return_keyboard[0]==return_keyboard[3])or(return_keyboard[1]==return_keyboard[2])or(return_keyboard[1]==return_keyboard[3])or(return_keyboard[2]==return_keyboard[3]): judge = False
        for i in range(len(return_keyboard)):
            if len(return_keyboard[i]) > 1:
                judge = False
        if judge == True:
            return(return_keyboard)
        else:
            print("Sorry, please input the correct letters like a d w s")

def creat_puzzle(boardsize):     #creat a 3 or 4 size puzzle
    import random
    while 1==1:
        checklist = []
        returnlist = []
        for i in range(boardsize*boardsize):
            checklist.append(i+1)
        for i in range(boardsize*boardsize):
            index = random.randint(0,len(checklist)-1)    
            returnlist.append(checklist[index])
            checklist.pop(index)
        #print(returnlist)
        for i in range(len(returnlist)):
            if returnlist[i] == boardsize*boardsize :
                returnlist[i] = 0
        if checkboard(returnlist):
            break
    return returnlist

def checkboard(board):      #in some case, the board will do not have answer to be a sorted link, this function can calculate the boardlist and return whether it have a solution
    #this function use a algorithm that calculate the inversion number of the list. A 3*3 board the total inversion number must be even, a 4*4 board should have odd number
    ans = 0     #calculate the inversion number
    space = 0       #store the position of 0
    for i in range(1,len(board)):
        counter = 0
        if board[i] == 0:
            space = i
        for j in range(i):
            if board[j]>board[i]:
                counter = counter + 1
        ans = ans + counter
    if len(board) == 9:     #ans should add the line and row number of positon of space
        lis = [0,1,2,1,2,3,2,3,4]
        ans = ans + lis[space]
        if ans % 2 == 0:
            return True
    if len(board) == 16:
        lis = [0,1,2,3,1,2,3,4,2,3,4,5,3,4,5,6]
        ans = ans + lis[space]
        if ans % 2 == 1:
            return True
    return False

def check(checkboard):      #check whether the board is completed
    ans = True
    for i in range(len(checkboard)-1):
        if i+1 != checkboard[i]:
            ans = False
    return ans

def getthemove(checkboard,movement):        #find the space of the board and print the movement user can do
    finder = 0
    for i in range(len(checkboard)):
        if checkboard[i] == 0:
            finder = i
    if len(checkboard) == 9:        #facing the 9 movement
        movecheck = [[1,0,1,0],[1,1,1,0],[0,1,1,0],
        [1,0,1,1],[1,1,1,1],[0,1,1,1],
        [1,0,0,1],[1,1,0,1],[0,1,0,1]]      #store the acceptable movement of the board
        outstr = ["left-" + movement[0] + ", ","right-" + movement[1] + ", ","up-" + movement[2] + ", ","down-" + movement[3] + ", "]
        out = "Enter your move ("
        for i in range(4):
            if movecheck[finder][i] == 1:
                out = out + outstr[i]
        out = out[:-2] + ") > "
        for i in range(len(checkboard)):
            if checkboard[i] == 0:
                print("   ",end="")
            else:
                print("%-3s" %str(checkboard[i]),end="")
            if (i==2)or(i==5)or(i==8):
                print("")
        ans = input(out)
        position = -1
        check = False
        for i in range(4):
            if ans == movement[i]:
                position = i
        if position != -1:
            if movecheck[finder][position] == 1:
                check = True
        if check:
            return position
        while 1==1:
            print("Sorry, please type the correct letter")
            ans = input(out)
            position = -1
            check = False
            for i in range(4):
                if ans == movement[i]:
                    position = i
            if position != -1:
                if movecheck[finder][position] == 1:
                    check = True
            if check:
                return position
    if len(checkboard) == 16:       #same as the 9 board
        movecheck = [[1,0,1,0],[1,1,1,0],[1,1,1,0],[0,1,1,0],
        [1,0,1,1],[1,1,1,1],[1,1,1,1],[0,1,1,1],
        [1,0,1,1],[1,1,1,1],[1,1,1,1],[0,1,1,1],
        [1,0,0,1],[1,1,0,1],[1,1,0,1],[0,1,0,1]]        #have the feasible movement of a 4*4 board
        outstr = ["left-" + movement[0] + ", ","right-" + movement[1] + ", ","up-" + movement[2] + ", ","down-" + movement[3] + ", "]
        out = "Enter your move ("
        for i in range(4):
            if movecheck[finder][i] == 1:
                out = out + outstr[i]
        out = out[:-2] + ") > "
        for i in range(len(checkboard)):
            if checkboard[i] == 0:
                print("   ",end="")
            else:
                print("%-3s" %str(checkboard[i]),end="")
            if (i==3)or(i==7)or(i==11)or(i==15):
                print("\n")
        ans = input(out)
        position = -1
        check = False
        for i in range(4):
            if ans == movement[i]:
                position = i
        if position != -1:
            if movecheck[finder][position] == 1:
                check = True
        if check:
            return position
        while 1==1:
            print("Sorry, please type the correct letter")
            ans = input(out)
            position = -1
            check = False
            for i in range(4):
                if ans == movement[i]:
                    position = i
            if position != -1:
                if movecheck[finder][position] == 1:
                    check = True
            if check:
                return position

def movetheboard(puzzle,movement):      #receive a movement order and return the final board
    finder = 0
    for i in range(len(puzzle)):
        if puzzle[i] == 0:
            finder = i
    if len(puzzle) == 9:
        retrunpuzzle = puzzle
        movepointer = [[1,0,3,0],[2,0,4,0],[0,1,5,0],
        [4,0,6,0],[5,3,7,1],[0,4,8,2],
        [7,0,0,3],[8,6,0,4],[0,7,0,5]]      #the target of every number of a 3*3 board
        retrunpuzzle[finder] = retrunpuzzle[movepointer[finder][movement]]
        retrunpuzzle[movepointer[finder][movement]] = 0
        return retrunpuzzle
    if len(puzzle) == 16:
        retrunpuzzle = puzzle
        movepointer = [[1,0,4,0],[2,0,5,0],[3,1,6,0],[0,2,7,0],
        [5,0,8,0],[6,4,9,1],[7,5,10,2],[0,6,11,3],
        [9,0,12,4],[10,8,13,5],[11,9,14,6],[0,10,15,7],
        [13,0,0,8],[14,12,0,9],[15,13,0,10],[0,14,0,11]]        #the target of every number of a 4*4 board
        retrunpuzzle[finder] = retrunpuzzle[movepointer[finder][movement]]
        retrunpuzzle[movepointer[finder][movement]] = 0
        return retrunpuzzle

def congratulate(ans):      #this is to congratulate the user for his winning
    print("Congratulations! You solved the puzzle in ", ans ," moves!")
    
def apuzzle():      #3*3 puzzle game
    keyboard = keyboard_control()       #save the control letter
    #print(keyboard)
    board = creat_puzzle(3)     #save the puzzle
  #  board = [1,2,3,4,5,6,7,0,8]
    #print(board)
    counter = 0
    while not check(board):
        counter = counter + 1
        move = getthemove(board,keyboard)       #the the user's movement
        #print(move)
        board = movetheboard(board,move)
    congratulate(counter)

def bpuzzle():      #4*4 puzzle game
    keyboard = keyboard_control()
    #print(keyboard)
    board = creat_puzzle(4)
    #board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15]
    #print(board)
    counter = 0
    while not check(board):
        counter = counter + 1
        move = getthemove(board,keyboard)
        #print(move)
        board = movetheboard(board,move)
    congratulate(counter)   

while 1==1:     #make the game repeatable
    game = begin_and_greet()
    if game == 8:
        apuzzle()
        #print(8)
    if game == 15:
        bpuzzle()
        #print(15)
    if game == 0:
        print("Bye")
        break
    ask = input("Do you want to play again? Please type yes or no: ")
    if ask == "no ":
        print("Thanks for playng! Bye")
        break
#print(1)