from tkinter import *

#akna seaded
aken = Tk()
aken.title('Tkinter "Hello World"')
aken.iconbitmap('pythongui.png')
aken.geometry("200x200")

tekst = Label(aken, text="Siia kunagi vastus1", font="Tahoma 12", pady=10, padx=30)
tekst.grid(row=0, columnspan=4)

#nupud
nupp1 = Button(aken, text="7", width=4, padx=2)
nupp1.grid(row=1, column=0, padx=2)
nupp2 = Button(aken, text="8")
nupp2.grid(row=1, column=1)
nupp3 = Button(aken, text="9")
nupp3.grid(row=1, column=2)
nupp3 = Button(aken, text="/")
nupp3.grid(row=1, column=3)

aken.mainloop()
