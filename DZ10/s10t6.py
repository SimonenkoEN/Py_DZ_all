#  Доработайте задачу 5.
#  Вынесите общие свойства и методы классов в класс
# Животное.
#  Остальные классы наследуйте от него.
#  Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name
    
    def specific_info(self) -> str:
        return 'это животное'

class Fish(Animal):

    def __init__(self,name: str, deep: int) -> None:
        super().__init__(name)
        self.deep = deep

    def specific_info(self) -> str:
        if self.deep < 10:
            return 'рыба медководная'
        elif self.deep >= 100:
            return 'рыба глубоководная'
        else:
            return 'рыба среднеглубинная'


class Bird(Animal):

    def __init__(self, name: str, height: int) -> None:
        super().__init__(name)
        self.height = height

    def specific_info(self) -> str:
        if self.height <= 0:
            return 'птица нелетающая'
        elif 0 < self.height <= 10:
            return 'птица приземная'
        elif 10 < self.height <= 100:
            return 'птица низколетающая'
        else:
            return 'птица высоколетающая'


if __name__ == '__main__':
    fish = Fish('Акула', 50)
    bird = Bird('Курица', 0)
    for animal in [fish, bird]:
        print(f'{animal.name} {animal.specific_info()}')