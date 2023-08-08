#  Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

import os
import csv
import json
from typing import Callable
from functools import wraps
from random import randint as rnd


def rnd_nums_to_csv() -> None:
    MIN_ROWS = 100
    MAX_ROWS = 1000
    MIN_NUMBER = -100
    MAX_NUMBER = 100
    NUMBERS_IN_ROW = 3
    with open('members.csv', 'w', newline='', encoding='utf-8') as cf:
        csv_data = csv.writer(cf, dialect='excel')
        for _ in range(rnd(MIN_ROWS, MAX_ROWS)):
            nums = [rnd(MIN_NUMBER, MAX_NUMBER) 
                    for i in range(NUMBERS_IN_ROW)]
            csv_data.writerow(nums)


def calculation(func: Callable):
    if not os.path.exists('members.csv'):
        rnd_nums_to_csv()
    with open('members.csv', 'r', newline='', encoding='utf-8') as cf:
        csv_data = csv.reader(cf, dialect='excel')
        members = list(csv_data)
    roots = []
    @wraps(func.__name__)
    def wraper(*args, **kwargs):
        for line in members:
            a, b, c = map(int, line)
            roots.append(func(a, b, c))
        return roots
    return wraper


def loger(func: Callable):
    data = []
    @wraps(func.__name__)
    def wraper(*args, **kwargs):
        roots = func(*args, **kwargs)
        j_dict = {'args' : args, 'roots' : str(roots)}
        data.append(j_dict)
        with open('roots.json', 'w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=2)
        return roots
    return wraper


@calculation
@loger
def get_roots_of_equation(a: int = 1, b: int = 1, c: int = 1) -> None:
    if a == 0:
        x = 'a = 0. Уравнение линейное!'
    else:
        x = []
        d = b ** 2 - 4 * a * c
        if d < 0:
            d = complex(d, 0)
        if d == 0:
            x.append(-b / (2*a))
        else:
            x.append((-b + d ** 0.5) / (2*a))
            x.append((-b - d ** 0.5) / (2*a))
    return x


if __name__ == '__main__':
    # print(*get_roots_of_equation(), sep='\n')
    get_roots_of_equation()
