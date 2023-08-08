# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

class MyExceptions(Exception):
    pass


class NegativeSizeError(MyExceptions):
    
    def __init__(self, size: int | float) -> None:
        self.__size = size
    
    def __str__(self) -> str:
        if self.__size == 0:
            return f'Bad value = {self.__size}. The rectangle size value cannot be zero.'
        else:
            return f'Bad value = {self.__size}. The rectangle size value cannot be negative.'


# Поднимаем исключения в 35, 37, 46 и 57 строках
class Rectangle:
    """При создании экземпляра класса, ожидает на входе значение ширины и длины прямоугольника. При вводе только одного значения, принимает его как стороеу квадрата. Класс включает методы: расчет периметра, расчет площади, сложение  и вычетание по периметрам, сравнение по площади."""
    __slots__ = ('__width', '__height') # Задание 5

    def __init__(self, width: float, height: float = None ) -> None:
        self.__width = width
        if height is None:
            self.__height = width
        else:
            self.__height = height

        if self.__width <= 0:
            raise NegativeSizeError(self.__width)
        if self.__height <= 0:
            raise NegativeSizeError(self.__height)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeSizeError(value)
        self.__width = value
            
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise NegativeSizeError(value)
        self.__height = value

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
    

if __name__ == '__main__':
    rect = Rectangle(5, 6)
    print(rect)
    
    rect.width = 10
    rect.height = 10
    print(rect)
