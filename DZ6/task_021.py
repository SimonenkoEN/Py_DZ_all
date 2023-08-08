""" ДЗ к семинару 6, задание 1
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
ункция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
ля простоты договоримся, что год может быть в диапазоне [1, 9999].
есь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
роверку года на високосность вынести в отдельную защищённую функцию.

В модуль с проверкой даты добавьте возможность запуска в терминале 
с передачей даты на проверку. -> chkdata.py
"""

__all__ = ['check_data']

def _check_data(data : str) -> bool:
    day, month, year = map(int, data.split('.'))

    if not 1 <= year <= 9999:
        return False
    if not 1 <= month <= 12:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12) and not 1 <= day <= 31:
        return False
    if month in (4, 6, 9, 11) and not 1 <= day <= 30:
        return False
    if month == 2 and _check_year(year) and not 1 <= day <= 29:
        return False
    if month == 2 and not _check_year(year) and not 1 <= day <= 28:
        return False
    return True
    

def _check_year(y : str) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0


def check_data(data):
    if _check_data(data):
        print('Такая дата существует!')
    else:
        print('Такой даты нет!')


if __name__ == '__main__':
    check_data('29.02.2020')
