# Задание №3
#  Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# - возврат строки без изменений
# - возврат строки с преобразованием регистра без потери
# символов
# - возврат строки с удалением знаков пунктуации
# - возврат строки с удалением букв других алфавитов
# - возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from string import ascii_letters

class TestFunc(unittest.TestCase):

    def test_func1(self):
        self.assertEqual(edit_text('hello world'), 'hello world', msg='Faiked')

    def test_func2(self):
        self.assertEqual(edit_text('Hello World'), 'hello world', msg='Faiked')

    def test_func3(self):
        self.assertEqual(edit_text('hello world!'), 'hello world', msg='Faiked')

    def test_func4(self):
        self.assertEqual(edit_text('hello world привет'), 'hello world ', msg='Faiked')

    def test_func5(self):
        self.assertEqual(edit_text('Hello World! Привет!'), 'hello world ', msg='Faiked')


def edit_text(s: str) -> str:
    return ''.join(char for char in s 
                   if char in set(ascii_letters + ' ')).lower()

if __name__ == '__main__':
    unittest.main(verbosity=2)