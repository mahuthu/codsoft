import tkinter as tk
from tkinter import messagebox


def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result["text"] = result
    except:
        messagebox.showwarning(title="Warning!", message="You must enter two numbers.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        label_result["text"] = result
    except:
        messagebox.showwarning(title="Warning!", message="You must enter two numbers.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label_result["text"] = result
    except:
        messagebox.showwarning(title="Warning!", message="You must enter two numbers.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        label_result["text"] = result
    except:
        messagebox.showwarning(title="Warning!", message="You must enter two numbers.")




window = tk.Tk()
window.title("Calculator")


frame1 = tk.Frame(window)
frame1.pack()

entry1 = tk.Entry(frame1, width=10)
entry1.pack(side=tk.LEFT)


entry2 = tk.Entry(frame1, width=10)
entry2.pack(side=tk.LEFT)

label_equal = tk.Label(frame1, text="=")
label_equal.pack(side=tk.LEFT)

label_result = tk.Label(frame1, text="")
label_result.pack(side=tk.LEFT)

frame2 = tk.Frame(window)
frame2.pack()

button_add = tk.Button(frame2, text="+", width=10, command=add)
button_add.pack(side=tk.LEFT)

button_subtract = tk.Button(frame2, text="-", width=10, command=subtract)
button_subtract.pack(side=tk.LEFT)

button_multiply = tk.Button(frame2, text="*", width=10, command=multiply)
button_multiply.pack(side=tk.LEFT)

button_divide = tk.Button(frame2, text="/", width=10, command=divide)
button_divide.pack(side=tk.LEFT)




window.mainloop()



