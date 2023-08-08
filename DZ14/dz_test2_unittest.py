# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
#  Напишите к ним тесты.
#  2-5 тестов на задачу в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

import unittest
from dz_test2_doctest import My_Fractions

class TestClass(unittest.TestCase):

    def test_Class_1(self):
        self.assertEqual(My_Fractions().get_fraction('3/4'), (3, 4))

    def test_Class_2(self):
        self.assertEqual(My_Fractions().sum_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2')), '3/4')

    def test_Class_3(self):
        self.assertEqual(My_Fractions().mult_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2')), '1/8')


if __name__ == '__main__':
    unittest.main(verbosity=2)