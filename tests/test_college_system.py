import unittest
import os
import tempfile

from college_management import CollegeManagementSystem


class CollegeManagementSystemTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = os.path.join(self.temp_dir.name, "college_data.json")
        self.system = CollegeManagementSystem(storage_path=self.storage_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_list_students(self):
        self.system.add_student("S101", "Aarav", "B.Tech", "CS")
        students = self.system.list_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["student_id"], "S101")

    def test_add_and_list_faculty(self):
        self.system.add_faculty("F101", "Dr. Mehta", "Computer Science")
        faculty = self.system.list_faculty()
        self.assertEqual(len(faculty), 1)
        self.assertEqual(faculty[0]["faculty_id"], "F101")

    def test_add_course_and_enroll_student(self):
        self.system.add_student("S101", "Aarav", "B.Tech", "CS")
        self.system.add_course("C101", "Python Essentials", "CS", 3)
        self.system.enroll_student("S101", "C101")
        enrollments = self.system.list_enrollments()
        self.assertEqual(len(enrollments), 1)
        self.assertEqual(enrollments[0]["student_id"], "S101")

    def test_fee_collection_and_report(self):
        self.system.add_student("S101", "Aarav", "B.Tech", "CS")
        self.system.record_fee_payment("S101", 25000)
        balance = self.system.get_student_balance("S101")
        self.assertEqual(balance, 25000)


if __name__ == "__main__":
    unittest.main()