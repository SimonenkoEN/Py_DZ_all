# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
#  Напишите к ним тесты.
#  2-5 тестов на задачу в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

from my_exc import *
import math

class Circle:
    def __init__(self, radius: float) -> None:
        if radius> 0:
            self.__radius= radius
        else:
            raise RadiusValueError(radius)

    @property
    def radius(self):
        """
        >>> Circle(1).radius
        1
        """
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius> 0:
            self.__radius= radius
        else:
            raise RadiusValueError(radius)

    def length(self) -> float:
        """
        >>> round(Circle(1).length(), 2)
        6.28
        """
        return 2*math.pi*self.__radius

    def area(self) -> float:
        """
        >>> round(Circle(1).area(), 2)
        3.14
        """
        return math.pi*self.__radius**2
    
    def __str__(self):
        return f'Окружность радиусом {self.radius}'
  
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
