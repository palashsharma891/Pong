# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:28:44 2020

@author: Palash
"""

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation, not of paddle
paddle_a.shape("square") # default 20*20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # 100 pixels wide
paddle_a.penup() # remove the previous state
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation, not of paddle
paddle_b.shape("square") # default 20*20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # 100 pixels wide
paddle_b.penup() # remove the previous state
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation, not of paddle
ball.shape("square") # default 20*20 pixels
ball.color("white")
ball.penup() # remove the previous state
ball.goto(0, 0)
ball.dx = 0.2 # move 2 pixels right
ball.dy = -0.2 # 2 pixels up -> sqrt(8) northeast/southwest/...diagonally

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # don't draw when the pen moves
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 12, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 # Increase one 'block' at a time
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 # Decrease one 'block' at a time
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 # Increase one 'block' at a time
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 # Decrease one 'block' at a time
    paddle_b.sety(y)
    
# Keyboard binding
wn.listen() # listen to the keyboard input
wn.onkeypress(paddle_a_up, 'w') # change paddle_a's cordinate when w is pressed
wn.onkeypress(paddle_a_down, 's') # change paddle_a's cordinate when s is pressed
wn.onkeypress(paddle_b_up, 'Up') # change paddle_a's cordinate when up arrow is pressed
wn.onkeypress(paddle_b_down, 'Down') # change paddle_a's cordinate when down arrow is pressed

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border checking
    if ball.ycor() > 290: # height = 600, block = 20 pixels
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290: # height = 600, block = 20 pixels
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 12, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 12, "normal"))
    
    # paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
