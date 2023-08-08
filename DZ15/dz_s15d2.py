# Задание 2
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import os
import csv
import json
import logging
import argparse
from typing import Callable
from functools import wraps
from random import randint as rnd

logging.basicConfig(level=logging.INFO, filename='log_dz2.txt', filemode='w', encoding='utf-8')
logger = logging.getLogger(__name__)


def get_roots(a: int, b: int, c: int):
    if a == 0:
        logger.error('Коэффициент "а" равен 0, уравнение не квадратное')
        x = None
    else:
        x = []
        d = b ** 2 - 4 * a * c
        if d < 0:
            d = complex(d, 0)
        if d == 0:
            x.append(-b / (2*a))
            logger.info(f'Корень уравнения c коэффициентами {a =}, {b =}, {c =}: {x[0]}')
        else:
            x.append((-b + d ** 0.5) / (2*a))
            x.append((-b - d ** 0.5) / (2*a))
            logger.info(f'Корни уравнения c коэффициентами {a =}, {b =}, {c =}: {x[0]}, {x[1]}')
    print(*x)
    return x


def calculation(func: Callable):
    if not os.path.exists('members.csv'):
        rnd_nums_to_csv()
    with open('members.csv', 'r', newline='', encoding='utf-8') as cf:
        csv_data = csv.reader(cf, dialect='excel')
        members = list(csv_data)
    roots = []
    @wraps(func.__name__)
    def wraper(*args, **kwargs):
        for i in range(len(members)):
            a, b, c = map(int, members[i])
            if a == 0:
                logger.error(f'Коэффтциент "а" равен 0, уравнение не квадратное')
            else:
                roots.append(func(a, b, c))
        return roots
    return wraper


def rnd_nums_to_csv() -> None:
    MIN_ROWS = 1
    MAX_ROWS = 10
    MIN_NUMBER = -10
    MAX_NUMBER = 10
    NUMBERS_IN_ROW = 3
    with open('members.csv', 'w', newline='', encoding='utf-8') as cf:
        count = 0
        csv_data = csv.writer(cf, dialect='excel')
        for _ in range(rnd(MIN_ROWS, MAX_ROWS)):
            count += 1
            nums = [rnd(MIN_NUMBER, MAX_NUMBER) 
                    for _ in range(NUMBERS_IN_ROW)]
            csv_data.writerow(nums)
        logger.error('Файл members.csv не найден')
        logger.info('Файл members.csv сгенерирован')
        logger.info(f'Сгенерировано наборов параметров: {len(nums)}')


def save_to_json(func: Callable):
    data = []
    @wraps(func.__name__)
    def wraper(*args, **kwargs):
        if args[0] == 0:
            return None
        else:
            roots = func(*args, **kwargs)
            j_dict = {'a' : args[0], 'b' : args[1], 'c' : args[2], 'roots' : str(roots)}
            data.append(j_dict)
        with open('roots.json', 'w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=2)
            logger.info(f'Результат сохранены в файл roots.json')
        return roots
    return wraper


@calculation
@save_to_json
def from_file(a: int, b: int, c: int):
    x = get_roots(a, b, c)
    return x


@save_to_json
def in_command_line(a: int, b: int, c: int):
    x = get_roots(a, b, c)
    return x


def pars():
    parser = argparse.ArgumentParser(prog='dz_s15d2.py', description='Вымисление корней квадратного уравнения')
    parser.add_argument('-a', '--a', default=1, type=int, help='Коэффициент а')
    parser.add_argument('-b', '--b', default=0, type=int, help='Коэффициент b')
    parser.add_argument('-c', '--c', default=0, type=int, help='Коэффициент c')
    parser.add_argument('-f', '--file', default=0, type=int, help='Работа с коэффициентами из файла')
    args = parser.parse_args()
    if args.file:
        return  from_file()
    else:
        return  in_command_line(args.a, args.b, args.c)


if __name__ == '__main__':
    pars()
