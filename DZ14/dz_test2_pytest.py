# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
#  Напишите к ним тесты.
#  2-5 тестов на задачу в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

import pytest
from dz_test2_doctest import My_Fractions


def test_Class_1():
    assert My_Fractions().get_fraction('3/4') == (3, 4)


def test_Class_2():
    assert My_Fractions().sum_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2')) == '3/4'


def test_Class_3():
    assert My_Fractions().mult_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2')) == '1/8'


if __name__ == '__main__':
    pytest.main(['-vv'])