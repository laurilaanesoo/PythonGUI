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
turtle.exitonclick()

#Kolmnurk

kolmnurkpikkus = int(input("Sisesta kolmnurga külgede pikkus: "))
kolmnurkvarv = input("Sisesta kolmnurga värv: ")

def kolmnurk(pikk):
    t = turtle.Turtle()
    for i in range(3):
        t.varvid(kolmnurkvarv)
        t.forward(kolmnurkpikkus)
        t.left(-120)
        
        
kolmnurk(kolmnurkpikkus)

turtle.exitonclick()
        
        