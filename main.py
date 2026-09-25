import os

from college_management import CollegeManagementSystem

 
def print_menu():
    print("\n=== College Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Faculty")
    print("4. View Faculty")
    print("5. Add Course")
    print("6. View Courses")
    print("7. Enroll Student in Course")
    print("8. View Enrollments")
    print("9. Record Fee Payment")
    print("10. View Fee Summary")
    print("11. Exit")


def handle_add_student(system):
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    program = input("Enter Program: ").strip()
    department = input("Enter Department: ").strip()

    student = system.add_student(student_id, name, program, department)
    print(f"Student added: {student['name']} ({student['student_id']})")


def handle_view_students(system):
    students = system.list_students()
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")
    for student in students:
        print(f"ID: {student['student_id']} | Name: {student['name']} | Program: {student['program']} | Department: {student['department']}")


def handle_add_faculty(system):
    faculty_id = input("Enter Faculty ID: ").strip()
    name = input("Enter Faculty Name: ").strip()
    department = input("Enter Department: ").strip()

    faculty_member = system.add_faculty(faculty_id, name, department)
    print(f"Faculty added: {faculty_member['name']} ({faculty_member['faculty_id']})")


def handle_view_faculty(system):
    faculty = system.list_faculty()
    if not faculty:
        print("No faculty members found.")
        return

    print("\nFaculty List:")
    for member in faculty:
        print(f"ID: {member['faculty_id']} | Name: {member['name']} | Department: {member['department']}")


def handle_add_course(system):
    course_id = input("Enter Course ID: ").strip()
    course_name = input("Enter Course Name: ").strip()
    department = input("Enter Department: ").strip()
    credits = input("Enter Credits: ").strip()

    course = system.add_course(course_id, course_name, department, credits)
    print(f"Course added: {course['course_name']} ({course['course_id']})")


def handle_view_courses(system):
    courses = system.list_courses()
    if not courses:
        print("No courses found.")
        return

    print("\nCourse List:")
    for course in courses:
        print(f"ID: {course['course_id']} | Name: {course['course_name']} | Department: {course['department']} | Credits: {course['credits']}")


def handle_enroll(system):
    student_id = input("Enter Student ID: ").strip()
    course_id = input("Enter Course ID: ").strip()

    enrollment = system.enroll_student(student_id, course_id)
    print(f"Enrollment successful: {enrollment['student_name']} -> {enrollment['course_name']}")


def handle_view_enrollments(system):
    enrollments = system.list_enrollments()
    if not enrollments:
        print("No enrollments available.")
        return

    print("\nEnrollment Records:")
    for item in enrollments:
        print(f"Student: {item['student_name']} ({item['student_id']}) | Course: {item['course_name']} ({item['course_id']}) | Date: {item['enrolled_on']}")


def handle_fee_payment(system):
    student_id = input("Enter Student ID: ").strip()
    amount = input("Enter payment amount: ").strip()

    total = system.record_fee_payment(student_id, amount)
    print(f"Fee payment recorded successfully. Total paid by student: {total}")


def handle_fee_summary(system):
    student_id = input("Enter Student ID: ").strip()
    summary = system.get_student_fee_summary(student_id)
    print(f"\nStudent Fee Summary:\nID: {summary['student_id']} | Name: {summary['name']} | Total Paid: {summary['total_paid']}")


def main():
    storage_path = os.path.join(os.path.dirname(__file__), "college_data.json")
    system = CollegeManagementSystem(storage_path=storage_path)

    while True:
        try:
            print_menu()
            choice = input("Choose an option (1-11): ").strip()

            if choice == "1":
                handle_add_student(system)
            elif choice == "2":
                handle_view_students(system)
            elif choice == "3":
                handle_add_faculty(system)
            elif choice == "4":
                handle_view_faculty(system)
            elif choice == "5":
                handle_add_course(system)
            elif choice == "6":
                handle_view_courses(system)
            elif choice == "7":
                handle_enroll(system)
            elif choice == "8":
                handle_view_enrollments(system)
            elif choice == "9":
                handle_fee_payment(system)
            elif choice == "10":
                handle_fee_summary(system)
            elif choice == "11":
                print("Exiting College Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 11.")

            input("\nPress Enter to continue...")
        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            break


if __name__ == "__main__":
    main()
