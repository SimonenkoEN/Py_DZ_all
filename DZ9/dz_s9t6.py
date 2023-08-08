# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import os
import json
from functools import wraps
from typing import Callable
from random import randint


def check_args(func: Callable):
    MIN_ALL = 1
    MAX_NUM = 100
    MAX_COUNT = 10
    
    @wraps(func)
    def wraper(num: int, count: int, *args, **kwargs):
        if not MIN_ALL <= num <= MAX_NUM:
            num = randint(1, 100)
        if not MIN_ALL <= count <= MAX_COUNT:
            count = randint(5, 10)
        result = func(num, count, *args, **kwargs)
        return result
    return wraper


def loger(func: Callable):
    j_file = f'{func.__name__}.json'
    if os.path.exists(j_file):
        with open(j_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
    else:
        data = []

    @wraps(func)
    def wraper(*args, **kwargs):
        j_dict = {'args' : args, **kwargs}
        result = func(*args, **kwargs)
        j_dict['result'] = result
        data.append(j_dict)
        with open(j_file, 'w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=2)
        return result
    return wraper


def starter(num: int = 1):
    def deco(func: Callable):
        res = []

        @wraps(func)
        def wraper(*args, **kwargs):
            for _ in range(num):
                res.append(func(*args, **kwargs))
            return res
        return wraper
    return deco


@check_args
@loger
@starter(2)
def gess_number(num: int, count: int) -> str:
    print(f'Угадайте число от 1 до 100 за {count} попвток!')
    for i in range(1, count + 1):
        attempt = int(input(f'Попытка №{i}: '))
        if attempt == num:
            print('Вы угадали!')
            return 'Вы угадали!'
        elif attempt > num:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')
    print('Вы не угадали!')
    return 'Вы не угадали!'

if __name__ == '__main__':
    gess_number(250, 50)