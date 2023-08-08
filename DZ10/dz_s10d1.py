# Доработаем задачи 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных 
# классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа
# и верните его из класса-фабрики.

from s10t6 import Animal, Fish, Bird


class AnimalFactory:

    def __init__(self) -> None:
        pass
    
    def create(self, type_animal: str,  *args, **kwargs):
        self.type_animal = type_animal
        if self.type_animal is 'fish':
            return Fish(*args, **kwargs)
        elif self.type_animal is 'bird':
            return Bird(*args, **kwargs)
        else:
            return Animal(*args, **kwargs)


if __name__ == '__main__':
    fish = AnimalFactory().create('fish', 'Акула', 50)
    bird1 = AnimalFactory().create('bird','Курица', 0)
    bird2 = AnimalFactory().create('bird','Орел', 500)
    cat = AnimalFactory().create('cat','Мурка')
    for animal in [fish, bird1, bird2, cat]:
        print(f'{animal.name} {animal.specific_info()}')