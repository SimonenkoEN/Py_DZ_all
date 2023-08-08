#  Задание 5
#  Дорабатываем класс прямоугольник из прошлого семинара.
#  Добавьте возможность сложения и вычитания.
#  При этом должен создаваться новый экземпляр
# прямоугольника.
#  Складываем и вычитаем периметры, а не длинну и ширину.
#  При вычитании не допускайте отрицательных значений.

#  Задание 6
#  Доработайте прошлую задачу.
#  Добавьте сравнение прямоугольников по площади
#  Должны работать все шесть операций сравнения


class Rectangle:
    """При создании экземпляра класса, ожидает на входе значение ширины и длины прямоугольника. При вводе только одного значения, принимает его как стороеу квадрата. Класс включает методы: расчет периметра, расчет площади, сложение  и вычетание по периметрам, сравнение по площади."""
    __square = False

    def __init__(self, width: float, height: float = None ) -> None:
        self.width = width
        if height is None:
            self.height = width
            self.__square = True
        else:
            self.height = height
    
    def culc_perimetr(self) -> float:
        return 2 * (self.height + self.width)

    def culc_area(self) -> float:
        return self.height * self.width
    
    def __add__(self, other):
        perimetr = self.culc_perimetr() + other.culc_perimetr()
        width = self.width + other.width
        height = perimetr / 2 - width
        return Rectangle(width, height)
    
    def __sub__(self, other):
        perimetr = abs(self.culc_area() - other.culc_area())
        width = abs(self.width - other.width)
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __eq__(self, other):
        return self.culc_area() == other.culc_area()

    def __lt__(self, other):
        return self.culc_area() < other.culc_area()

    def __le__(self, other):
        return self.culc_area() <= other.culc_area()

    def __str__(self) -> str:
        if self.__square:
            return f'Квадрат со сторонами {self.width}'
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self) -> str:
        return f'{type(self.width)} {self.width = }\n{type(self.height)} {self.height = }'

if __name__ == '__main__':
    rect1 = Rectangle(5)
    rect2 = Rectangle(2, 3)
    print(f'{rect1.culc_perimetr() = }, {rect1.culc_area() = }')
    print(f'{rect2.culc_perimetr() = }, {rect2.culc_area() = }')

    
    print('\nЗадание 5:')
    rect3 = rect1 + rect2
    print(f'{rect3.width = }, {rect3.height = }, {rect3.culc_perimetr() = }, {rect3.culc_area() = }')
    rect4 = rect1 - rect2
    print(f'{rect4.width = }, {rect4.height = }, {rect4.culc_perimetr() = }, {rect4.culc_area() = }')

    print('\nЗадание 6:')
    print(f'{rect1.culc_area() = }, {rect2.culc_area() = }')
    print(f'rect1 == rect2 : {rect1 == rect2}')
    print(f'rect1 != rect2 : {rect1 != rect2}')
    print(f'rect1 < rect2 : {rect1 < rect2}')
    print(f'rect1 > rect2 : {rect1 > rect2}')
    print(f'rect1 <= rect2 : {rect1 <= rect2}')
    print(f'rect1 >= rect2 : {rect1 >= rect2}')

    print('\nДомашнее задание 1:')
    print(rect1, rect2, sep='\n', end='\n\n')
    print(repr(rect3), end='\n\n')
    print(Rectangle.__doc__)
