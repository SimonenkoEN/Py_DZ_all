#  Дорабатываем задачу 1.
#  Превратите внешнюю функцию в декоратор.
#  Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
#  Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
from random import randint


def check_args(func: Callable):
    MIN_ALL = 1
    MAX_NUM = 100
    MAX_COUNT = 10
    def wraper(num: int, count: int, *args, **kwargs):
        if not MIN_ALL <= num <= MAX_NUM:
            num = randint(1, 100)
        if not MIN_ALL <= count <= MAX_COUNT:
            count = randint(1, 10)
        result = func(num, count, *args, **kwargs)
        return result
    return wraper


@check_args
def gess_number(num: int, count: int) -> Callable[[], None]:
    def gess() -> None:
        print(f'Угадайте число от 1 до 100 за {count} попвток!')
        for i in range(1, count + 1):
            attempt = int(input(f'Попытка №{i}: '))
            if attempt == num:
                print('Вы угадали!')
                break
            elif attempt > num:
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
    return gess


if __name__ == '__main__':
    game = gess_number(250, 50)
    game()