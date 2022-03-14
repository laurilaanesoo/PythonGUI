#Ülesanne 1
#Lauri Laanesoo
#14.03.2022


import turtle
import random

#aken
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanne 1")

varvid =('red','blue','orange','green')
poora = 0


for i in range(8):
    k1 = turtle.Turtle()
    k1.speed(5)
    k1.color(random.choice(varvid))
    k1.left(poora)
    k1.forward(100)
    poora+=45

turtle.exitonclick()
