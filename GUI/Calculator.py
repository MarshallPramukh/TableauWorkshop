from tkinter import *
main=Tk()

ent = Entry(main,width=25).grid(row=0,column=0,columnspan=4)
but = Button(main,text="7",height=2,width=4,bg="Black",fg="Red").grid(row=1,column=0)
but = Button(main,text="8",height=2,width=4,bg="Black",fg="Red").grid(row=1,column=1)
but = Button(main,text="9",height=2,width=4,bg="Black",fg="Red").grid(row=1,column=2)
but = Button(main,text="4",height=2,width=4,bg="Black",fg="Red").grid(row=2,column=0)
but = Button(main,text="5",height=2,width=4,bg="Black",fg="Red").grid(row=2,column=1)
but = Button(main,text="6",height=2,width=4,bg="Black",fg="Red").grid(row=2,column=2)
but = Button(main,text="1",height=2,width=4,bg="Black",fg="Red").grid(row=3,column=0)
but = Button(main,text="2",height=2,width=4,bg="Black",fg="Red").grid(row=3,column=1)
but = Button(main,text="3",height=2,width=4,bg="Black",fg="Red").grid(row=3,column=2)
but = Button(main,text="+",height=2,width=4,bg="Green2",fg="Black").grid(row=1,column=3)
but = Button(main,text="-",height=2,width=4,bg="Green2",fg="Black").grid(row=2,column=3)
but = Button(main,text="*",height=2,width=4,bg="Green2",fg="Black").grid(row=3,column=3)
but = Button(main,text="÷",height=2,width=4,bg="Green2",fg="Black").grid(row=4,column=3)
but = Button(main,text="=",height=2,width=15,bg="Red",fg="Black").grid(columnspan=3,row=4)
    

main.mainloop()
