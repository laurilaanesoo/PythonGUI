from tkinter import *

#akna seaded
aken = Tk()
aken.title('Tkinter "Hello World"')
aken.iconbitmap('pythongui.png')
aken.geometry("200x200")

tekst = Label(aken, text="Vastus", font="Tahoma 12", pady=10, padx=30)
tekst.grid(row=4,column=0)

#nupud
#nupp1 = Button(aken, text="Nupp1")
#nupp1.grid(row=0, column=1)
#nupp2 = Button(aken, text="Nupp2")
#nupp2.grid(row=0, column=0)
#nupp3 = Button(aken, text="Nupp3")
#nupp3.grid(row=1, column=0)

aken.mainloop()