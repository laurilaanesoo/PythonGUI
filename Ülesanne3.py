from tkinter import *

#Aken
aken = Tk()
aken.resizable(0, 0)
aken.configure(background='black')
aken.iconbitmap('pythongui.png')


#Tekst
Label(aken, text="Nimi: Lauri Laanesoo", foreground="red", background="black", font="Tahoma 16 bold italic", pady=10, padx=30).pack()
Label(aken, text="Rühm: IT21", foreground="red", background="black", font="Tahoma 16 bold italic", pady=10, padx=30).pack()
Label(aken, text="2022", foreground="red", background="black", font="Tahoma 16 bold italic", pady=10, padx=30).pack()



aken.mainloop()