# Project and Task Management Tool

A fully functional **Project & Task Management Tool** built using **Python**. It includes a **Terminal TUI**, a **Web App (Flask)**, and a **Desktop GUI (Tkinter)** to manage projects and tasks seamlessly.

## Features

- **Create, delete, and list projects**
- **Add, delete, and complete tasks**
- **TUI (Text User Interface)** for terminal-based operations
- **Web app (Flask)** with Bootstrap for a responsive UI
- **Desktop GUI (Tkinter)** for a native experience

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone this repository** (or download the code):

   ```bash
   git clone https://github.com/your-username/task-tool.git
   cd task-tool

2. ## INSTALL DEPENDENCIES:
   ```bash
   pip install -r requirements.txt

3. ## Set up the database:
   You don’t need to do this manually. The database will be initialized automatically the first time you run the app.

## FILE STRUCTURE:
task_tool/
├── backend/            # Backend logic: database & core functions
│   ├── core.py         # Functions for project and task management
│   └── database.py     # SQLite database handling
├── tui/                # Terminal-based User Interface
│   └── main.py         # Main script for TUI
├── web/                # Flask Web Application
│   ├── app.py          # Flask app to run the web server
│   ├── templates/      # HTML templates for the web pages
│   └── static/         # Static files (CSS, images, etc.)
├── gui/                # Tkinter Desktop GUI
│   └── app.py          # Tkinter-based app for desktop interface
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (you are here!)

## Database Structure:
The application uses SQLite to store project and task data.

Projects table: Stores project names and unique IDs.

Tasks table: Stores task details, including title, project ID, and status.

## Contributing:
Feel free to fork the repository, make improvements, or fix bugs. To contribute:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Make your changes and commit them (git commit -am 'Add new feature').

4. Push to the branch (git push origin feature-branch).

5. Open a pull request.

## Credits
1. Flask for the web framework.

2. Tkinter for the desktop GUI.

3. SQLite for the database.
`