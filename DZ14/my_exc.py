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
