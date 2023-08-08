# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
#  Напишите к ним тесты.
#  2-5 тестов на задачу в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

import unittest
from dz_test1_doctest import Circle

class TestClass(unittest.TestCase):

    def test_Class_1(self):
        self.assertEqual(Circle(1).radius, 1)

    def test_Class_2(self):
        self.assertEqual(round(Circle(1).area(), 2), 3.14)

    def test_Class_3(self):
        self.assertEqual(round(Circle(1).length(), 2), 6.28)


if __name__ == '__main__':
    unittest.main(verbosity=2)