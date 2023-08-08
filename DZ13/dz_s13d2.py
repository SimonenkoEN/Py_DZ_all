# Задание
# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

import math

class Circle:
    def __init__(self, radius: float) -> None:
        if radius> 0:
            self.__radius= radius
        else:
            raise RadiusValueError(radius)

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius> 0:
            self.__radius= radius
        else:
            raise RadiusValueError(radius)

    def length(self) -> float:
        return 2*math.pi*self.__radius

    def area(self) -> float:
        return math.pi*self.__radius**2
    
    def __str__(self):
        return f'Окружность радиусом {self.radius}'


class MyExceptions(Exception):
    pass


class RadiusValueError(MyExceptions):
    def __init__(self, radius) -> None:
        self.radius= radius
    
    def __str__(self) -> str:
        if self.radius== 0:
            return f'Неверное значение {self.radius}. Радиус не может быть равен нулю.'
        else:
            return f'Неверное значение {self.radius}. Радиус не может быть отрицательным.'



if __name__ == '__main__':
    c= Circle(5)
    print('Длина окружности=', round(c.length(), 2))
    print('Площадь=', round(c.area(), 2))
    c.radius= -5
