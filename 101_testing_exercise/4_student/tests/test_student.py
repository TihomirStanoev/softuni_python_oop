from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    STUDENT_NAME = 'Test'
    COURSE = {"Python OOP": ["Inheritance", "Polymorphism"]}
    def setUp(self):
        self.student = Student(self.STUDENT_NAME)
        self.student_with_course = Student(self.STUDENT_NAME, self.COURSE)

    def test_init(self):
        self.assertEqual(self.student.name, self.STUDENT_NAME)
        self.assertIsInstance(self.student.courses, dict)

    def test_enroll_new_course(self):
        course_dict = {"Python OOP":["Inheritance", "Polymorphism"]}
        result = self.student.enroll("Python OOP", ["Inheritance", "Polymorphism"])
        expected_result = "Course and course notes have been added."

        self.assertEqual(result, expected_result)
        self.assertDictEqual(self.student.courses, course_dict)

    def test_enroll_new_course_with_y(self):
        course_dict = {"Python OOP":["Inheritance", "Polymorphism"]}
        result = self.student.enroll("Python OOP", ["Inheritance", "Polymorphism"], 'Y')
        expected_result = "Course and course notes have been added."

        self.assertEqual(result, expected_result)
        self.assertDictEqual(self.student.courses, course_dict)


    def test_enroll_update_notes(self):
        added_notes = {"Python OOP": ["Inheritance", "Polymorphism", "Abstraction", "Capsulation"]}
        self.student.enroll("Python OOP", ["Inheritance", "Polymorphism"])

        result = self.student.enroll("Python OOP", ["Abstraction", "Capsulation"])
        expected_result = "Course already added. Notes have been updated."

        self.assertEqual(result, expected_result)
        self.assertDictEqual(added_notes, self.student.courses)

    def test_enroll_add_new_course(self):
        result = self.student.enroll('Python OOP',None,'N')
        expected_dict = {'Python OOP':[]}
        expected_result = "Course has been added."

        self.assertEqual(result, expected_result)
        self.assertDictEqual(expected_dict, self.student.courses)

    def test_add_note_if_course_name_exist(self):
        result = self.student_with_course.add_notes('Python OOP', "Abstraction")
        expected_result = "Notes have been updated"

        self.assertEqual(result, expected_result)
        self.assertIn('Abstraction', self.student_with_course.courses['Python OOP'])

    def test_add_notes_raises_exception_when_course_not_found(self):
        expected_exception = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as e:
            self.student.add_notes('Test', 'Test note')
        self.assertEqual(str(e.exception), expected_exception)

    def test_leave_course(self):
        result = self.student_with_course.leave_course('Python OOP')
        expected_result = "Course has been removed"

        self.assertEqual(result, expected_result)
        self.assertNotIn('Python OOP', self.student_with_course.courses)

    def test_leave_course_raises_exception_when_course_not_found(self):
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as e:
            self.student_with_course.leave_course('lmK')
        self.assertEqual(expected_result, str(e.exception))


if __name__ == '__main__':
    main()