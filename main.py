

from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.security import APIKeyHeader
from typing import Optional
import sqlite3

app = FastAPI(title="Student Record Management API")

API_KEY = "rajitha123"


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)

def verify_api_key(x_api_key: str = Depends(api_key_header)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )
    return x_api_key


def setup_database():
    connection = sqlite3.connect("students.db")
    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

setup_database()

@app.get("/")
def home():
    return {"message": "Student API is working!"}

@app.post("/students", dependencies=[Depends(verify_api_key)])
def add_student(name: str, age: int, course: str):
    connection = sqlite3.connect("students.db")
    cursor = connection.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    connection.commit()
    student_id = cursor.lastrowid
    connection.close()
    return {"id": student_id, "name": name, "age": age, "course": course}

@app.get("/students", dependencies=[Depends(verify_api_key)])
def get_students():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    rows = connection.execute("SELECT * FROM students").fetchall()
    result = [dict(row) for row in rows]
    connection.close()
    return result

@app.delete("/students/{student_id}", dependencies=[Depends(verify_api_key)])
def delete_student(student_id: int):
    connection = sqlite3.connect("students.db")
    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?", (student_id,)
    )
    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    return {"message": "Student deleted successfully"}

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, course: str):
    connection = sqlite3.connect("students.db")
    cursor = connection.execute(
        "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )
    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    return {
        "message": "Student updated successfully",
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int, course: str):
    connection = sqlite3.connect("students.db")
    cursor = connection.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, student_id)
    )
    connection.commit()
    connection.close()

    if cursor.rowcount == 0:
        return {"message": "Student not found"}

    return {"message": "Student updated successfully"}
