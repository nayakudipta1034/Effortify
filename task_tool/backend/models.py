from backend.database import get_connection

class Project:
    def __init__(self, name):
        self.name = name
        
    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO projects (name) VALUES (?)", (self.name))
            conn.commit()
            
    @staticmethod
    def delete(name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM projects WHERE name = ?", (name))
            conn.commit()
    
    @staticmethod
    def all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM projects")
            return cursor.fetchall()

class Task:
    def __init__(self, title, project_id):
        self.title = title
        self.project_id = project_id
    
    def save(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (title, project_id) VALUES (?, ?)", (self.title, self.project_id))
            conn.commit()
            
    @staticmethod
    def complete(task_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = 'DONE' WHERE id = ?", (task_id,))
            conn.commit()
            
    @staticmethod
    def delete(task_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id, ))
            conn.commit()
            
    @staticmethod
    def by_project(project_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id, ))
            return cursor.fetchall()

