#  Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
#  У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
#  Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Fish:

    def __init__(self, name: str, deep: int, ) -> None:
        self.name = name
        self.deep = deep

    def specific_info(self) -> str:
        if self.deep < 10:
            return 'медководная'
        elif self.deep >= 100:
            return 'глубоководная'
        else:
            return 'среднеглубинная'


class Bird:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def specific_info(self) -> str:
        if self.height <= 0:
            return 'нелетающая'
        elif 0 < self.height <= 10:
            return 'приземная'
        elif 10 < self.height <= 100:
            return 'низколетающая'
        else:
            return 'высоколетающая'


if __name__ == '__main__':
    fish = Fish('Акула', 50)
    bird = Bird('Орёл', 500)
    print(f'{fish.name} рыба {fish.specific_info()}')
    print(f'{bird.name} птица {bird.specific_info()}')    