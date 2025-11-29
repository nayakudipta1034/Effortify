import sqlite3
import os
from os.path import dirname

DB_FILE = os.path.join(os.path.dirname(__file__), "tasks.db")

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    return conn

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT CHECK(status IN ('TODO', 'DONE')) NOT NULL DEFAULT 'TODO',
            project_id INTEGER,
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
        )''')
        conn.commit()