from tkinter import *

class myBut:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printBut = Button(frame,text="Print",command=self.printMsg)
        self.printBut.pack(side=LEFT)

        self.quitBut = Button(frame,text="Quit",command=frame.quit)
        self.quitBut.pack(side=LEFT)
    def printMsg(self):
        print("This thing works !!!")

root=Tk()
b=myBut(root)
root.mainloop()
