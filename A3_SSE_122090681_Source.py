import random
import turtle
import time
import math

def control(x,y,z):     #using to change the the direction of the snake
    global aim,direct
    aim[0] = x
    aim[1] = y
    direct = z

def pause():        #if player stop the game, snake should pause
    global direct,aim
    direct = 0

def startgame(x,y):         #using this function to control the motion of the snkae
    redraw()
    timer = time.time()    
    turtle.hideturtle()     
    turtle.listen()
    turtle.onkey(lambda: control(0,20,1), 'Up')         #up
    turtle.onkey(lambda: control(0,-20,2), 'Down')      #down
    turtle.onkey(lambda: control(-20,0,3), 'Left')      #left
    turtle.onkey(lambda: control(20,0,4), 'Right')      #right
    turtle.onkey(pause, 'space')        #pause
    move()
    turtle.update()
    turtle.done()

def crashjudge():       #judging whether the monster and snake itself crash the snake
    global snake, monster,snakesize
    if (math.fabs(snake[0][0] - monster[0])<=10)and(math.fabs(snake[0][1]-monster[1]) <=10):        #snake and monster
        return True
    for i in range(1,snakesize):        #snake and it self
        if (snake[0][0] == snake[i][0])and(snake[0][1] == snake[i][1]):
            return True
    return False

def finishgame():       #the snake died, finished the game
    global monster
    turtle.penup()
    turtle.goto(monster[0],monster[1])
    turtle.write("Game Over!!!",font = "Arial 16 bold")
    win.exitonclick()

def contactjudge():         #judging whether the monster crash the snake's body
    global monster, snake, snakesize
    for i in range(snakesize):
        if (math.fabs(snake[i][0] - monster[0])<=20)and(math.fabs(snake[i][1]-monster[1]) <=20):
            return True
    return False

def foodjudge():        #judging whether the snake eats all the foods
    global food
    for i in range(5):
        if food[i][2] != 0:
            return False
    return True

def wingame():      #snake eats all the food, finish the game
    global snake
    turtle.penup()
    turtle.goto(snake[0][0],snake[0][1])
    turtle.write("Winner!!",font = "Arial 16 bold")
    win.exitonclick()

def changefood():       #open or hide the food, control the food's visiable
    global food
    while True:
        i = random.randint(0,4)
        if food[i][2]!=0:
            break
    if food[i][3]:
        food[i][3] = False
    else:
        food[i][3] = True
    judge = 0
    posi = 0
    for i in range(5):
        if food[i][2] !=0:
            judge = judge + 1
            posi = i
    if judge == 1:
        food[posi][3] = True
    
