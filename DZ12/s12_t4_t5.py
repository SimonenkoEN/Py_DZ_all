# Задание 4
#  Доработайте класс прямоугольник из прошлых семинаров.
#  Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
#  Используйте декораторы свойств.

# задание 5
#  Доработаем прямоугольник и добавим экономию памяти для хранения свойств
# экземпляра без словаря __dict__.


from sys import getsizeof


class Rectangle:
    """При создании экземпляра класса, ожидает на входе значение ширины и длины прямоугольника. При вводе только одного значения, принимает его как стороеу квадрата. Класс включает методы: расчет периметра, расчет площади, сложение  и вычетание по периметрам, сравнение по площади."""
    __slots__ = ('__width', '__height') # Задание 5

    def __init__(self, width: float, height: float = None ) -> None:
        self.__width = width
        if height is None:
            self.__height = width
        else:
            self.__height = height
    
    def culc_perimetr(self) -> float:
        return 2 * (self.__height + self.__width)

    def culc_area(self) -> float:
        return self.__height * self.__width
    
    def __add__(self, other):
        perimetr = self.culc_perimetr() + other.culc_perimetr()
        width = self.__width + other.width
        height = perimetr / 2 - width
        return Rectangle(width, height)
    
    def __sub__(self, other):
        perimetr = abs(self.culc_area() - other.culc_area())
        width = abs(self.__width - other.width)
        height = perimetr / 2 - width
        return Rectangle(width, height)

    def __eq__(self, other):
        return self.culc_area() == other.culc_area()

    def __lt__(self, other):
        return self.culc_area() < other.culc_area()

    def __le__(self, other):
        return self.culc_area() <= other.culc_area()

    def __str__(self) -> str:
        if self.__width == self.__height:
            return f'Квадрат со сторонами {self.__width}'
        return f'Прямоугольник со сторонами {self.__width} и {self.__height}'

    def __repr__(self) -> str:
        return f'{type(self.__width)} {self.__width = }\n{type(self.__height)} {self.__height = }'

    # Задание 4
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            raise ValueError('Значение должно быть больше 0!')
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value > 0:
            self.__height = value
        else:
            raise ValueError('Значение должно быть больше 0!')
    

if __name__ == '__main__':
    rect = Rectangle(5, 6)
    print(rect)
    
    # Задание 4
    rect.width, rect.height = 3, 4
    print(rect)

    # Задание 5
    print(rect.__slots__)
    print(getsizeof(rect))