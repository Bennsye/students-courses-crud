# Students & Courses CRUD App

This is a **simple FastAPI CRUD application** with SQLite for managing **Students**, **Courses**, and **Enrollments**.  
It demonstrates a full backend workflow with relational data, including one-to-many and many-to-many relationships.

---

## 🛠 Features

- Create, Read, Update, Delete (CRUD) operations for:
  - **Students** (name, email, age)
  - **Courses** (title, description)
  - **Enrollments** (linking students to courses)
- Interactive **Swagger UI** documentation for testing API endpoints
- SQLite database (`students_courses.db`) stored locally
- Clean project structure using SQLAlchemy models, Pydantic schemas, and separate CRUD functions

---

## 📦 Requirements

- Python 3.10 or higher  
- FastAPI  
- SQLAlchemy  
- Uvicorn

---

## ⚡ Project Structure

students-courses-crud/
│── database.py # Database connection and session setup
│── models.py # SQLAlchemy table models: Student, Course, Enrollment
│── schemas.py # Pydantic models for request/response validation
│── crud.py # Functions to perform CRUD operations
│── main.py # FastAPI app with endpoints
│── requirements.txt # Project dependencies
│── README.md # Project instructions (this file)
│── env/ # Virtual environment (do not upload to GitHub)

yaml
Copy code

---

## 🚀 Setup Instructions

1. **Clone or download the repository**:

```cmd
git clone <your-repo-url>
cd students-courses-crud
Create and activate a virtual environment:

cmd
Copy code
python -m venv env
env\Scripts\activate
Install dependencies:

cmd
Copy code
pip install -r requirements.txt
Run the FastAPI application:

cmd
Copy code
uvicorn main:app --reload
Open the API docs in a browser:

arduino
Copy code
http://127.0.0.1:8000/docs
You will see the Swagger UI with all endpoints for Students, Courses, and Enrollments.

🧩 API Endpoints
Students
POST /students/ → Create a new student

GET /students/ → List all students

GET /students/{student_id} → Get a single student

DELETE /students/{student_id} → Delete a student

Courses
POST /courses/ → Create a new course

GET /courses/ → List all courses

GET /courses/{course_id} → Get a single course

DELETE /courses/{course_id} → Delete a course

Enrollments
POST /enrollments/ → Enroll a student in a course

GET /enrollments/ → List all enrollments

⚙ Usage Example
Create a student:

json
Copy code
POST /students/
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "age": 21
}
Create a course:

json
Copy code
POST /courses/
{
  "title": "Mathematics 101",
  "description": "Introductory math course"
}
Enroll the student in the course:

json
Copy code
POST /enrollments/
{
  "student_id": 1,
  "course_id": 1
}
View all enrollments:

bash
Copy code
GET /enrollments/
💡 Notes
The database file students_courses.db is automatically created in the project folder when you first run the app.

For production, you can replace SQLite with MySQL, PostgreSQL, or any other relational database.

The project uses SQLAlchemy ORM for database interactions and Pydantic for data validation.

Keep env/ out of GitHub; anyone else can recreate it using requirements.txt.

📖 References
FastAPI Official Documentation

SQLAlchemy ORM Documentation

Pydantic Documentation

Uvicorn ASGI Server

✅ Author
Benson Syengo – FastAPI CRUD Student & Courses Project – 2025