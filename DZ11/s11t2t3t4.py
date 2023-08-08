#  задание 2
#  Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
#  При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
#  list-архивы также являются свойствами экземпляра

# Задание 3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание 4
#  Доработаем класс Архив из задачи 2.
#  Добавьте методы представления экземпляра для программиста
# и для пользователя.


class Archive:
    """При создании нового экземпляра класса, хранит все введенные ранее параметры в соответствующих списках"""
    __instance = None
    
    def __init__(self, text: str, number: int) -> None:
        self.text = text
        self.number = number

    def __new__(cls, text: str, num: int):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.archive_text = []
            cls.__instance.archive_number = []
        else:
            cls.__instance.archive_text.append(cls.__instance.text)
            cls.__instance.archive_number.append(cls.__instance.number)
        return cls.__instance

    def __repr__ (self) -> str:
        return f'{self.text = }, {self.number = }\n{self.archive_text = }, {self.archive_number = }'

    def __str__(self) -> str:
        return f'{self.text}, {self.number}'


if __name__ == '__main__':
    print('Задание 2:')
    s1 = Archive('Один', 1)
    print(s1.archive_text, s1.archive_number)
    s2 = Archive('Два', 2)
    print(s2.archive_text, s2.archive_number)
    s3 = Archive('Три', 3)
    print(s3.archive_text, s3.archive_number)

    print('\nЗадание 3:')
    print(Archive.__doc__)

    print('\nЗадание 4:')
    print(repr(s3))
    print(s3)

