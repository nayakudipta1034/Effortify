import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from rich.console import Console
from rich.table import Table
from prompt_toolkit import prompt
from backend.database import init_db
from backend.core import (
    create_project, delete_project, list_projects,
    add_task, complete_task, delete_task, get_tasks
)

console = Console()

def show_menu():
    console.rule("[bold green]Project & Task Manager[/]")
    console.print("[bold yellow]1.[/] Create Project")
    console.print("[bold yellow]2.[/] Delete Project")
    console.print("[bold yellow]3.[/] List Projects")
    console.print("[bold yellow]4.[/] Add Task")
    console.print("[bold yellow]5.[/] Complete Task")
    console.print("[bold yellow]6.[/] Delete Task")
    console.print("[bold yellow]7.[/] List Tasks for a Project")
    console.print("[bold yellow]8.[/] Exit")

def input_project_id():
    projects = list_projects()
    if not projects:
        console.print("⚠️ No projects found.")
        return None

    console.print("\n[bold cyan]Available Projects:[/]")
    for p in projects:
        console.print(f"{p['id']}: {p['name']}")
    pid = prompt("Enter project ID: ").strip()
    return int(pid) if pid.isdigit() else None

def input_task_id(project_id):
    tasks = get_tasks(project_id)
    if not tasks:
        console.print("⚠️ No tasks found.")
        return None

    console.print("\n[bold cyan]Tasks:[/]")
    for t in tasks:
        console.print(f"{t['id']}: [{t['status']}] {t['title']}")
    tid = prompt("Enter task ID: ").strip()
    return int(tid) if tid.isdigit() else None

def tui_loop():
    init_db()
    while True:
        show_menu()
        choice = prompt("\nChoose: ").strip()
        
        if choice == "1":
            name = prompt("Project name: ").strip()
            console.print(create_project(name))
        
        elif choice == "2":
            name = prompt("Project name to delete: ").strip()
            console.print(delete_project(name))

        elif choice == "3":
            projects = list_projects()
            table = Table(title="Projects")
            table.add_column("ID")
            table.add_column("Name")
            for p in projects:
                table.add_row(str(p["id"]), p["name"])
            console.print(table)

        elif choice == "4":
            pid = input_project_id()
            if pid:
                title = prompt("Task title: ").strip()
                console.print(add_task(title, pid))

        elif choice == "5":
            pid = input_project_id()
            if pid:
                tid = input_task_id(pid)
                if tid:
                    console.print(complete_task(tid))

        elif choice == "6":
            pid = input_project_id()
            if pid:
                tid = input_task_id(pid)
                if tid:
                    console.print(delete_task(tid))

        elif choice == "7":
            pid = input_project_id()
            if pid:
                tasks = get_tasks(pid)
                table = Table(title=f"Tasks in Project {pid}")
                table.add_column("ID")
                table.add_column("Title")
                table.add_column("Status")
                for t in tasks:
                    table.add_row(str(t["id"]), t["title"], t["status"])
                console.print(table)

        elif choice == "8":
            console.print("👋 Goodbye!")
            break

        else:
            console.print("❌ Invalid choice.")

        input("\n[Press Enter to continue]")
        console.clear()

if __name__ == "__main__":
    tui_loop()