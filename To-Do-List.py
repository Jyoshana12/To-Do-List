
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:  # only delete if an item is selected
        listbox.delete(selected[0])

# Window
win = tk.Tk()
win.title("To-Do List")

entry = tk.Entry(win, width=30, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(win, text="Add Task", command=add_task).pack(pady=5)
tk.Button(win, text="Delete Task", command=delete_task).pack(pady=5)

listbox = tk.Listbox(win, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

win.mainloop()
