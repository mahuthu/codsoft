import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = []
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line[:-1])
        for task in tasks:
            listbox_tasks.insert(tk.END, task)
    except:
        messagebox.showwarning(title="Warning!", message="Cannot find tasks.txt.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

window = tk.Tk()
window.title("To-Do List")

frame_tasks = tk.Frame(window)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

entry = tk.Entry(window, width=50)
entry.pack()

add_task_button = tk.Button(window, text="Add task", width=48, command=add_task)
add_task_button.pack()

delete_task_button = tk.Button(window, text="Delete task", width=48, command=delete_task)
delete_task_button.pack()

load_tasks_button = tk.Button(window, text="Load tasks", width=48, command=load_tasks)
load_tasks_button.pack()

save_tasks_button = tk.Button(window, text="Save tasks", width=48, command=save_tasks)
save_tasks_button.pack()

window.mainloop()

# Path: tasks.txt
# Clean room
# Wash dishes
# Learn Tkinter


