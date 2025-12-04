from turtle import *
import turtle
import random
import time

t=turtle.Turtle()
turtle.speed(5)
#turtle.setworldcoordinates(1,1,100,100)
#turtle.setworldcoordinates(0,0,200,500)
turtle.setup(800,700,350,50)


turtle.title("Bappa.py")

turtle.bgcolor("black")
turtle.color("red")
turtle.penup()

#turtle.setx(80)
turtle.pendown()
turtle.pensize(5)


turtle.left(60)
turtle.fd(50)
turtle.left(15)
turtle.circle(100,90)
turtle.fd(30)
turtle .pensize(10)
turtle.penup()
turtle.right(90)
turtle.fd(20)
turtle.pendown()

turtle.right(40)
turtle.circle(-50,90)
turtle.fd(20)
turtle.left(150)

#seconde head curve
turtle.color("red")
turtle.penup()
turtle.fd(40)
turtle.left(20)
turtle.pendown()
turtle.circle(50,90)

#third head curve-----

#goto beginning
turtle.color("red")
turtle.penup()
goto(0,0)
turtle.pensize(5)
turtle.pendown()
turtle.left(30)
turtle.fd(120)
turtle.circle(60,270)

#eyyes
turtle.color("red")
turtle.penup()
turtle.forward(30)
turtle.right(50)
turtle.forward(135)
turtle.pendown()
turtle.pensize(8)
turtle.circle(50,90)
turtle.left(95)
turtle.penup()
turtle.circle(60,75)

#eyebrows
turtle.penup()
turtle.forward(15)
turtle.left(90)
turtle.pensize(2)
turtle.pendown()
turtle.circle(70,90)

#ears
turtle.pensize(5)
turtle.penup()
turtle.forward(75)
turtle.right(90)
turtle.forward(20)
turtle.pendown()
turtle.circle(90,90)
turtle.forward(20)

turtle.circle(30,170)
turtle.right(180)
turtle.circle(28,180)
turtle.right(160)
turtle.circle(25,180)
turtle.right(160)
turtle.circle(22,160)
turtle.forward(20)
turtle.circle(60,45)


#trunk

turtle.penup()
goto(0,0)
turtle.left(130)
turtle.fd(140)
turtle.right(250)
turtle.backward(20)
#turtle.pendown()-------curve near neck
turtle.circle(80,20)
turtle.circle(20,40)

turtle.right(110)
turtle.penup()
turtle.fd(20)
turtle.pendown()
turtle.pensize(10)
turtle.forward(50)
turtle.circle(100,80)
turtle.pensize(9)
turtle.circle(150,50)
turtle.pensize(7)
turtle.circle(100,60)
turtle.pensize(5)
turtle.circle(90,60)
turtle.pensize(4)
turtle.circle(40,60)
turtle.circle(10,90)


#head
turtle.color("red")
turtle.penup()

goto(0,0)

goto(-90,290)
turtle.right(230)
turtle.pendown()

turtle.circle(-100,50)
turtle.circle(200,20)
turtle.circle(50,30)

turtle.right(180)

turtle.circle(50,30)
turtle.circle(200,20)
turtle.circle(-100,40)
turtle.right(95)
turtle.penup()
turtle.fd(40)
turtle.right(90)
turtle.pendown()
turtle.circle(100,40)
turtle.penup()
turtle.circle(35,120)
turtle.right(30)
turtle.pendown()
turtle.pensize(1)
turtle.circle(60,50)

#done
turtle.penup()

goto(-70,90)

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(20,180)
turtle.end_fill()

turtle.penup()
turtle.left(75)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(70,35)
turtle.end_fill()

turtle.left(180)
turtle.backward(10)
turtle.pendown()
turtle.left(6)
turtle.pensize(5)
turtle.color("red")
turtle.circle(-80,40)
turtle.penup()

#goto(0,0)

turtle.color("yellow")
turtle.penup()
goto(0,0)
turtle.left(180)
turtle.fd(240)
turtle.right(30)
turtle.pendown()
turtle.circle(90,65)



#borderrrr


done()