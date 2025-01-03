from flask import Flask,render_template,url_for,request,redirect
from contextlib import contextmanager
import sqlite3

app=Flask(__name__)

@contextmanager
def db_connection():
    connection = sqlite3.connect("students.db")
    try:
        yield connection
    finally:
        connection.close()

@app.route("/")
def home():
    with db_connection() as conn:
        students = conn.execute("SELECT * FROM students;").fetchall()
    return render_template("home.html",students=students)


@app.route("/add_student",methods=["GET","POST"])
def add_student():
    if request.method =="POST":
        new_name = request.form['name']
        new_age= request.form['age']
        new_grade=request.form['grade']
        new_subjects=request.form['subjects']
        with db_connection() as conn:
            conn.execute(f"""
            INSERT INTO students (name,age,grade,subjects)
            VALUES ("{new_name}", "{new_age}", "{new_grade}","{new_subjects}");
            """)
            conn.commit()
            return redirect(url_for('home'))
    return render_template('add_student.html')

if __name__ == "__main__":
    app.run(debug = True)