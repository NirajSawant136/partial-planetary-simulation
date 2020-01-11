# Partial simulation of gravity
# I have predifined a path (an ellipse) but the velocity (and even acceeleration) at each instant of time
# is decided by the distance between the star and respective planet (only gravitational force)
# This is PART 2 in my attempt to make a full simulation
# WORKING !!

import turtle
import math

space = turtle.Screen()
space.bgcolor('black')
space.title('Planetary Simulation - v2')
space.tracer(0)

planets = []
x = [200 , 300]
y = [0 , 300]
colors = ['skyblue', 'brown']
Mass = [1 , 18]
ellipse = [(200,100) , (300 , 150)]
for i in range(2):
        planets.append(turtle.Turtle())

for i in range(2):
        planets[i].color(colors[i])
        planets[i].shape('circle')
        planets[i].penup()
        planets[i].speed(0)
        planets[i].theta = 0
        planets[i].setx(x[i])
        planets[i].sety(y[i])
        planets[i].mass = Mass[i]
        
star = turtle.Turtle()
star.color('orange')
star.turtlesize(3)
star.shape('circle')
star.penup()


star.setx(math.sqrt(200**2 - 100**2) - 80)

while True:
        space.update()
       # planet.pendown()
        for i in range(2) :
                dis = math.sqrt((star.xcor() - planets[i].xcor())**2 + (star.ycor() - planets[i].ycor())**2)
                planets[i].setx(ellipse[i][0]*math.cos(math.radians(planets[i].theta)))
                planets[i].sety(ellipse[i][1]*math.sin(math.radians(planets[i].theta)))

                if(planets[i].ycor() == y[i] and planets[i].xcor() == x[i]) :
                        planets[i].theta = 0

                planets[i].theta += 10/dis
       
space.mainloop()
