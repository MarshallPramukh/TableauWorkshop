from tkinter import *
rt = Tk()
tFrame=Frame(rt)
tFrame.pack()
bFrame=Frame(rt)
bFrame.pack(side=BOTTOM)

but1=Button(tFrame, text="Button 1", bg="black",fg="white")
but2=Button(tFrame, text="Button 2", bg="black",fg="white")
but3=Button(tFrame, text="Button 3", bg="black",fg="white")
but4=Button(bFrame, text="Button 4", bg="white",fg="black")

but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=BOTTOM)
rt.mainloop()
