#  Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
#  Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable


def gess_number(num: int, count: int) -> Callable[[], None]:
    def gess() -> None:
        print(f'Угадайте число от 1 до 100 за {count} попвток!')
        for i in range(1, count + 1):
            attempt = int(input(f'Попытка №{i}: '))
            if attempt == num:
                print('Вы угадали!')
                break
            elif attempt > num:
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
    return gess


if __name__ == '__main__':
    game = gess_number(25, 5)
    game()