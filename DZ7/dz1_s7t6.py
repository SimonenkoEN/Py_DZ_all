# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

__all__ = ['files_todir_gen', 'files_gen']

from random import randint as rnd, choices as chs
from string import ascii_lowercase as asc, digits as dig
import os


def files_gen(ext: str,files: int = 42 , min_name: int = 6, max_name: int = 30, \
      min_bytes: int = 256, max_bytes: int = 4096) -> None:
    count = 0
    while count < files:
        name = ''.join(chs(asc + dig, k=rnd(min_name,max_name + 1)))
        if not f'{name}.{ext}' in os.listdir():
            data = bytes(rnd(0, 255) for _ in range(rnd(min_bytes, max_bytes)))
            with open(f'{name}.{ext}', 'wb') as f:
                f.write(data)
        count += 1


def files_todir_gen(*args) -> None:
    """files_todir_gen(расширение, кол-во файлов, 
    [расширение, кол-во файлов, ...,] имя директории)"""
    dir = args[-1]
    if not dir in os.listdir():
        os.mkdir(dir)
        os.chdir(dir)
    else:
        os.chdir(dir)
    print(os.getcwd())
    for i in range(0, len(args) - 1, 2):
        files_gen(args[i], args[i + 1])
    os.chdir('..')


if __name__ == '__main__':
    files_todir_gen('bmp', 4, 'avi', 3, 'Alfa')