from pydantic import BaseModel
from typing import Optional

# Student
class StudentBase(BaseModel):
    name: str
    email: str
    age: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    student_id: int
    class Config:
        orm_mode = True

# Course
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int
    class Config:
        orm_mode = True

# Enrollment
class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    enrollment_id: int
    class Config:
        orm_mode = True

