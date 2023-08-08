# задание 6
#  Изменяем класс прямоугольника.
#  Заменяем пару декораторов проверяющих длину и ширину на дескриптор с 
# валидацией размера.


class ValidateSize:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value <= 0:
            raise ValueError('Значение должно быть больше 0!')


class Rectangle:
    """При создании экземпляра класса, ожидает на входе значение ширины и длины прямоугольника. При вводе только одного значения, принимает его как стороеу квадрата. Класс включает методы: расчет периметра, расчет площади, сложение  и вычетание по периметрам, сравнение по площади."""
    __width = ValidateSize()
    __height = ValidateSize()

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


if __name__ == '__main__':
    rect = Rectangle(-5, 6)
    print(rect)
