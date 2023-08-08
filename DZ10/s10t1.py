#  Создайте класс окружность.
#  Класс должен принимать радиус окружности при создании
# экземпляра.
#  У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math

class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def culc_length(self) -> float:
        return 2 * math.pi * self.radius

    def culc_area(self) -> float:
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle1 = Circle(1)
    print(f'{circle1.culc_length() = }, {circle1.culc_area() = }')