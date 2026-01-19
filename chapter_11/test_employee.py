import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):

        self.employee = Employee('aaa', 'bbb', 7000)
        #默认雇员实例

    def test_give_default_raise(self):
        #默认年薪添加
        self.employee.give_raise()
        self.assertEqual(self.employee.year_raise, 12000)

    def test_give_custom_raise(self):
        #指定年薪添加
        self.employee.give_raise(2500)
        self.assertEqual(self.employee.year_raise, 9500)