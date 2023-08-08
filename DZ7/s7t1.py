# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции

from random import randint as ri, uniform as uf

MIN = -1000
MAX = 1001


def write_rnd_to_file(nlines:int, file_name:str) -> None:
    with open(file_name, 'a', encoding='UTF-8') as f:
        for _ in range(nlines):
            f.write(f'{ri(MIN, MAX)}|{uf(MIN, MAX)}\n')


if __name__ == '__main__':
    write_rnd_to_file(3, 't1.txt')