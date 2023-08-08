# Создайте декоратор с параметром.
#  Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable


def starter(num: int = 1):
    def deco(func: Callable):
        res = []
        def wraper(*args, **kwargs):
            for _ in range(num):
                res.append(func(*args, **kwargs))
            return res
        return wraper
    return deco


@starter(3)
def get_summ(a: int, b: int, *args, **kwargs) -> int:
    return a + b


if __name__ == '__main__':
    print(get_summ(2, 2))
