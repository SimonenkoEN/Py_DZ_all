# Задание №1
#  Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
#  Возвращается строка в нижнем регистре

from string import ascii_letters


def edit_text(text: str) -> str:
    return ''.join(char for char in text 
                   if char in set(ascii_letters + ' ')).lower()

if __name__ == '__main__':
    print(edit_text('as DF 123 ава @#$@#$'))