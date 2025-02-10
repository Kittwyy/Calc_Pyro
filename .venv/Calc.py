import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        try:
            result = math.sqrt(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "You are Stupid, you broke Calculator")

def clear():
    entry.delete(0, tk.END)

def key_press(event):
    if event.char.isdigit() or event.char in "+-*/.":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "Escape":
        clear()

root = tk.Tk()
root.title("Taschenrechner")

entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# entry.bind("<Key>", key_press)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button in buttons:
    if button == '=':
        btn = ttk.Button(root, text=button, command=calculate)
    elif button == 'C':
        btn = ttk.Button(root, text=button, command=clear)
    else:
        btn = ttk.Button(root, text=button, command=lambda b=button: entry.insert(tk.END, b))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()