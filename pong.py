# PONG GAME

import turtle
import winsound  # for sound

wn = turtle.Screen() # window
wn.title("Pong by @xeaj")
wn.bgcolor("black") # bg color
wn.setup(width=800, height=600) # width: 400 left 400 right, height: 300 up 300 down
wn.tracer(0) # stops the window from updating,
    # speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # sets speed to the max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) 

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # sets speed to the max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) 

# Ball
ball = turtle.Turtle()
ball.speed(0) # sets speed to the max possible speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0) 
ball.dx = 0.3 # change in x, moves by 2 pixels
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor() # coordinate of paddle a y coordinate
    y += 20 # moves it up
    paddle_a.sety(y) # set y coor to the new y with 20 added

def paddle_a_down():
    y = paddle_a.ycor() # coordinate of paddle a y coordinate
    y -= 20 # moves it down
    paddle_a.sety(y) # set y coor to the new y with 20 added

def paddle_b_up():
    y = paddle_b.ycor() # coordinate of paddle a y coordinate
    y += 20 # moves it up
    paddle_b.sety(y) # set y coor to the new y with 20 added

def paddle_b_down():
    y = paddle_b.ycor() # coordinate of paddle a y coordinate
    y -= 20 # moves it down
    paddle_b.sety(y) # set y coor to the new y with 20 added


# keyboard binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w") # when w is pressed, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") # when s is pressed, call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") # Up - up arrow key
wn.onkeypress(paddle_b_down, "Down") # Down - down arrow key

# Main game loop
while True:
    wn.update() # everytime the loop runs, the window updates

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # sets new coordinate for x
    ball.sety(ball.ycor() + ball.dy)

    # Border checking 
    # (what we want to happen when the ball hits the border)
    if ball.ycor() > 290: # top
        ball.sety(290)
        ball.dy *= -1 # reverses the direction of it hits the border
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290: # bottom
        ball.sety(-290)
        ball.dy *= -1 # reverses the direction of it hits the border
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    # right
    if ball.xcor() > 390: # if it has gone past the paddle and off the screen
        ball.goto(0,0) # goes back to center. restarts the game
        ball.dx *= -1
        score_a +=1
        pen.clear() #clears the screen b4 printing
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390: # left
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions

    # paddle_b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
    # if balls are touching, and is it between the top of the paddle and the bottom of the paddle
        ball.setx(340)
        ball.dx *= -1
    
    # paddle_a
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

