# Задание 3
#  Создайте класс-генератор.
#  Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
#  Если переданы два параметра, считаем step=1.
#  Если передан один параметр, также считаем start=1.


class FactorialGenerator:
    
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.start = 1
            self.stop = args[0]
            self.step = 1
        if len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        if len(args) == 3:
            self.start, self.stop, self.step = args    

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start <= self.stop:
            factorial = 1
            for i in range(1, self.start + 1):
                factorial *= i
            self.start += self.step
            return factorial
        raise StopIteration


if __name__ == '__main__':
    fg1 = FactorialGenerator(8)
    fg2 = FactorialGenerator(3, 8)
    fg3 = FactorialGenerator(3, 8, 2)
    
    for i in fg1, fg2, fg3:
        for f in i:
            print(f)
        print()