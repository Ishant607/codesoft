import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

def add_task():
    task_text = simpledialog.askstring("Add Task", "Enter the new task:")
    if task_text:
        tasks.append({"task": task_text, "completed": False})
        refresh_tasks()

def mark_completed():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")
        return
    idx = selected[0]
    tasks[idx]["completed"] = True
    refresh_tasks()

def update_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to update.")
        return
    idx = selected[0]
    new_task = simpledialog.askstring("Update Task", "Enter the new task description:")
    if new_task:
        tasks[idx]["task"] = new_task
        refresh_tasks()

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
    if confirm:
        idx = selected[0]
        tasks.pop(idx)
        refresh_tasks()

# Create main window
root = tk.Tk()
root.title("To-Do List App")

# Create listbox to show tasks
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_btn = tk.Button(button_frame, text="Add Task", width=15, command=add_task)
add_btn.grid(row=0, column=0, padx=5, pady=5)

update_btn = tk.Button(button_frame, text="Update Task", width=15, command=update_task)
update_btn.grid(row=0, column=1, padx=5, pady=5)

complete_btn = tk.Button(button_frame, text="Mark Completed", width=15, command=mark_completed)
complete_btn.grid(row=0, column=2, padx=5, pady=5)

delete_btn = tk.Button(button_frame, text="Delete Task", width=15, command=delete_task)
delete_btn.grid(row=0, column=3, padx=5, pady=5)

# Start with empty list
refresh_tasks()

# Run app
root.mainloop()