def move():         #move the snake, and judge the game in real time
    global contact,starttime,snake,snakesize,monster,direct,aim,timer,remainblock
    redraw()
    if remainblock != 0:        #change the speed of the snake
        snakespeed = 250
    else:
        snakespeed = 200
    if crashjudge():
        finishgame()
    if contactjudge():
        contact = contact + 1
    if foodjudge():
        wingame()
    timer = time.time()
    if (int(timer - starttime)%8==0):       #change the food per 8 seconds
        changefood()

    if direct == 0:     #using this function to move the snake and control it
        direct = 0  
    elif (-10<(snake[0][0]+aim[0])<=490)and(-10<(snake[0][1]+aim[1])<=490):
        if remainblock != 0:        #if the snake should become longer
            freshsnake = [[snake[0][0]+aim[0],snake[0][1]+aim[1]]]
            for i in range(0,snakesize):
                freshsnake.append([snake[i][0],snake[i][1]])
            snakesize = snakesize + 1
            remainblock = remainblock - 1
            snake = freshsnake
        else:       #else the snake will have a faster speed and keep moving
            freshsnake = []
            freshsnake.append([snake[0][0]+aim[0],snake[0][1]+aim[1]])
            for i in range(1,snakesize):
                freshsnake.append([snake[i-1][0],snake[i-1][1]])
            snake = freshsnake
        #print(snake)
        #print(freshsnake)
        for i in range(5):      #judging whether the snake eat the food
            a1 = snake[0][0]+10
            b1 = food[i][0]
            a2 = snake[0][1]+10
            b2 = food[i][1]
            if (a1==b1)and(a2==b2):
                if food[i][3]:
                    remainblock = remainblock + food[i][2]
                    food[i][2] = 0
            #print(snake[0][0],b1,snake[0][1],b2)
            #print(food)
        redraw()

    for i in range(snakespeed//50):         #monster movement with a random speed, if moster move 2 or 4 pixel per 0.05 second, snake move per 0.2 second with no food, per 0.25 second with food 
        x = monster[0] - snake[0][0]
        y = monster[1] - snake[0][1]
        monsterspeed  = random.randint(2,4)
        if math.fabs(x)>math.fabs(y):
            if x<0:
                monster[0] = monster[0] + monsterspeed
            else:
                monster[0] = monster[0] - monsterspeed
        else:
            if y<0:
                monster[1] = monster[1] + monsterspeed
            else:
                monster[1] = monster[1] - monsterspeed
        time.sleep(0.05)
        redraw()        #redraw the screen
    turtle.update()
    win.tracer(0)    
    turtle.ontimer(move(),snakespeed)   

def foodposition():         #creat the different food in random area
    food = []
    position = []
    for i in range(5):
        while True:
            x = random.randint(1,24) * 20
            y = random.randint(1,24) * 20
            if [x,y] not in position:
                break
        position.append([x,y])
        food.append([x,y,i+1,True])         #xposition, yposition, value of food, visiable or not
    return food

def redraw():       #the funtion to redraw the screen to refrash the time and contact
    global contact,timer,direct
    turtle.clear()
    turtle.penup()
    turtle.goto(-5,-5)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(3)
    turtle.goto(505,-5)
    turtle.goto(505,505)
    turtle.goto(-5,505)
    turtle.goto(-5,-5)
    turtle.goto(-5,585)
    turtle.goto(505,585)
    turtle.goto(505,505)
    drawsnake()
    drawmonster()
    drawfood()
    turtle.penup()
    turtle.goto(20,520)
    turtle.color("black")
    timer = time.time()
    directstring = ["Pause","Up","Down","Left","Right"]         #store the words of direction
    output = "Contact: " + str(contact) + "  Time: " + str(int(timer-starttime)) + "  Motion: " + directstring[direct]
    turtle.write(output, font = "Arial 16 bold")

def welcome_and_draw():         #the origin screen to welcome the player
    win.title("Snake board game")
    win.setup(580,660)
    win.setworldcoordinates(-40,-40,540,620)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(10,500)
    turtle.pendown()
    turtle.write('''Welcome to my snake game
Please use 4 arrow keys to control the movement of the snake,
eat all the number and try to dodge the monster
Have fun!''',font = "Arial 12 bold")
    turtle.penup()
    turtle.goto(-5,-5)
    turtle.pendown()
    turtle.color("black")
    turtle.pensize(3)
    turtle.goto(505,-5)
    turtle.goto(505,505)
    turtle.goto(-5,505)
    turtle.goto(-5,-5)
    turtle.goto(-5,585)
    turtle.goto(505,585)
    turtle.goto(505,505)
    turtle.penup()
    turtle.goto(snake[0][0],snake[0][1])
    turtle.color("red")
    turtle.stamp()
    turtle.penup()
    turtle.goto(monster[0],monster[1])
    turtle.color("purple")
    turtle.stamp()

def drawfood():         #draw the food which is visiable
    global food
    for i in range(5):
        if food[i][2] != 0:
            if food[i][3] == True:
                turtle.penup()
                turtle.color("black")
                turtle.goto(food[i][0]-15,food[i][1]-20)
                turtle.write(str(food[i][2]), font = "Arial 16 bold")

def drawsnake():            #draw the snake
    turtle.penup()
    turtle.clearstamp(-1)
    turtle.goto(snake[0][0],snake[0][1])
    turtle.color("red")
    turtle.stamp()
    for i in range(1,snakesize):
        turtle.penup()
        turtle.goto(snake[i][0],snake[i][1])
        turtle.color("black","blue")
        turtle.stamp()

def drawmonster():          #draw the monster
    turtle.penup()
    turtle.goto(monster[0],monster[1])
    turtle.color("purple")
    turtle.stamp()


###main function
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.shape("square")
turtle.pensize(20)
win = turtle.Screen()       #the screen of the turtle
snake = [(13*20-10,13*20-10)]       #this variable to store the position of the head and body of the snake 
snakesize = 1       #store the size of snake
remainblock = 4         #store the magnitude block the snake should grow longer
contact = 0         #store the contact number
direct = 1          #store the direction of the snake, 1 for up, 2 for down, 3 for left, 4 for right, 0 for pause
aim = [0,20]        #store the changing of the x,y position of the snake
monster = [random.randint(1,25)*20-10,random.randint(1,8)*20-10]        #random the position of the monster
welcome_and_draw()          #draw the origin area
food = foodposition()           #get the food position
#print(food)
#food = [[260, 280, 1, True], [400, 200, 2, False], [140, 40, 3, True], [20, 440, 4, True], [400, 420, 5, True]]
starttime = time.time()         #store the start time
timer = time.time()     
win.tracer(0)       
win.listen()
win.onscreenclick(startgame)        #start the game with a game click
turtle.done()
###main function