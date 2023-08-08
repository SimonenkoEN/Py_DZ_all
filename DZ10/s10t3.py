#  Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
#  У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
#  Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:

    def __init__(self, ln: str, fn: str, p: str, age: int) -> None:
        self.first_name = fn
        self.last_name = ln
        self.patronymic = p
        self.__age = age

    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self) -> None:
        self.__age += 1
    
    def get_age(self) -> int:
        return self.__age
    

if __name__ == '__main__':
    pers1 = Person('Ivanov', 'Ivan', 'Ivanovich', 55)
    print(pers1.full_name())
    print(pers1.get_age())
    pers1.birthday()
    print(pers1.get_age())
    print(pers1._Person__age)