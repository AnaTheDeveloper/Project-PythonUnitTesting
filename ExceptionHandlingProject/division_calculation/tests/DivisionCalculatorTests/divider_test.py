import unittest
from ExceptionHandlingProject.division_calculation.divider import Divider


class TestDivider(unittest.TestCase):

    def test_divide_will_work(self):
        result = Divider.divide_two_numbers(self, 10, 2)
        self.assertEquals(result, 5)

    def test_divide_by_zero_will_not_work(self):
        Divider.divide_two_numbers(self, 10, 0)
        self.assertRaises(ZeroDivisionError)

    def test_divide_by_a_string_number_will_fail(self):
        Divider.divide_two_numbers(self, 10, '2')
        self.assertRaises(TypeError)

#TODO: Rewrite tests
    def test_dividing_by_null_will_fail(self):
        Divider.divide_two_numbers(self, 10, None)



if __name__ == '__main__':
    unittest.main()
