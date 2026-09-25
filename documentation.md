# Documentation

## Project Title
College Management System

## Overview
This project is a Python-based command-line application designed to manage common activities in a college. It allows users to maintain records of students, faculty, courses, enrollments, and fee payments. The system is implemented using Python only and can be run from the terminal without any GUI. 

## Objective
The main goal of this project is to provide a simple and practical college administration solution that demonstrates key Python concepts such as:

- Classes and objects
- Data storage using JSON
- Input/output handling
- Validation and error handling
- File-based persistence
- Menu-driven CLI design

## Features
1. Add Student
2. View all students
3. Add Faculty
4. View all faculty members
5. Add Course
6. View all courses
7. Enroll a student in a course
8. View all enrollments
9. Record fee payment
10. View fee summary for a student
11. Exit the system

## System Architecture
The project is built using a simple class-based architecture:

- `CollegeManagementSystem`: Handles all major operations and data logic.
- `main.py`: Runs the interactive menu-based interface.
- `college_data.json`: Stores the data persistently on the local disk.

## Functional Modules

### 1. Student Management
- Add a student with ID, name, program, and department
- Save the student record in the storage file
- Retrieve and display student details

### 2. Faculty Management
- Add faculty members with ID, name, and department
- Track faculty details in the system

### 3. Course Management
- Add new courses with ID, name, department, and credits
- View all available courses

### 4. Enrollment Management
- Enroll students in specific courses
- Prevent duplicate enrollment entries
- Store enrollment date and related data

### 5. Fee Management
- Record payment amount for a specific student
- Maintain total paid amount
- Display fee summary for any student

## Data Storage
The data is stored in a JSON file named `college_data.json` in the project folder. This allows the system to retain information between runs.

## How to Run
1. Open the terminal in the project folder.
2. Run the following command:

```bash
python main.py
```

3. Use the menu options to perform operations.

## Example Workflow
- Add a student: `S101`
- Add a faculty member: `F101`
- Add a course: `C101`
- Enroll the student in the course
- Record a fee payment
- Display the student fee summary

## Error Handling
The application includes basic validation for:

- Empty required input values
- Duplicate student or faculty IDs
- Duplicate course IDs
- Duplicate course enrollment
- Invalid numeric fee values

## Advantages
- Easy to use
- Beginner-friendly code
- Suitable for Python essential course projects
- Works completely from the command line

## Conclusion
The College Management System is a practical Python project that demonstrates essential programming and data management concepts. It is simple, functional, and suitable for academic submission and evaluation.
