#  Задание 1
#  Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
#  Экземпляр должен запоминать последние k значений.
#  Параметр k передаётся при создании экземпляра.
#  Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов..

# Задание 2
#  Доработаем задачу 1.
#  Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json
import time
from collections import deque


class Factorial:
    
    def __init__(self, k: int) -> None:
        self.results = deque(maxlen=k)

    def __call__(self, number : int, *args, **kwds) -> int:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
        self.results.append({number: factorial})
        return self.results[-1]

    def get_results(self) -> deque:
        return self.results
    
    # Задание 2
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sec = time.time()
        struct = time.localtime(sec)
        t = time.strftime('%d.%m.%Y %H-%M-%S', struct)
        j_dict = {}
        while self.results:
            j_dict.update(self.results.popleft())
        with open(f'DZ12/s12_t2({t}).json', 'w', encoding='utf-8') as jf:
            json.dump(j_dict, jf, indent=2)


if __name__ == '__main__':
    fact = Factorial(3)
    print(fact(3))
    print(fact(4))
    print(fact(5))
    print(fact(6))
    print(fact.get_results())

    with fact as jf:
        print(jf)