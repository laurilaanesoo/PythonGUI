#Ülesanne2
#Lauri Laanesoo
#15.03.2022

import turtle

#aken
aken = turtle.Screen()
aken.setup(300,300)

def viisnurk(pikkus):
    t = turtle.Turtle()
    for x in range(5):
        t.forward(108)
        t.left(-144)
        
viisnurk(100)


varvid =('red','blue','orange','green')
def kolmnurk(pikk, varvid):
    t = turtle.Turtle()
    for i in range(3):
        t.color(varvid)
        t.forward(pikk)
        t.left(-120)
        

kolmnurkpikkus = int(input("Sisesta kolmnurga külgede pikkus: "))
kolmnurkvarv = input("Sisesta kolmnurga värv: ")
kolmnurk(kolmnurkpikkus,kolmnurkvarv)

turtle.exitonclick()
