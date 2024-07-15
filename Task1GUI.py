#TASK1-SimpleGUI TO-DO List
import tkinter as tk
from tkinter import simpledialog
root = tk.Tk()
root.geometry("500x500")
root.title("To-Do List")
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)

    def list_tasks(self):
        return self.tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = ToDoList()
        self.heading_label = tk.Label(root, text="To-Do List", font=("Times New Roman", 16), bd=2, relief="solid", padx=165, pady=3)
        self.heading_label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=70, height=21)
        self.task_listbox.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_task_done)
        self.done_button.pack(pady=5)

        self.refresh_tasks()

    def add_task(self):
        task =simpledialog.askstring("Add Task", "Enter a task:")
        if task:
            self.todo_list.add_task(task)
            self.refresh_tasks()

    def mark_task_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_number = selected_task_index[0]
            self.todo_list.delete_task(task_number)
            self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.todo_list.list_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = ToDoApp(root)
    root.mainloop()
