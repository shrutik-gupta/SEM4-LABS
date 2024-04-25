from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
root.config(bg="pink")

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20), bg="hotpink")
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)
entry_1 = Entry(root)
entry_1.place(x=280, y=130, width=135, height=22)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=80, y=180)
entry_2 = Entry(root)
entry_2.place(x=280, y=180, width=135, height=22)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=80, y=230)
var = IntVar()
rb1=Radiobutton(root, text="Male", padx=1, variable=var, value=1)
rb1.place(x=280, y=230)
rb2=Radiobutton(root, text="Female", padx=1, variable=var, value=2)
rb2.place(x=350, y=230)

label_4 = Label(root, text="Age:", width=20, font=("bold", 10))
label_4.place(x=80, y=280)
entry_3 = Entry(root)
entry_3.place(x=280, y=280, width=135, height=22)

def submit():
    messagebox.showinfo(title="Successful Login!",message="You have logged in successfully!")
b1 = Button(root, text='Submit', width=20, bg='brown', fg='white', command=submit, cursor="hand2")
b1.place(x=180, y=350, height=25, width=135)

root.mainloop()
