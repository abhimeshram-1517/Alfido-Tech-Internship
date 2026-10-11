from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "student-management-demo-key"

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "students.db"


# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Create the students table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home page: Display all students
@app.route("/")
def index():
    conn = get_db_connection()
    students = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("index.html", students=students)


# Add a student: GET displays the form; POST saves the data
@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not course:
            flash("Please fill in all fields.", "danger")
            return render_template("add_student.html")

        conn = get_db_connection()

        conn.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )

        conn.commit()
        conn.close()

        flash("Student added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_student.html")


# Edit an existing student
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    if student is None:
        conn.close()
        flash("Student not found.", "danger")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not course:
            conn.close()
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("edit_student", student_id=student_id))

        conn.execute(
            """
            UPDATE students
            SET name = ?, email = ?, course = ?
            WHERE id = ?
            """,
            (name, email, course, student_id)
        )

        conn.commit()
        conn.close()

        flash("Student updated successfully!", "success")
        return redirect(url_for("index"))

    conn.close()

    return render_template(
        "edit_student.html",
        student=student
    )


# Delete a student
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()

    flash("Student deleted successfully!", "success")
    return redirect(url_for("index"))


# Initialize the database before starting the server
init_db()


if __name__ == "__main__":
    app.run(debug=True)