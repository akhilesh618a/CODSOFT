from tkinter import *
from tkinter import messagebox, filedialog
import os

# ---------- Core Functions ----------

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def mark_done():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(END, f" {task}")
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to mark as done.")

def save_tasks():
    tasks = task_listbox.get(0, END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        messagebox.showinfo("Saved", "Tasks saved successfully.")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path and os.path.isfile(file_path):
        task_listbox.delete(0, END)
        with open(file_path, 'r') as file:
            for line in file:
                task_listbox.insert(END, line.strip())

# ---------- GUI Setup ----------

root = Tk()
root.title("College To-Do List")
root.geometry("450x550")
root.config(bg="#f7f1e3")

title = Label(root, text="📘 College To-Do List", font=("Helvetica", 20, "bold"), bg="#f7f1e3", fg="#2c3e50")
title.pack(pady=10)

task_entry = Entry(root, font=("Helvetica", 14), bd=4, relief=SUNKEN)
task_entry.pack(pady=10, padx=20, fill=X)

btn_frame = Frame(root, bg="#f7f1e3")
btn_frame.pack(pady=5)

Button(btn_frame, text="Add Task", font=("Helvetica", 12), bg="#58B19F", fg="white", command=add_task).pack(side=LEFT, padx=5)
Button(btn_frame, text="Mark Done", font=("Helvetica", 12), bg="#3B3B98", fg="white", command=mark_done).pack(side=LEFT, padx=5)
Button(btn_frame, text="Delete Task", font=("Helvetica", 12), bg="#B33771", fg="white", command=delete_task).pack(side=LEFT, padx=5)

task_listbox = Listbox(root, font=("Helvetica", 14), height=15, bd=3, relief=SUNKEN, selectbackground="#f8c291")
task_listbox.pack(padx=20, pady=20, fill=BOTH, expand=True)

bottom_frame = Frame(root, bg="#f7f1e3")
bottom_frame.pack(pady=5)

Button(bottom_frame, text=" Save Tasks", font=("Helvetica", 12), bg="#f19066", fg="white", command=save_tasks).pack(side=LEFT, padx=10)
Button(bottom_frame, text=" Load Tasks", font=("Helvetica", 12), bg="#e77f67", fg="white", command=load_tasks).pack(side=LEFT, padx=10)

root.mainloop()
