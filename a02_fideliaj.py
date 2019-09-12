######################################################################
# Author: Jenifer Fidelia
# Username: Fideliaj
#

# Assignment: A02: Exploring Turtles in Python
# Purpose: Practice using turtles and loops. Drawing A Turtle
######################################################################
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################


#P.S: I AM GOING TO DRAW A TURTLE

import turtle

#make window and add attributes
window = turtle.Screen()
window.bgcolor("LemonChiffon")

#make turtles
tess=turtle.Turtle()
carol=turtle.Turtle()
nic=turtle.Turtle()
lisa=turtle.Turtle()
mary=turtle.Turtle()

#defining functions:

# making circle (radius)

def circle (t,radius):
    t.pencolor ("darkgreen")
    t.speed (10)

    t.left(45)
    t.circle(radius)

#making the diamond shell of the turtle (size)

def diamond (t , size):
    t.pensize(2)
    t.pencolor("darkgreen")
    t.speed(10)

    t.left (90)
    t.penup()
    t.forward(size)
    t.right(135)
    t.pendown()
    for i in range (4):
        t.forward (size)
        t.right(90)

diamond (tess, 100)
circle(tess, -72)

#making the turtle's shell/body and head
tess.left (90)
tess.penup()
tess.forward (17)
tess.left (45)
tess.pendown()
circle(tess,(90))
tess.right (90)
tess.penup()
tess.forward(25)
tess.pendown()

diamond(tess,33)

#making the little circle 1/ the first feet

carol.penup()
carol.forward(90)
carol.pendown()
carol.pencolor("darkgreen")
carol.pensize (2)
circle(carol,-10)

#making the little circle 2/ the second feet

nic.penup()
nic.forward(-90)
nic.pendown()
nic.pencolor("darkgreen")
nic.pensize (2)
circle(nic,10)

#making the little circle 3/ the third feet

lisa.pensize(2)
lisa.penup()
lisa.left(90)
lisa.forward(90)
lisa.right(90)
lisa.forward(90)
lisa.pendown()
lisa.pencolor("darkgreen")
circle(lisa,10)

#making the little circle 4/ the fourth feet

mary.penup()
mary.pensize(2)
mary.pencolor("darkgreen")
mary.forward(-90)
mary.left(90)
mary.forward(90)
mary.pendown()
circle(mary,10)


#hide the turtles so they wont show on the picture
mary.hideturtle()
lisa.hideturtle()
nic.hideturtle()
carol.hideturtle()
tess.hideturtle()


window.exitonclick()








