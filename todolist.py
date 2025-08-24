import tkinter as tk
from tkinter import messagebox

# ---------------- To-Do App ----------------
def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# ---------------- GUI ----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="lightblue")

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", command=add_task, width=12, bg="lightgreen")
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", command=delete_task, width=12, bg="tomato")
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(frame, text="Clear All", command=clear_all, width=12, bg="orange")
clear_btn.grid(row=0, column=2, padx=5)

save_btn = tk.Button(root, text="Save Tasks", command=save_tasks, width=40, bg="yellow")
save_btn.pack(pady=5)

# Task list
listbox = tk.Listbox(root, font=("Arial", 14), height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Load saved tasks
load_tasks()

root.mainloop()
