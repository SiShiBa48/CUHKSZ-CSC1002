import turtle as t

def draw():  # this fubction is used to draw the origin screen(8 black blocks)
    board.hideturtle()
    board.speed(0)
    board.penup()
    board.shape("square")
    board.pensize(1)
    board.goto(-310, -310)
    for i in range(8):  # draw 8 blocks
        blank = i * 80
        board.penup()
        board.goto(-310 + blank, -310)
        board.pendown()
        board.fillcolor("black")
        board.begin_fill()
        board.goto(-310 + blank + 60, -310)
        board.goto(-310 + blank + 60, -290)
        board.goto(-310 + blank, -290)
        board.goto(-310 + blank, -310)
        board.end_fill()


# this fuction is used to judge whether the player have finished the game, return is True or False
def checkboard(boardneedcheck):
    for i in range(8):  # check the horizontal line solution
        for j in range(4):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i][j+1] != 0) and (boardneedcheck[i][j+2] != 0) and (boardneedcheck[i][j+3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i][j+1] + boardneedcheck[i][j+2] + boardneedcheck[i][j+3] == 4:
                    return True
                if boardneedcheck[i][j] + boardneedcheck[i][j+1] + boardneedcheck[i][j+2] + boardneedcheck[i][j+3] == 8:
                    return True
    for i in range(4):
        for j in range(8):  # check the vertical token solution
            if (boardneedcheck[i+1][j] != 0) and (boardneedcheck[i][j] != 0) and (boardneedcheck[i+2][j] != 0) and (boardneedcheck[i+3][j] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j] + boardneedcheck[i+2][j] + boardneedcheck[i+3][j] == 4:
                    return True
                if boardneedcheck[i][j] + boardneedcheck[i+1][j] + boardneedcheck[i+2][j] + boardneedcheck[i+3][j] == 8:
                    return True
    for i in range(5):  # check the slide solution
        for j in range(5):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i+1][j+1] != 0) and (boardneedcheck[i+2][j+2] != 0) and (boardneedcheck[i+3][j+3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j+1] + boardneedcheck[i+2][j+2] + boardneedcheck[i+3][j+3] == 4:
                    return True
                if boardneedcheck[i][j] + boardneedcheck[i+1][j+1] + boardneedcheck[i+2][j+2] + boardneedcheck[i+3][j+3] == 8:
                    return True
    for i in range(5):  # check the slide solution
        for j in range(3, 8):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i+1][j-1] != 0) and (boardneedcheck[i+2][j-2] != 0) and (boardneedcheck[i+3][j-3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j-1] + boardneedcheck[i+2][j-2] + boardneedcheck[i+3][j-3] == 4:
                    return True
                if boardneedcheck[i][j] + boardneedcheck[i+1][j-1] + boardneedcheck[i+2][j-2] + boardneedcheck[i+3][j-3] == 8:
                    return True
    return False


    

# this function is used to add token to the screen and the memorize list keyboard
def addtoken(x, y):  
    global counter
    global keyboard
    counter = counter + 1
    if checkboard(keyboard):  # if there exist a solution, stop the game and highlight the solution
        #print("222222")
        congratulate(keyboard)
    if counter == 65:  # if the game fail,  stop the game
        failure()
    # print(counter)
    if counter % 2 == 1:  # change the title
        s = "It's player 1's turn, your color is blue"
        win.title(s)
    else:
        s = "It's player 2's turn, your color is purple"
        win.title(s)
    # find the coordinate of token
    row = -1
    if (x >= -310) and (x <= -250):
        row = 0
    if (x >= -230) and (x <= -170):
        row = 1
    if (x >= -150) and (x <= -90):
        row = 2
    if (x >= -70) and (x <= -10):
        row = 3
    if (x >= 10) and (x <= 70):
        row = 4
    if (x >= 90) and (x <= 150):
        row = 5
    if (x >= 170) and (x <= 230):
        row = 6
    if (x >= 250) and (x <= 310):
        row = 7
    if row == -1:
        counter = counter - 1
        return
    i = 0
    while keyboard[i][row] != 0:
        i = i + 1
        if i == 8:
            break
   # print(keyboard)
    if i > 7:
        counter = counter - 1
        return
    if counter % 2 == 1:
        keyboard[i][row] = 1
    else:
        keyboard[i][row] = 2
    xposition = -280 + 80 * row
    yposition = -270 + 70 * i
    # finish finding、

    # start drawing
    board.penup()
    board.goto(xposition, yposition)
    board.pendown()
    if counter % 2 == 1:
        board.color("blue")
        board.fillcolor("blue")
    else:
        board.color("purple")
        board.fillcolor("purple")
    board.begin_fill()
    board.circle(30)
    board.end_fill()
    # finish drawing
    if checkboard(keyboard):  # if there exist a solution, stop the game and highlight the solution
        #print("222222")
        congratulate(keyboard)


# this function is used to find the position of the solution, return is a list with four tokens' positons and the winner
def checkanswer(boardneedcheck):
    for i in range(8):
        for j in range(4):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i][j+1] != 0) and (boardneedcheck[i][j+2] != 0) and (boardneedcheck[i][j+3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i][j+1] + boardneedcheck[i][j+2] + boardneedcheck[i][j+3] == 4:
                    returnlist = [[i, j], [i, j+1], [i, j+2], [i, j+3], [1]]
                    return returnlist
                if boardneedcheck[i][j] + boardneedcheck[i][j+1] + boardneedcheck[i][j+2] + boardneedcheck[i][j+3] == 8:
                    returnlist = [[i, j], [i, j+1], [i, j+2], [i, j+3], [2]]
                    return returnlist
    for i in range(4):
        for j in range(8):
            if (boardneedcheck[i+1][j] != 0) and (boardneedcheck[i][j] != 0) and (boardneedcheck[i+2][j] != 0) and (boardneedcheck[i+3][j] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j] + boardneedcheck[i+2][j] + boardneedcheck[i+3][j] == 4:
                    returnlist = [[i, j], [i+1, j], [i+2, j], [i+3, j], [1]]
                    return returnlist
                if boardneedcheck[i][j] + boardneedcheck[i+1][j] + boardneedcheck[i+2][j] + boardneedcheck[i+3][j] == 8:
                    returnlist = [[i, j], [i+1, j], [i+2, j], [i+3, j], [2]]
                    return returnlist
    for i in range(5):
        for j in range(5):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i+1][j+1] != 0) and (boardneedcheck[i+2][j+2] != 0) and (boardneedcheck[i+3][j+3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j+1] + boardneedcheck[i+2][j+2] + boardneedcheck[i+3][j+3] == 4:
                    returnlist = [[i, j], [i+1, j+1],
                                  [i+2, j+2], [i+3, j+3], [1]]
                    return returnlist
                if boardneedcheck[i][j] + boardneedcheck[i+1][j+1] + boardneedcheck[i+2][j+2] + boardneedcheck[i+3][j+3] == 8:
                    returnlist = [[i, j], [i+1, j+1],
                                  [i+2, j+2], [i+3, j+3], [2]]
                    return returnlist
    for i in range(5):
        for j in range(3, 8):
            if (boardneedcheck[i][j] != 0) and (boardneedcheck[i+1][j-1] != 0) and (boardneedcheck[i+2][j-2] != 0) and (boardneedcheck[i+3][j-3] != 0):
                if boardneedcheck[i][j] + boardneedcheck[i+1][j-1] + boardneedcheck[i+2][j-2] + boardneedcheck[i+3][j-3] == 4:
                    returnlist = [[i, j], [i+1, j-1],
                                  [i+2, j-2], [i+3, j-3], [1]]
                    return returnlist
                if boardneedcheck[i][j] + boardneedcheck[i+1][j-1] + boardneedcheck[i+2][j-2] + boardneedcheck[i+3][j-3] == 8:
                    returnlist = [[i, j], [i+1, j-1],
                                  [i+2, j-2], [i+3, j-3], [2]]
                    return returnlist


# this function is used to highlight the solution and stop the game
def congratulate(boardfind):
    answerlist = checkanswer(boardfind)  # get the solution
    # start highlighting
    board.penup()
    for i in range(4):
        board.color("red")
        board.pensize(5)
        board.goto(-280 + 80 * answerlist[i][1], -270 + 70 * answerlist[i][0])
        board.pendown()
        board.circle(30)
        board.penup()
    if answerlist[4][0] == 1:
        win.title("Congratulations! Player 1 win!")
        board.goto(-200, 0)
        board.color("black")
        board.write("Player 1 win!", font=("宋体",40,"normal"))
    else:
        win.title("Congratulations! Player 2 win!")
        board.goto(-200, 0)
        board.color("black")
        board.write("Player 2 win!", font=("宋体",40,"normal"))
    # finish highlighting
    #win.ontimer(timer(), 5000)  # count for 5 sec
    win.exitonclick()  # stop the game

# this function is used to stop the game when the step is more than 65 times
def failure():  
    board.write("Game Tied!", font=("宋体",40,"normal"))
    win.exitonclick()


def redraw():       #redraw the blocks, and make it black
    for i in range(8):
        board.penup()
        board.color("black")
        board.pensize(3)
        blank = 80 * i
        board.goto(-310 + blank, -310)
        board.pendown()
        board.goto(-310 + blank + 60, -310)
        board.goto(-310 + blank + 60, -290)
        board.goto(-310 + blank, -290)
        board.goto(-310 + blank, -310)
        board.penup()


def motion(event):  # this function is used to chace the mice motion
    global xlast,counter
    # get the position of the token
    row = -1
    # print("11111111111111")
    x = event.x - 330
    y = event.y - 330
    #print('{}, {}'.format(x,y))
    if -330 < y < 330:
        if (x >= -310) and (x <= -250):
            redraw()
            row = 0
            board.penup()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= -230) and (x <= -170):
            row = 1
            redraw()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.penup()
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= -150) and (x <= -90):
            row = 2
            redraw()
            board.penup()
            board.pensize(3)
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= -70) and (x <= -10):
            row = 3
            redraw()
            board.penup()
            board.pensize(3)
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= 10) and (x <= 70):
            row = 4
            redraw()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.penup()
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= 90) and (x <= 150):
            row = 5
            redraw()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.penup()
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= 170) and (x <= 230):
            row = 6
            redraw()
            board.penup()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        if (x >= 250) and (x <= 310):
            row = 7
            redraw()
            if counter % 2 ==0:
                board.color("blue")
            else:
                board.color("purple")
            board.penup()
            board.pensize(3)
            blank = 80 * row
            board.goto(-310 + blank, -310)
            board.pendown()
            board.goto(-310 + blank + 60, -310)
            board.goto(-310 + blank + 60, -290)
            board.goto(-310 + blank, -290)
            board.goto(-310 + blank, -310)
            board.penup()
        xlast = event.x


def timer():  # a timer function
    return


board = t.Turtle()  # the turtle of the screen
win = t.Screen()  # the windows
win.setup(660, 660)
draw()
# creat the blank keyboard to store the tokens
keyboard = []
for i in range(8):
    line = []
    for j in range(8):
        line.append(0)
    keyboard.append(line)
# finish creating

counter = 0  # memorize the step of the players, and memorize the sequence of the players
xlast = 0  # follow the mice motion
# when clicking the mice, the addtoken function will start
win.tracer(0, 0)
can = t.getcanvas()
can.bind("<Motion>", motion)
win.listen()
win.onclick(addtoken)
win.mainloop()