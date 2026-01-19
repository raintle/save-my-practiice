import unittest
from  city_fuc import city_describe
#测试用例的使用

class TestCities(unittest.TestCase):

    def test_city_name(self):
        describe_city = city_describe('shanghai', 'china')
        self.assertEqual(describe_city, 'shanghai, china')
        #第一个测试用例

    def test_city_population(self):
        b_describe_city = city_describe('shanghai', 'china', '200000')
        self.assertEqual(b_describe_city, 'shanghai, china, 200000')
        #第二个测试用例