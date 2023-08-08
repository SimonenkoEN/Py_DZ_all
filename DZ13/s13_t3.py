# Задание №3
#  Создайте класс с базовым исключением и дочерние классы-
# исключения:
# - ошибка уровня,
# - ошибка доступа.


class MyExceptions(Exception):
    pass


class SetLevelEror(MyExceptions):
    
    def __init__(self) -> None:
        pass    
    
    def __str__(self) -> str:
        return 'Level Eror'


class SetAccessEror(MyExceptions):

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return 'Access denied'