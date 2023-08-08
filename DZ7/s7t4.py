# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

__all__ = ['files_generator']

from random import randint as rnd, choices as chs
from string import ascii_lowercase as asc, digits as dig


def files_generator(ext:str,files:int=42 , min_name:int=6, max_name:int=30, \
      min_bytes:int=256, max_bytes:int=4096) -> None:
    for _ in range(files):
        name = ''.join(chs(asc + dig, k=rnd(min_name,max_name + 1)))
        data = bytes(rnd(0, 255) for _ in range(rnd(min_bytes, max_bytes)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    files_generator('txt', 2, 3, 7, 25, 500)