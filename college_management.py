import json
import os
from datetime import datetime


class CollegeManagementSystem:
    """Simple project-based college management system for CLI use."""

    def __init__(self, storage_path="college_data.json"):
        self.storage_path = storage_path
        self.students = []
        self.faculty = []
        self.courses = []
        self.enrollments = []
        self.fee_records = {}
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self.storage_path):
            self._save_data()
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            self._save_data()
            return

        self.students = data.get("students", [])
        self.faculty = data.get("faculty", [])
        self.courses = data.get("courses", [])
        self.enrollments = data.get("enrollments", [])
        self.fee_records = data.get("fee_records", {})

    def _save_data(self):
        data = {
            "students": self.students,
            "faculty": self.faculty,
            "courses": self.courses,
            "enrollments": self.enrollments,
            "fee_records": self.fee_records,
        }
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def add_student(self, student_id, name, program, department):
        if not student_id or not name or not program or not department:
            raise ValueError("Student ID, name, program, and department are required.")

        for student in self.students:
            if student["student_id"] == student_id:
                raise ValueError(f"Student ID {student_id} already exists.")

        student = {
            "student_id": student_id,
            "name": name.strip(),
            "program": program.strip(),
            "department": department.strip(),
            "status": "active",
        }
        self.students.append(student)
        self._save_data()
        return student

    def list_students(self):
        return [student.copy() for student in self.students]

    def add_faculty(self, faculty_id, name, department):
        if not faculty_id or not name or not department:
            raise ValueError("Faculty ID, name, and department are required.")

        for faculty_member in self.faculty:
            if faculty_member["faculty_id"] == faculty_id:
                raise ValueError(f"Faculty ID {faculty_id} already exists.")

        faculty_member = {
            "faculty_id": faculty_id,
            "name": name.strip(),
            "department": department.strip(),
            "status": "active",
        }
        self.faculty.append(faculty_member)
        self._save_data()
        return faculty_member

    def list_faculty(self):
        return [member.copy() for member in self.faculty]

    def add_course(self, course_id, course_name, department, credits):
        if not course_id or not course_name or not department:
            raise ValueError("Course ID, name, and department are required.")

        try:
            credits = int(credits)
        except (TypeError, ValueError):
            raise ValueError("Credits must be a valid integer.")

        for course in self.courses:
            if course["course_id"] == course_id:
                raise ValueError(f"Course ID {course_id} already exists.")

        course = {
            "course_id": course_id,
            "course_name": course_name.strip(),
            "department": department.strip(),
            "credits": credits,
        }
        self.courses.append(course)
        self._save_data()
        return course

    def list_courses(self):
        return [course.copy() for course in self.courses]
 
    def _find_student(self, student_id):
        for student in self.students:
            if student["student_id"] == student_id:
                return student
        return None

    def _find_course(self, course_id):
        for course in self.courses:
            if course["course_id"] == course_id:
                return course
        return None

    def enroll_student(self, student_id, course_id):
        student = self._find_student(student_id)
        course = self._find_course(course_id)

        if student is None:
            raise ValueError(f"Student {student_id} not found.")
        if course is None:
            raise ValueError(f"Course {course_id} not found.")

        for enrollment in self.enrollments:
            if enrollment["student_id"] == student_id and enrollment["course_id"] == course_id:
                raise ValueError(f"Student {student_id} is already enrolled in {course_id}.")

        enrollment = {
            "student_id": student_id,
            "course_id": course_id,
            "student_name": student["name"],
            "course_name": course["course_name"],
            "enrolled_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.enrollments.append(enrollment)
        self._save_data()
        return enrollment

    def list_enrollments(self):
        return [entry.copy() for entry in self.enrollments]

    def record_fee_payment(self, student_id, amount):
        student = self._find_student(student_id)
        if student is None:
            raise ValueError(f"Student {student_id} not found.")

        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Payment amount must be positive.")

        self.fee_records[student_id] = self.fee_records.get(student_id, 0.0) + amount
        self._save_data()
        return self.fee_records[student_id]

    def get_student_balance(self, student_id):
        student = self._find_student(student_id)
        if student is None:
            raise ValueError(f"Student {student_id} not found.")
        return float(self.fee_records.get(student_id, 0.0))

    def get_student_fee_summary(self, student_id):
        student = self._find_student(student_id)
        if student is None:
            raise ValueError(f"Student {student_id} not found.")
        return {
            "student_id": student_id,
            "name": student["name"],
            "total_paid": float(self.fee_records.get(student_id, 0.0)),
        }
