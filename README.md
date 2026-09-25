# College Management System

A Python-only command-line college management system built for academic project submission. It helps manage students, faculty, courses, enrollments, and fee records in a simple and beginner-friendly way.
 
## Features

- Add and display students
- Add and display faculty members
- Add and display academic courses
- Enroll students in courses
- View course enrollments
- Record student fee payments
- View fee summary for any student
- Data stored in a local JSON file for persistence

## Project Structure

- `main.py` – command-line user interface
- `college_management.py` – application logic and data handling
- `college_data.json` – auto-generated storage file
- `tests/test_college_system.py` – unit tests for key features

## Requirements

- Python 3.8 or above
- No external libraries are required

## Setup

1. Open a terminal in the project folder.
2. Check Python installation:
   ```bash
   python --version
   ```
3. If Python is installed, run the project using:
   ```bash
   python main.py
   ```

## How to Use

Once the program starts, a menu will be displayed:

1. Add Student
2. View Students
3. Add Faculty
4. View Faculty
5. Add Course
6. View Courses
7. Enroll Student in Course
8. View Enrollments
9. Record Fee Payment
10. View Fee Summary
11. Exit

Follow the on-screen prompts to complete actions.

## Example Flow

- Add a student with ID `S101`
- Add a faculty member with ID `F101`
- Add a course with ID `C101`
- Enroll student `S101` in course `C101`
- Record a fee payment for `S101`
- View summary to see the total amount paid

## Running Tests

To verify the project logic, run:

```bash
python -m unittest discover -s tests -v
```

## Project Report Summary

This project demonstrates core Python programming skills such as:

- Class-based object design
- File handling using JSON
- User input and menu-driven command-line systems
- Data validation and error handling
- Basic reporting and listing features

It is suitable as a Python essentials course project because it covers real-world academic operations in a simple and executable format.
