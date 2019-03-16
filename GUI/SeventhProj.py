from tkinter import *

class Login:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.lbl=Label(frame,text="Username: ",bg="Black",fg="White")
        self.lbl.grid(row=0,column=0)

        self.lbl2=Label(frame,text="Password",bg="Black",fg="White")
        self.lbl2.grid(row=1,column=0)

        self.ent=Entry(frame)
        self.ent.grid(row=0,column=2)

        self.ent2=Entry(frame)
        self.ent2.grid(row=1,column=2)

        self.but=Button(frame,text="Login",command=self.Login)
        self.but.grid(row=3,column=1)

        self.but2=Button(frame,text="Quit",command=frame.quit)
        self.but2.grid(row=3,column=2)

        self.chk=Checkbutton(frame,text="Keep me logged in")
        self.chk.grid(row=2,column=1)

    def Login(self):
        inp=self.ent.get()
        inp2=self.ent2.get()

        if inp=="Pramukh" and inp2=="Marshall":
            print("Login Successful !!")
            exit()
        elif inp=="Marshall" and inp2=="Pramukh":
            print("Login Successful !!")
            exit()
        elif inp=="marshall"and inp2=="pramukh":
            print("Login Successful !!")
            exit()
        elif inp=="pramukh" and inp2=="marshall":
            print("Login Successful !!")
            exit()
        else:
            print("Login Unsuccessful !!")
            exit()
            
root=Tk()
t=Login(root)
root.mainloop()
