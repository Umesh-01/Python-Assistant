import turtle
import random
import time


def game():

    delay=0.1
    score=0
    highstscore=0

    #snake body
    bodies=[]

    #getting a screen
    s=turtle.Screen()
    s.title("Snake Game")
    s.bgcolor("black")
    s.setup(width=600,height=600)
    s.cv._rootwindow.resizable(False, False)

    #create head of Snake
    head=turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("#79891A")
    head.fillcolor("#0CB968")
    head.penup()
    head.goto(0,0)
    head.direction="stop"

    #Food of Snake
    food=turtle.Turtle()
    food.speed(0)
    food.shape("turtle")
    food.color("yellow")
    food.fillcolor("#4ACB61")
    food.penup()
    food.ht()
    food.goto(0,200)
    food.st()

    #Game Score board
    sb=turtle.Turtle()
    sb.shape("square")
    sb.color("gray")
    sb.fillcolor("gray")
    sb.penup()
    sb.ht()
    sb.goto(-250,-250)
    sb.write("Score:0 | Highest Score:0")


    def moveup():
        if head.direction!="down":
            head.direction="up"
            
    def movedown():
        if head.direction!="up":
            head.direction="down"  
    def moveleft():
        if head.direction!="right":
            head.direction="left"
    def moveright():
        if head.direction!="left":
            head.direction="right" 

    def move():
        if head.direction=="up":
            y=head.ycor()
            head.sety(y+20)
        if head.direction=="down":
            y=head.ycor()
            head.sety(y-20)
        if head.direction=="left":
            x=head.xcor()
            head.setx(x-20)
        if head.direction=="right":
            x=head.xcor()
            head.setx(x+20)

    #Game Keyboard
    s.listen()
    s.onkey(moveup,"Up")
    s.onkey(movedown,"Down")
    s.onkey(moveleft,"Left")
    s.onkey(moveright,"Right")


    #main loop

    while True:
        s.update()  #this is to update the screen
        #Handle collission with border
        if head.xcor()>290:
            head.setx(-290)
        if head.xcor()<-290:
            head.setx(290)
        if head.ycor()>290:
            head.sety(-290)
        if head.ycor()<-290:
            head.sety(290)

        #chechk for collission with food
        if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)

            #increase the length of snake
            body=turtle.Turtle()
            body.speed(0)
            body.penup()
            body.shape("circle")
            body.color("#79891A")
            body.fillcolor("#0CB968")
            bodies.append(body)     #append new body

            #increase the score
            score+=5

            #change delay
            delay-=0.001

            #update the highestscore
            if score>highstscore:
                highstscore=score
            sb.clear()
            sb.write(f"Score: {score} | Highest Score: {highstscore}")
        
        #move the snake bodies
        for index in range(len(bodies)-1,0,-1):
            x=bodies[index-1].xcor()
            y=bodies[index-1].ycor()
            bodies[index].goto(x,y)

        if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
        move()

        #check for collision with snake body
        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"

                #hide bodies
                for body in bodies:
                    body.ht()
                bodies.clear()


                score=0
                delay=0.1

                #update the score board
                sb.clear()
                sb.write(f"Score: {score} | Highest Score: {highstscore}")
                s.bye()
        time.sleep(delay)
    s.mainloop()


if __name__ == '__main__':
    game()    
