import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("To-Do")

task=tk.StringVar()
task_entry=tk.Entry(root, textvariable=task, font=("Times New Roman", 10), width=45)
task_entry.pack(padx=5, pady=5)

def add():
    listbox_todo.insert(tk.END, task.get())

add_task=tk.Button(root, text="Add Task", font=("Times New Roman", 10), command=add)
add_task.pack( padx=10, pady=10)

listbox_todo=tk.Listbox(root, height=12, width=45)
listbox_todo.pack(padx=20, pady=20)

def delete():
    try:
        selected=listbox_todo.curselection()
        listbox_todo.delete(selected)
    except:
        messagebox.showwarning("showwarning","No task selected!")

delete_task=tk.Button(root, text="Delete Task", font=("Times New Roman", 10), command=delete)
delete_task.pack( padx=10, pady=10)

def save(*args):
    with open (r"C:\Users\Josias Rabe\tasks.txt", "a") as file:
        items=list(listbox_todo.get(0, tk.END))
        for task in items:
            file.write(task+ "\n")
 
save_tasks=tk.Button(root, text="Save Tasks", font=("Times New Roman", 10), command=save)
save_tasks.pack( padx=10, pady=10)

def load(*args):
    try:
        with open (r"C:\Users\Josias Rabe\tasks.txt", "r") as file:
            for line in file.readlines():
                listbox_todo.insert(tk.END, line)
    except:
        messagebox.showinfo("showinfo", "Task list is empty!")

load_tasks=tk.Button(root, text="Load Tasks", font=("Times New Roman", 10), command=load)
load_tasks.pack( padx=10, pady=10)

root.mainloop()
