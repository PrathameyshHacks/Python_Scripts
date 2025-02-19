# this is turtle python script coded by Prathameysh Acharekar 
# in this script i am using turtle graphics for creating a 
# portrait of Chhatrapati Shivaji Maharaj 


import turtle

t = turtle.Turtle()

# lets setup frame dimensions & co-ordinates
turtle.setup(width=800,height=700,startx=370,starty=30)

# set a title for frame 
turtle.title("CSM_Graphics")

# set a background image for canvas
# replace file address with your PCs file address
# else just save image in same project directory


# THE SOURCE CODE IS POSTED ON MY GITHUB ACC
# AND REPOSITORY LINK IS IN MY BIO 




turtle.bgpic("CanBgPNG.png")

# setup size of marker & speed of painting

t.pensize(5)
t.speed(15)

#turtle.bgcolor("#EC1313")

t.color("black")  


t.penup()

t.goto(-120,50)
t.goto(-190,110)
t.goto(-280,150)

# lets create Knight ...
t.pendown()
t.fillcolor("black")
# Knight's head_feather ...
t.begin_fill()
t.lt(140)
t.circle(-25,80)
t.lt(2)
t.fd(35)
t.rt(50)
t.fd(15)
t.lt(15)
t.fd(15)
t.rt(145)
t.fd(20)
t.lt(40)
t.circle(-100,20)
#.....
t.lt(90)
t.fd(10)
t.rt(120)
t.fd(10)
t.lt(50)
t.fd(10)
t.rt(90)
t.fd(55)

#.....

# draw knight's Head ...


t.lt(103)
t.fd(20)
t.rt(30)
t.fd(15)
t.lt(55)
t.fd(5)
t.circle(-20,40)
t.rt(40)
t.fd(5)
t.lt(30)
t.fd(12)
t.lt(30)
t.fd(15)
t.rt(70)
t.fd(5)
t.lt(80)
t.fd(40)
t.rt(70)
t.fd(10)
t.lt(80)
t.fd(15)
#knight chin ...
t.lt(50)
t.fd(15)
t.lt(15)
t.fd(10)
t.lt(20)
t.fd(15)
t.lt(60)    #
t.fd(9)
t.lt(15)
t.fd(8)
t.lt(55)
t.fd(5)

# ....

t.rt(70)
t.fd(8)

# ....

t.rt(30)
t.fd(8)
t.rt(20)
t.fd(10)
t.rt(45)
t.circle(-20,100)
# creating knight's neck .....

t.lt(25)
t.fd(10)
t.lt(75)
t.fd(5)
t.rt(85)
t.fd(15)
t.lt(10)
t.fd(15)
t.lt(75)
t.fd(5)
t.rt(90)
t.fd(25)

# creating knight's forward leg .....

t.rt(45)
t.fd(10)
t.lt(20)
t.fd(10)
t.lt(30)
t.fd(15)
t.lt(25)
t.fd(15)

# .....

t.lt(55)
t.fd(2)

# .....
t.rt(105)
t.fd(10)

# .....

t.rt(85)
t.fd(15)
t.rt(10)
t.fd(20)
t.lt(10)
t.fd(20)
t.lt(20)
t.fd(10)
t.lt(10)
t.fd(8)
t.lt(60)
t.fd(10)
t.lt(10)
#
t.fd(40)
t.lt(10)
#
t.fd(30)
t.lt(5)
t.fd(20)
t.rt(12)
t.circle(20,60)
t.fd(20)
t.lt(10)
t.fd(20)
t.lt(80)
t.circle(30,30)
t.lt(10)
t.fd(15)
#
t.lt(100)
t.fd(5)
t.rt(30)
t.fd(5)
t.rt(20)
t.fd(10)
#
t.circle(-10,50)
t.fd(15)
t.rt(5)
t.fd(25)
#
t.lt(3)
t.circle(-30,30)

t.rt(35)
t.circle(-30,45)
#
t.rt(10)
t.fd(30)
t.rt(5)
t.fd(10)
t.rt(15)
t.fd(15)
t.rt(5)
t.fd(5)

