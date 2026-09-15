from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)
DB = "tasks.db"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/api/tasks")
def list_tasks():
    conn = get_db()
    tasks = [dict(row) for row in conn.execute(
        "SELECT id, title, completed FROM tasks ORDER BY id DESC"
    )]
    conn.close()
    return jsonify(tasks)

@app.post("/api/tasks")
def add_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify(error="Task title is required"), 400

    conn = get_db()
    cur = conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    task = dict(conn.execute(
        "SELECT id, title, completed FROM tasks WHERE id = ?", (cur.lastrowid,)
    ).fetchone())
    conn.close()
    return jsonify(task), 201

@app.patch("/api/tasks/<int:task_id>")
def toggle_task(task_id):
    conn = get_db()
    row = conn.execute(
        "SELECT completed FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    if row is None:
        conn.close()
        return jsonify(error="Task not found"), 404

    new_value = 0 if row["completed"] else 1
    conn.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?", (new_value, task_id)
    )
    conn.commit()
    task = dict(conn.execute(
        "SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,)
    ).fetchone())
    conn.close()
    return jsonify(task)

@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    conn = get_db()
    cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        return jsonify(error="Task not found"), 404
    return "", 204

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
