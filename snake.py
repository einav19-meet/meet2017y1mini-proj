import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup
SQUARE_SIZE=22
START_LENGTH=6
turtle.color("#BD2CE1")
turtle.bgcolor("#010303")

#initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.penup()
snake = turtle.clone()
snake.shape("square")

turtle.register_shape("strawbery.gif")
turtle.register_shape("wm.gif")
turtle.register_shape("apple1.gif")
turtle.register_shape("pie.gif")
turtle.register_shape("pop.gif")

food= turtle.clone()


turtle.hideturtle()



for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)

    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction=UP
    print("you pressed UP!")

def left():
    global direction
    direction=LEFT
    print("you pressed LEFT!")

def down():
    global direction
    direction=DOWN
    print("you pressed DOWN!")
    
def right():
    global direction
    direction=RIGHT
    print("you pressed RIGHT!")

def make_food():    
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1

    
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    #food.goto(food_x,food_y)
    #food_pos.append((food_x, food_y))
    #stamp_id=food.stamp()
    #food_stamps.append(stamp_id)

    #generates a random number between 0 and 3
    r = random.randint(0,4)
    if r==0:
        food.shape("wm.gif")
    elif r==1:
        food.shape("strawbery.gif")
    elif r==2:
        food.shape("apple1.gif")
    elif r==3:
        food.shape("pie.gif")
    elif r==4:
        food.shape("pop.gif") 

        
    food.goto(food_x,food_y)
    food_pos.append((food_x, food_y))
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)
        
    
          
    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + SQUARE_SIZE,y_pos)
        print("you moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE,y_pos)
        print("you moved left!")
    elif direction == UP:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("you moved up!")
    elif direction == DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("you moved down!")
   
        
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    my_pos=snake.pos()
    pos_list.append(my_pos)
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food! getting BIGGER...")
        make_food()
    else:
        
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("GAME OVER!!!!!!!!!!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("GAME OVER!!!!!!!!!!")
        quit()
    elif new_y_pos >= UP_EDGE:
        print("GAME OVER!!!!!!!!!!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("GAME OVER!!!!!!!!!!")
        quit()
    elif new_pos in pos_list[:-1]:
        print("GAME OVER!!!!!!!")
        quit()
    
    

    turtle.ontimer(move_snake,TIME_STEP)



             
    

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()
make_food()
move_snake()




    
    
    
        
