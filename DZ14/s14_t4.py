# Задание №4
#  Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# - возврат строки без изменений
# - возврат строки с преобразованием регистра без потери
# символов
# - возврат строки с удалением знаков пунктуации
# - возврат строки с удалением букв других алфавитов
# - возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from s14_t1 import edit_text
import pytest


def test_edit_text_1():
    assert edit_text('hello world') == 'hello world'


def test_edit_text_2():
    assert edit_text('Hello World') == 'hello world'


def test_edit_text_3():
    assert edit_text('hello world!') == 'hello world'


def test_edit_text_4():
    assert edit_text('hello world привет') == 'hello world '


def test_edit_text_5():
    assert edit_text('Hello World! Привет!') == 'hello world '



if __name__ == '__main__':
    pytest.main(['-v'])