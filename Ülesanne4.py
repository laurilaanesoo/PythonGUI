from tkinter import *

#akna seaded
aken = Tk()
aken.title('Tkinter "Hello World"')
aken.iconbitmap('pythongui.png')
aken.geometry("200x200")

#Tekst
tekst = Label(aken, text="Siia kunagi vastus!", font="Tahoma 12", pady=10, padx=30)
tekst.grid(row=0, columnspan=4)

#nupud
nupp1 = Button(aken, text="7", width=5, padx=2)
nupp1.grid(row=1, column=0)

nupp2 = Button(aken, text="8", width=5, padx=2)
nupp2.grid(row=1, column=1)

nupp3 = Button(aken, text="9", width=5, padx=2)
nupp3.grid(row=1, column=2)

nupp3 = Button(aken, text="/", width=5, padx=2)
nupp3.grid(row=1, column=3)

nupp4 = Button(aken, text="*", width=5, padx=2)
nupp4.grid(row=2, column=3, pady=2)

nupp5 = Button(aken, text="6", width=5, padx=2)
nupp5.grid(row=2, column=2, pady=2)

nupp6 = Button(aken, text="5", width=5, padx=2)
nupp6.grid(row=2, column=1, pady=2)

nupp7 = Button(aken, text="4", width=5, padx=2)
nupp7.grid(row=2, column=0, pady=2)

nupp8 = Button(aken, text="-", width=5, padx=2)
nupp8.grid(row=3, column=3, pady=2)

nupp9 = Button(aken, text="3", width=5, padx=2)
nupp9.grid(row=3, column=2, pady=2)

nupp10 = Button(aken, text="2", width=5, padx=2)
nupp10.grid(row=3, column=1, pady=2)

nupp11 = Button(aken, text="1", width=5, padx=2)
nupp11.grid(row=3, column=0, pady=2)

nupp12 = Button(aken, text="+", width=5, padx=2)
nupp12.grid(row=4, column=3, pady=2)

nupp13 = Button(aken, text="=", width=5, padx=2)
nupp13.grid(row=4, column=2, pady=2)

nupp14 = Button(aken, text=",", width=5, padx=2)
nupp14.grid(row=4, column=1, pady=2)

nupp15 = Button(aken, text="0", width=5, padx=2)
nupp15.grid(row=4, column=0, pady=2)

aken.mainloop()
