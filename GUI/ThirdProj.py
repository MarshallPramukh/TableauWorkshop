from tkinter import *
root=Tk()
lbl1=Label(root,text="First Label",bg="black",fg="red")
lbl1.pack()
lbl2=Label(root,text="Second Text",bg="red",fg="black")
lbl2.pack(fill=X)
lbl3=Label(root,text="Third Text",bg="black",fg="white")
lbl3.pack(side=LEFT,fill=Y)
root.mainloop()
