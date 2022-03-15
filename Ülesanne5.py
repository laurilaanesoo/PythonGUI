from tkinter import *
import tkinter.ttk

aken = Tk()
aken.title('Nupud')

aken.geometry("300x200")

#funktsioonid
def naita_valikut():
    print(var.get())

#valikukast
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20)
valikukast.grid(row=2,column=1)


#sildid
silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=0,column=0)

silt2 = Label(aken, text="Käibemaksumäär")
silt2.grid(row=1,column=0)

valjund = Label(aken, text="Käibemaks: ")
valjund.grid(row=7,column=0)

valjund2 = Label(aken, text="Hind käibemaksuga: ")
valjund2.grid(row=8,columnspan=1)

valjund4 = Label(aken, text="")
valjund4.grid(row=7,column=1)

valjund5= Label(aken, text="")
valjund5.grid(row=8,column=1)


#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)


#funktsioonid
def arvutamine():
    global kokku
    global protsent
    kokku = int(sisestus.get())
    protsent = int(var.get())
    kaibemaks = (kokku/100*protsent)
    hind = kokku + kaibemaks
    valjund4.config(text=f"{kaibemaks}€")
    valjund5.config(text=f"{hind}€")
    
    
#nupud
nupp1 = Button(aken, text="OK", width=10, command=arvutamine)
nupp1.grid(row=16, column=2)

    
aken.mainloop()