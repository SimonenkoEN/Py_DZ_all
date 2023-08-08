#  Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
#  Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
#  Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
#  Имя файла должно совпадать с именем декорируемой
# функции.

import os
import json
from typing import Callable


def loger(func: Callable):
    j_file = f'{func.__name__}.json'
    if os.path.exists(j_file):
        with open(j_file, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
    else:
        data = []

    def wraper(*args, **kwargs):
        j_dict = {'args' : args, **kwargs}
        result = func(*args, **kwargs)
        j_dict['result'] = result
        data.append(j_dict)
        with open(j_file, 'w', encoding='utf-8') as jf:
            json.dump(data, jf, indent=2)
        return result

    return wraper


@loger
def get_summ(a: int, b: int, *args, **kwargs) -> int:
    return a + b


if __name__ == '__main__':
    print(get_summ(2, 2, 'Hello', x = 5, y = 6, z = 'world'))
