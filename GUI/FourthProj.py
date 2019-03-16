from tkinter import *

gui=Tk()

def chk(event):
    inp=ent1.get()
    inp2=ent2.get()
    print("Successful")

lbl1=Label(gui,text="Login ID: ")
lbl2=Label(gui,text="Password: ")
lbl3=Label(gui)
ent1=Entry(gui)
ent2=Entry(gui)

lbl1.grid(row=0,sticky=E)
lbl2.grid(row=1,sticky=E)

ent1.grid(row=0,column=2)
ent2.grid(row=1,column=2)

chk=Checkbutton(gui,text="Keep me logged in")
chk.grid(columnspan=3)

but1=Button(gui,text="Click to Submit",command=chk)
but1.grid(row=5,column=1)

gui.mainloop()
