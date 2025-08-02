from project.senior_student import SeniorStudent
from unittest import TestCase, main


class TestSeniorStudent(TestCase):
    VALID_ID = '0001'
    VALID_NAME = 'Name'
    VALID_GPA = 2.0
    def setUp(self):
        self.student = SeniorStudent(self.VALID_ID, self.VALID_NAME, self.VALID_GPA)

    def test_init(self):
        self.assertEqual(self.student.student_id, self.VALID_ID)
        self.assertEqual(self.student.name, self.VALID_NAME)
        self.assertEqual(self.student.student_gpa, self.VALID_GPA)
        self.assertEqual(self.student.colleges, set())
        self.assertIsInstance(self.student.colleges, set)

    def test_student_id_setter_if_raise_error(self):
        for student_id in ['', '123']:
            with self.subTest(student_id=student_id):
                with self.assertRaises(ValueError) as e:
                    self.student.student_id = student_id
                self.assertEqual(str(e.exception), "Student ID must be at least 4 digits long!")

    def test_name_setter_raised_error_with_empty_or_null_value(self):
        for name in [' ', '']:
            with self.subTest(name=name):
                with self.assertRaises(ValueError) as e:
                    self.student.name = name
                self.assertEqual(str(e.exception), "Student name cannot be null or empty!")

    def test_gpa_setter_with_value_equel_or_less_zero(self):
        for student_gpa in [-1, 0, 1.0]:
            with self.subTest(student_gpa=student_gpa):
                with self.assertRaises(ValueError) as e:
                    self.student.student_gpa = student_gpa
                self.assertEqual(str(e.exception), "Student GPA must be more than 1.0!")

    def test_apply_to_college_if_failed(self):
        gpa_required = self.VALID_GPA + 1.0
        college_name = 'College'

        result = self.student.apply_to_college(gpa_required, college_name)
        expected_result = 'Application failed!'

        self.assertEqual(result, expected_result)

    def test_apply_to_college_if_student_is_in(self):
        college = 'COLLEGE'
        result = self.student.apply_to_college(1.1, college)
        expected_result = f'{self.student.name} successfully applied to {college}.'

        self.assertEqual(result, expected_result)
        self.assertIn(college, self.student.colleges)

    def test_update_gpa_with_lower_value_from_one(self):
        new_gpa = 0.5
        result = self.student.update_gpa(new_gpa)
        expected_result = 'The GPA has not been changed!'

        self.assertEqual(result, expected_result)
        self.assertNotEqual(new_gpa, self.student.student_gpa)

    def test_update_gpa_with_valid_value(self):
        new_gpa = 2.5
        result = self.student.update_gpa(new_gpa)
        expected_result = 'Student GPA was successfully updated.'

        self.assertEqual(result, expected_result)
        self.assertEqual(new_gpa, self.student.student_gpa)

    def test_equal_student_gpa_return_true(self):
        student_2 = SeniorStudent('0002', 'Student', self.VALID_GPA)

        result = self.student == student_2
        self.assertTrue(result)

    def test_equal_student_gpa_return_false(self):
        student_2 = SeniorStudent('0002', 'Student', 2.5)

        result = self.student == student_2
        self.assertFalse(result)




if __name__ == '__main__':
    main()
