import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from backend.database import init_db
from backend.core import (
    create_project, delete_project, list_projects,
    add_task, complete_task, delete_task, get_tasks
)

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task & Project Manager")
        self.root.geometry("500x400")
        
        self.projects_listbox = tk.Listbox(root, height=10, width=40)
        self.projects_listbox.grid(row=0, column=0, padx=10, pady=10)
        
        self.tasks_listbox = tk.Listbox(root, height=10, width=40)
        self.tasks_listbox.grid(row=0, column=1, padx=10, pady=10)

        self.add_project_button = tk.Button(root, text="Add Project", command=self.add_project)
        self.add_project_button.grid(row=1, column=0, pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=1, pady=10)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.grid(row=2, column=1, pady=10)

        self.delete_project_button = tk.Button(root, text="Delete Project", command=self.delete_project)
        self.delete_project_button.grid(row=2, column=0, pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=3, column=1, pady=10)

        self.refresh_projects()
        self.projects_listbox.bind("<<ListboxSelect>>", self.on_project_select)

    def refresh_projects(self):
        self.projects_listbox.delete(0, tk.END)
        projects = list_projects()
        for project in projects:
            self.projects_listbox.insert(tk.END, project['name'])

    def on_project_select(self, event):
        selected_project_index = self.projects_listbox.curselection()
        if not selected_project_index:
            return
        selected_project_name = self.projects_listbox.get(selected_project_index)
        project = next(p for p in list_projects() if p['name'] == selected_project_name)
        self.refresh_tasks(project['id'])

    def refresh_tasks(self, project_id):
        self.tasks_listbox.delete(0, tk.END)
        tasks = get_tasks(project_id)
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task['title']} [{task['status']}]")

    def add_project(self):
        project_name = simpledialog.askstring("Input", "Enter project name:")
        if project_name:
            message = create_project(project_name)
            messagebox.showinfo("Info", message)
            self.refresh_projects()

    def add_task(self):
        selected_project_index = self.projects_listbox.curselection()
        if not selected_project_index:
            messagebox.showwarning("Warning", "Please select a project first.")
            return

        selected_project_name = self.projects_listbox.get(selected_project_index)
        project = next(p for p in list_projects() if p['name'] == selected_project_name)
        
        task_title = simpledialog.askstring("Input", "Enter task title:")
        if task_title:
            message = add_task(task_title, project['id'])
            messagebox.showinfo("Info", message)
            self.refresh_tasks(project['id'])

    def complete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task first.")
            return

        selected_task = self.tasks_listbox.get(selected_task_index)
        task_id = int(selected_task.split()[0])  # Assuming task ID is at the start
        message = complete_task(task_id)
        messagebox.showinfo("Info", message)
        self.refresh_tasks(task_id)

    def delete_project(self):
        selected_project_index = self.projects_listbox.curselection()
        if not selected_project_index:
            messagebox.showwarning("Warning", "Please select a project first.")
            return

        selected_project_name = self.projects_listbox.get(selected_project_index)
        message = delete_project(selected_project_name)
        messagebox.showinfo("Info", message)
        self.refresh_projects()

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Warning", "Please select a task first.")
            return

        selected_task = self.tasks_listbox.get(selected_task_index)
        task_id = int(selected_task.split()[0])  # Assuming task ID is at the start
        message = delete_task(task_id)
        messagebox.showinfo("Info", message)
        self.refresh_tasks(task_id)


if __name__ == '__main__':
    init_db()
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
