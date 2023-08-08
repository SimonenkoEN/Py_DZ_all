#  Создайте класс прямоугольник.
#  Класс должен принимать длину и ширину при создании
# экземпляра.
#  У класса должно быть два метода, возвращающие периметр
# и площадь.
#  Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, width: float, height: float = None ) -> None:
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
    
    def culc_perimetr(self) -> float:
        return 2 * (self.height + self.width)

    def culc_area(self) -> float:
        return self.height * self.width


if __name__ == '__main__':
    rect1 = Rectangle(5)
    rect2 = Rectangle(2, 3)
    print(f'{rect1.culc_perimetr() = }, {rect1.culc_area() = }')
    print(f'{rect2.culc_perimetr() = }, {rect2.culc_area() = }')