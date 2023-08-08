#  задание 1
#  Создайте класс Моя Строка, где:
# - будут доступны все возможности str
# - дополнительно хранятся имя автора строки и время создания
# (time.time)

# Задание 3
# Добавьте к задачам 1 и 2 строки документации для классов.

import time


class MyString(str):
    """Класс наследует от str и хранит автора и время создания"""
    
    def __new__(cls, value: str, author: str = None):
        instance = super().__new__(cls, value)
        instance.author = author
        sec = time.time()
        struct = time.localtime(sec)
        instance.created = time.strftime('%d-%m-%Y %H:%M', struct)
        return instance
    
    def __str__(self) -> str:
        return f'{super().__str__()} ({self.author})'

    def __repr__(self) -> str:
        return f'Автор строки: {self.author}\nВремя создания: {self.created}'

if __name__ == '__main__':
    print('Задание 1:')
    s = MyString('Hello world!', 'Anonimus')
    print(s)

    print('\nЗадание 3:')
    print(MyString.__doc__)

    print('\nДомашнее задание 1:')
    print(repr(s), end='\n\n')
    print(MyString.__doc__)
    