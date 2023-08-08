# Задание 2. ДЗ. Семинар 2
# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from math import gcd
from fractions import Fraction

user_fraction_1 = input('Введите первую дробь вида a/b: ')
fraction_1 = user_fraction_1.split('/')
numerator_1, denominator_1 = int(fraction_1[0]), int(fraction_1[1])

user_fraction_2 = input('Введите вторую дробь вида a/b: ')
fraction_2 = user_fraction_2.split('/')
numerator_2, denominator_2 = int(fraction_2[0]), int(fraction_2[1])

# вычисление суммы
num_res = numerator_1 * denominator_2 + numerator_2 * denominator_1
denom_res = denominator_1 * denominator_2
nod = gcd(num_res, denom_res)
print(user_fraction_1, '+', user_fraction_2, '=', end=' ')
print(num_res//nod, '/', denom_res//nod, sep='')

# вычисление произведения
num_res = numerator_1 * numerator_2
denom_res = denominator_1 * denominator_2
nod = gcd(num_res, denom_res)
print(user_fraction_1, '*', user_fraction_2, '=', end=' ')
print(num_res//nod, '/', denom_res//nod, sep='')

#  модуль fraction
x = Fraction(user_fraction_1)
y = Fraction(user_fraction_2)
print('Проверка модулем fraction:', x + y, x * y)