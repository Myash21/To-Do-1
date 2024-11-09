# Todo App

A simple Todo application built with Flask and SQLAlchemy to help manage tasks. This app allows users to create, update, and delete tasks.

## Features

- **Add Todo**: Add a new todo item with a title and incomplete status.
- **View Todo List**: View all existing todos.
- **Update Todo Status**: Mark a todo as complete or incomplete.
- **Delete Todo**: Remove a todo from the list.

## Prerequisites

- **Python 3.x** (if running locally)
- **Docker** (if running in a Docker container)

## Installation

### Option 1: Running with Docker (Recommended)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Myash21/To-Do-1.git
   cd todo-app

2. **Build the Docker Image**:
   
   ```bash
   docker build -t flask-todo-app .

3. **Run the Docker Container**:

    ```bash
   docker run -p 5000:5000 flask-todo-app
4. **Access the Application**:
   Open your web browser and go to http://localhost:5000 to access the app.

### Option 2: Running Locally  
   
1. **Clone the repository**:

   ```bash
   git clone https://github.com/Myash21/To-Do-1.git
   cd todo-app

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**

   ```bash
   pip install Flask Flask-SQLAlchemy

4. **Run the application:**

   ```bash
   python app.py

5. **Open your browser and go to http://127.0.0.1:5000 to access the app.**

## Technologies Used
  1. **Flask**: For the web framework.
  2. **Flask-SQLAlchemy**: For ORM and SQLite database management.
  3. **Semantic UI**: For basic styling of the UI.
