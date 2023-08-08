# Задание №1
#  Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
#  Обрабатывайте не числовые данные как исключения


def get_numbers() -> float | int:
    while True:
        num = input()
        try:
            num = int(num)
            break
        except ValueError as e:
            try:
                num = float(num)
                break
            except ValueError as e:
                print(e)
    return num


if __name__ == '__main__':
    print(get_numbers())