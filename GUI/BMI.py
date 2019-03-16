from tkinter import  *

class BMI:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.lbl=Label(frame,text="Check Your Body Mass Index !!",bg="Black",fg="Cyan")
        self.lbl.grid(row=0,column=1)

        self.het=Label(frame,text="Enter Height (in cms):",bg="Cyan")
        self.het.grid(row=1,column=0)

        self.wit=Label(frame,text="Enter Weight (in kg):",bg="Cyan")
        self.wit.grid(row=2,column=0)

        self.ent=Entry(frame)
        self.ent.grid(row=1,column=2)

        self.ent2=Entry(frame)
        self.ent2.grid(row=2,column=2)

        self.but=Button(frame,text="Click to check your BMI !!",command=self.chkbmi)
        self.but.grid(row=4,column=1)

    def chkbmi(self):
        inp=int(self.ent.get())
        inp2=int(self.ent2.get())

        inpx=inp/100 #converting height from mts to cms
        bmi=inp2/(inpx*inpx)

        if bmi < 18.5:
            print("Your Body Mass Index is: ",round(bmi,2)," and you are Underweight :(")
        elif bmi > 18.6 and bmi < 24.9:
            print("Your Body Mass Index is: ",round(bmi,2)," and you are Healthy :)")
        elif bmi > 25 and bmi < 29.9:
            print("Your Body Mass Index is: ",round(bmi,2)," and you are Overweight :(")
        elif bmi > 30 and bmi < 100:
            print("Your Body Mass Index is: ",round(bmi,2)," and you are Obese :((")
        else:
            print("Sorry !! Out of range")


root=Tk()
b=BMI(root)
root.mainloop()
