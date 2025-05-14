import tkinter as tk
from tkinter import messagebox

# Set up the main window
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x450")
root.resizable(False, False)

tasks = []

# Function to update listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Add new task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        tasks.remove(task)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Set up the input field
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_btn = tk.Button(button_frame, text="Add Task", width=15, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

# Listbox to show tasks
listbox = tk.Listbox(root, width=40, height=15, font=('Arial', 12), selectbackground="lightblue")
listbox.pack(pady=20)

# Run the app
root.mainloop()
