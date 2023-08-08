#  Возьмите 1-3 любые задачи из прошлых семинаров (например 
# сериализация данных), которые вы уже решали. Превратите 
# функции в методы класса, а параметры в свойства. Задачи 
# должны решаться через вызов методов экземпляра.

from random import randint as rnd


class QE: # Quadratic Equation

    def __init__(self) -> None:
        pass
    
    def get_roots(self, a: int = 1, b: int = 1, c: int = 1) -> None:
        if a == 0:
            x = 'a = 0. Уравнение линейное!'
        else:
            x = []
            d = b ** 2 - 4 * a * c
            if d < 0:
                d = complex(d, 0)
            if d == 0:
                x.append(-b / (2*a))
            else:
                x.append((-b + d ** 0.5) / (2*a))
                x.append((-b - d ** 0.5) / (2*a))
        return x


if __name__ == '__main__':
    a, b, c = [rnd(-10, 10) for _ in range(3)]
    example = QE()
    roots = example.get_roots(a, b, c)
    print(f'{a = }, {b = }, {c = }\n  {roots =}')