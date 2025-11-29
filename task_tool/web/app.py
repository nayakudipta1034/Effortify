import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from flask import Flask, render_template, request, redirect, url_for, flash
from backend.database import init_db
from backend.core import (
    create_project, delete_project, list_projects,
    add_task, complete_task, delete_task, get_tasks
)

app = Flask(__name__)
app.secret_key = "naira_super_secret_key"  # Change if needed

init_db()

@app.route('/')
def home():
    projects = list_projects()
    return render_template("index.html", projects=projects)

@app.route('/project/<int:pid>')
def view_project(pid):
    projects = list_projects()
    tasks = get_tasks(pid)
    return render_template("project.html", pid=pid, tasks=tasks, projects=projects)

@app.route('/create_project', methods=['POST'])
def create_project_route():
    name = request.form.get("name")
    msg = create_project(name)
    flash(msg)
    return redirect(url_for("home"))

@app.route('/delete_project/<name>')
def delete_project_route(name):
    msg = delete_project(name)
    flash(msg)
    return redirect(url_for("home"))

@app.route('/add_task/<int:pid>', methods=['POST'])
def add_task_route(pid):
    title = request.form.get("title")
    msg = add_task(title, pid)
    flash(msg)
    return redirect(url_for("view_project", pid=pid))

@app.route('/complete_task/<int:pid>/<int:tid>')
def complete_task_route(pid, tid):
    msg = complete_task(tid)
    flash(msg)
    return redirect(url_for("view_project", pid=pid))

@app.route('/delete_task/<int:pid>/<int:tid>')
def delete_task_route(pid, tid):
    msg = delete_task(tid)
    flash(msg)
    return redirect(url_for("view_project", pid=pid))

if __name__ == '__main__':
    app.run(debug=True)