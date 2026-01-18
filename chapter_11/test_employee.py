import unittest
from 练习.chapter_11.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_give_default_raise(self):
        employee = Employee('aaa', 'bbb', 7000)
        employee.give_raise()
        self.assertEqual(employee.year_raise, 12000)

    def test_give_custom_raise(self):
        employee = Employee('aaa', 'bbb', 7000)
        employee.give_raise(2500)
        self.assertEqual(employee.year_raise, 9500)