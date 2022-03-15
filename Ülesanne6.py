from tkinter import *

#akna seaded
aken = Tk()
aken.title('Lipu joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine

louend.create_rectangle(15, 20, 200, 120,fill='red')
louend.create_line(15, 70, 200, 70,fill='white',width=15)
louend.create_line(90, 20, 90, 120,fill='white',width=15)


#pildi lisamine
minu_pilt = PhotoImage(file='taani.png')
louend.create_image(150, 150, anchor=NW, image=minu_pilt)

aken.mainloop()