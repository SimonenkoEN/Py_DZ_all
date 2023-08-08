# ✔ Напишите функцию группового переименования файлов. Она должна:
#  ✔ принимать параметр желаемое конечное имя файлов.
#   При переименовании в конце имени добавляется порядковый номер.
#  ✔ принимать параметр количество цифр в порядковом номере.
#  ✔ принимать параметр расширение исходного файла.
#   Переименование должно работать только для этих файлов внутри каталога.
#  ✔ принимать параметр расширение конечного файла.
#  ✔ принимать диапазон сохраняемого оригинального имени. Например для
#   диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#   К ним прибавляется желаемое конечное имя, если оно передано.
#   Далее счётчик файлов и расширение.

__all__ = ['rename_files']

import os


def rename_files(start: int, stop: int, ext_old: str, ext_new: str, \
                 numb_name: int = 3,  end_name: str = "_" ) -> None:
    counter = 1
    for i in os.listdir():
        if os.path.isfile(i):
            file_name, file_ext = i.rsplit(".", maxsplit=1)
            if file_ext == ext_old:
                zero = numb_name - len(str(counter))
                new_file_name = "".join([file_name[start:stop], end_name, '0' * zero, \
                                         str(counter), '.' , ext_new ])
                os.rename(i, new_file_name)
                counter +=1


if __name__ == '__main__':
    rename_files(1, 5, 'xxx', 3, 'yyy', '_0_')