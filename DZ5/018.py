# ДЗ к семинару 5, задание 1
# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def get_path(path):
    return path.rsplit('\\', maxsplit=1)[0], *path.rsplit('\\', maxsplit=1)[1].rsplit('.',maxsplit=1)


if __name__ == '__main__':
    path = 'D:\GeekBraims\Погружение в Python\Семинар 5.pdf'
    print(f'{get_path(path) = }')