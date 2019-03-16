from tkinter import *
import re

class MiniCalc:
    def __init__(self,master):
        main=Frame(master,bg="Black")
        main.pack()

        self.lbl=Label(main,text="Enter a number: ",bg="Black",fg="White").grid(row=0,column=0)
        self.lbl=Label(main,text="Enter another number: ",bg="Black",fg="White").grid(row=1,column=0)

        self.ent1=Entry(main,bg="Black",fg="White").grid(row=0,column=1)
        self.ent2=Entry(main,bg="Black",fg="White").grid(row=1,column=1)

        self.but=Button(main,text="+",width=4,bg="Red",fg="Black",command=self.Add).grid(row=3,column=0)
        self.but=Button(main,text="-",width=4,bg="Red",fg="Black").grid(row=3,column=1)
        self.but=Button(main,text="/",width=4,bg="Red",fg="Black").grid(row=4,column=0)
        self.but=Button(main,text="x",width=4,bg="Red",fg="Black").grid(row=4,column=1)

        self.inp=self.ent1.get()
        self.inp2=self.ent2.get()

    def Add(self):
        inp=int(self.ent1.get())
        inp2=int(self.ent2.get())
        s=inp+inp2
        txt="Your Sum is: "+s
        lbl=Label(main,text=self.txt).grid(row=5,colspan=4)

root=Tk()
c=MiniCalc(root)
