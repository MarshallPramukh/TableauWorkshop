from tkinter import *
root=Tk()

def lclick(event):
    print("Left")
def rclick(event):
    print("Right")

frm=Frame(root, height=500,width=500)
frm.bind("<Button-1>",lclick)
frm.bind("<Button-2>",rclick)

root.mainloop()
