######################################################################
# Author: Jenifer Fidelia
# Username: Fideliaj
#

# Assignment: A02: Exploring Turtles in Python
# Purpose: Practice using turtles and loops
######################################################################
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle

#make window and add attributes
window = turtle.Screen()
window.bgcolor("LemonChiffon")

#make turtles
tess=turtle.Turtle()
carol=turtle.Turtle()
nic=turtle.Turtle()
lisa=turtle.Turtle()
mary=turtle.Turtle

#defining functions:
    #building blocks: diamond (size)
    # fullcircle (radius)

def circle (t,radius):
    t.pencolor ("darkgreen")
    t.speed (10)

    t.left(45)
    t.circle(radius)


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

carol.penup()
carol.forward(90)
carol.pendown()
carol.pencolor("darkgreen")
carol.pensize (2)
circle(carol,-10)

nic.penup()
nic.forward(-90)
nic.pendown()
nic.pencolor("darkgreen")
nic.pensize (2)
circle(nic,10)

lisa.penup()
lisa.left(90)
lisa.forward(90)
lisa.right(90)
lisa.forward(90)
lisa.pendown()
lisa.pencolor("darkgreen")
circle(lisa,10)

mary.penup()
mary.left(-90)
# lisa.forward(-90)
# lisa.right(-90)
# lisa.forward(90)
# lisa.pendown()
# lisa.pencolor("darkgreen")
# circle(lisa,10)



window.exitonclick()








