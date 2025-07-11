from tkinter import *
from random import randint


root = Tk()
root.title('Strong Password Generator')
root.geometry("500x300")


def new_rand():
    pw_entry.delete(0, END)  
    password = ''
    try:
        length = int(my_entry.get())
        for _ in range(length):
            password += chr(randint(33, 126))  
        pw_entry.insert(0, password)
    except ValueError:
        pw_entry.insert(0, "Enter a valid number")


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)


my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)


pw_entry = Entry(root, font=("Helvetica", 24), width=24)
pw_entry.pack(pady=20)


my_frame = Frame(root)
my_frame.pack(pady=20)


my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()