#frontLeg Done()#
#2nd froLeg#
t.penup()
#t.setx(0)
#t.sety(0)
t.setx(-125)
t.sety(-115)
t.pendown()
#start
t.rt(40)
t.fd(40)
t.lt(17)
t.fd(15)
t.rt(21)
#leg_len()
t.fd(55)
#
t.rt(5)
t.fd(30)
###
t.rt(35)
t.fd(15)
t.rt(30)
t.fd(10)
t.lt(38)
t.fd(20)
t.lt(110)
t.fd(30)
#back#
t.lt(70)
t.fd(15)
t.rt(10)
t.fd(10)
t.rt(5)
t.fd(5)
t.lt(42)
t.fd(20)
t.rt(1)
#leg_len()
t.fd(50)
#
t.rt(3)
t.fd(65)
t.lt(15)
t.fd(10)
#
t.rt(55)
t.fd(15)
t.lt(35)
t.fd(10)
#
t.rt(95)
t.fd(40)
t.lt(10)
#sto_len
t.fd(45)
#
t.lt(15)
t.fd(30)
#stodone()
#back_leg_start()
t.speed(15)
t.rt(95)
t.fd(20)
t.lt(10)
t.fd(15)
t.lt(30)
t.fd(25)
t.rt(25)
t.fd(7)
t.rt(35)
t.fd(7)
t.rt(43)
#leg_len()
t.fd(40)
#
t.rt(10)
t.fd(15)
t.rt(10)
t.fd(5)
#
#
t.lt(60)
t.fd(10)
t.rt(15)
t.fd(10)
t.lt(15)
t.fd(15)
t.lt(35)
t.fd(10)
t.lt(35)
t.fd(5)
t.lt(30)
t.fd(5)
t.lt(30)
t.fd(10)
t.lt(30)
t.fd(10)
t.lt(25)
t.fd(5)
t.lt(25)
t.fd(12)
t.rt(30)
t.fd(5)
#back
t.rt(63)
t.fd(10)
t.lt(22)
#leg_len()
t.fd(40)
#
t.rt(10)
t.fd(30)
t.circle(10,100)
t.fd(15)
t.rt(25)
t.fd(5)
t.rt(15)
t.fd(7)
#leg_done()
#last_leg_start()
t.rt(113)
t.fd(15)
t.lt(27)
#gap()
t.fd(25)
#
t.rt(35)
t.fd(35)
t.rt(55)
#leg_len()
t.fd(70)
#
t.rt(35)
t.fd(20)
t.lt(30)
t.fd(10)
t.rt(25)
t.fd(20)
t.lt(30)
t.fd(18)
t.lt(87)
#foot
t.fd(25)
t.lt(94)
t.fd(10)
t.rt(30)
t.fd(13)
t.lt(25)
t.fd(10)
t.rt(70)
t.fd(5)
t.lt(55)
t.fd(1)
t.rt(50)
t.fd(7)
t.circle(10,140)
t.rt(75)
#leg_len()
t.fd(60)
#
t.rt(10)
t.circle(100,40)
t.rt(20)
t.fd(5)
t.circle(-50,20)
t.circle(100,30)
#back_leg_done()
#go_back
#
#t.speed(100)

#t.penup()

t.goto(0,0)
t.goto(-120,50)
t.goto(-190,110)
t.goto(-280,150)

#t.setx(-50)
#t.sety(50)
#t.setx(-200)
#t.sety(100)
#t.setx(-280)
#t.sety(150)
#t.pendown()
t.lt(120)
t.fd(20)
t.goto(-240,153)
#
#neck_up_start()
t.lt(80)
t.fd(8)
t.lt(90)
t.fd(8)
t.rt(90)
t.fd(12)
t.lt(90)
t.fd(10)
t.rt(90)
t.fd(10)
t.lt(70)
t.fd(10)
t.rt(40)
t.fd(20)
t.rt(30)
t.fd(15)
t.lt(70)
t.fd(5)
t.rt(50)
t.fd(30)
t.rt(20)
t.fd(30)
#t.lt(20)
#t.fd(30)
t.lt(40)
t.fd(5)
t.rt(20)
t.fd(30)
t.lt(32)
#back_len()
t.fd(100)
#
t.rt(5)
t.fd(80)
t.rt(10)
t.fd(45)
t.lt(5)
t.fd(25)
t.rt(27)
t.fd(30)
t.rt(10)
t.fd(5)
#body_done()
#
#tail_start()
#
t.lt(58)
t.fd(30)

