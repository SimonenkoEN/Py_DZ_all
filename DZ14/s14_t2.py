# Задание №2
#  Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# - возврат строки без изменений
# - возврат строки с преобразованием регистра без потери
# символов
# - возврат строки с удалением знаков пунктуации
# - возврат строки с удалением букв других алфавитов
# - возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters

def edit_text(s: str) -> str:
    """
    >>> edit_text('hello world')
    'hello world'

    >>> edit_text('Hello world')
    'hello world'

    >>> edit_text('hello world!')
    'hello world'

    >>> edit_text('Hello world привет')
    'hello world '

    >>> edit_text('Hello world! Привет!')
    'hello world '
    """
    return ''.join(char for char in s 
                   if char in set(ascii_letters + ' ')).lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

