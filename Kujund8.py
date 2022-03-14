#Kujund nr 8
#Lauri Laanesoo
#14.03.2022

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)

def joonista_ruut(pikkus):
    t = turtle.Turtle()
    for x in range(4):
        
        t.forward(pikkus)
        t.left(45)
        t.forward(pikkus)
        t.right(90)
        t.forward(pikkus)
        t.left(45)
        t.forward(pikkus)
        t.right(90)
    

joonista_ruut(20)