t.circle(-70,130)
#t.fd(5)

t.circle(60,80)

t.rt(170)
t.fd(10)

t.circle(-60,80)

t.circle(60,130)

t.lt(100)
t.fd(20)

#t.penup()

t.goto(0,0)
t.goto(-120,50)
t.goto(-190,110)
t.goto(-280,150)


t.end_fill() 
#creating csm...
t.speed(10)
t.begin_fill()

t.lt(43)
t.fd(155)
t.lt(17)

#t.pendown()

t.fd(30)
t.lt(35)
t.fd(35)
t.rt(22)
t.fd(8)
#
#
t.rt(100)
t.fd(20)
t.rt(50)
t.fd(50)
#
#
t.lt(120)
t.fd(65)
t.lt(18)
#len()
t.fd(115)
#
t.lt(130)
t.fd(50)
#
t.rt(65)
t.fd(40)
#
t.lt(120)
t.fd(8)

t.rt(80)
t.fd(5)
#
t.rt(60)
#t.fd(8)
#
#back()
t.lt(30)
t.fd(10)
t.lt(15) 
t.fd(40)
t.lt(20)
t.fd(25)
t.lt(30)
t.fd(25)
#backdone()
#
t.rt(55)
t.fd(8)
t.lt(80)
t.fd(6)
t.rt(45)
t.fd(15)
#
#helmet()
t.rt(60)
t.fd(25)
t.lt(10)
t.fd(20)
#
t.rt(130)
t.fd(20)
t.rt(10)
t.fd(15)
t.lt(90)
t.fd(15)
t.lt(105)
t.fd(45)
t.rt(120)
t.fd(10)
t.rt(10)
t.fd(20)
t.lt(110)
t.fd(12)
t.lt(80)
t.fd(30)
#
#
t.rt(55)
t.fd(15)
t.lt(35)
t.fd(20)
t.lt(25)
#len()
t.fd(22)
#
t.lt(50)
t.fd(7)
t.rt(40)
t.fd(5)
t.lt(25)
t.fd(10)
t.lt(10)
t.fd(5)
#hel_Com()....
#
t.lt(25)
t.fd(10)
#nose()
t.lt(45)
t.fd(5)
t.rt(70)
t.fd(8)
#
t.lt(15)
t.fd(10)
#
t.lt(90)
t.fd(6)
#noseCom()....
#
t.rt(90)
t.fd(7)
t.lt(90)
t.fd(5)
t.rt(90)
t.fd(5)
t.rt(50)
t.fd(7)
#
#beardStart()
t.lt(45)
t.fd(8)
t.rt(15)
t.fd(12)
#
t.lt(140)
t.fd(10)
t.lt(2)
t.fd(15)
#com()
#
t.rt(95)
t.fd(8)
#shoulStart()....
t.rt(75)
t.fd(20)
#
#

t.lt(30)
t.fd(30)
#
t.lt(20)
t.fd(50)
#
t.rt(30)
t.fd(32)
#
t.rt(40)
t.fd(50)
t.fd(30)
#com()

#t.goto(0,0)
#t.goto(-120,50)
#t.goto(-190,110)
t.end_fill()
t.speed(8)
t.penup()
t.goto(-235,20)
t.pendown()
t.lt(90)
t.fd(15)
#t.lt(10)
t.circle(50,120)
t.lt(30)
t.fd(20)
t.lt(150)
t.circle(-50,120)





#end_prg
#

turtle.done()