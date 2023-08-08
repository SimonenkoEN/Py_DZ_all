#  Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых

import csv


class Validator:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value.istitle():
            raise ValueError('Первая буква должна быть прописной!')
        if not value.isalpha():
            raise ValueError('Вводить можно только буквы!')
        setattr(instance, self.param_name, value)


class Student:
    __last_name = Validator()
    __first_name = Validator()
    __patronymic = Validator()

    def __init__(self, last_name: str, first_name: str, patronymic: str) -> None:
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__subjects = {}
        self.__score = []
        self.__test = []

        with open('DZ12/subjects.csv', 'r', newline='', encoding='utf-8') as cf:
            for line in cf:
                self.__subjects[line[:-2]] = {'оценки': [], 'тесты': []}

    def __call__(self, subject: str, *args, **kwargs):
        for i in self.__score:
            self.__subjects[subject]['оценки'].append(i)
        self.__score.clear()
        for i in self.__test:
            self.__subjects[subject]['тесты'].append(i)
        self.__test.clear()

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 2 <= value <= 5 and isinstance(value, int):
            self.__score.append(value)
        else:
            raise ValueError('Значение должно быть целым числом от 2 до 5!')
    
    @score.deleter
    def score(self):
        self.__score.pop()

    @property
    def test(self):
        return self.__test
    
    @test.setter
    def test(self, value):
        if  0 <= value <= 100 and isinstance(value, int):
            self.__test.append(value)
        else:
            raise ValueError('Значение должно быть целым числом от 0 до 100!')
    
    @test.deleter
    def test(self):
        self.__test.pop()

    def full_name(self):
        return f'{self.__last_name} {self.__first_name} {self.__patronymic}'
    
    def mean_tests(self, subject: str):
        if len(self.__subjects[subject]['тесты']) != 0:
            return round(sum(self.__subjects[subject]['тесты']) / len(self.__subjects[subject]['тесты']), 2)
        return 0

    def mean_scores(self, subject: str):
        if len(self.__subjects[subject]['оценки']) != 0:
            return round(sum(self.__subjects[subject]['оценки']) / len(self.__subjects[subject]['оценки']), 2)
        return 0

    def mean_subjects(self):
        means_lst = []
        for key1, value1 in self.__subjects.items():
            if len(value1['оценки']) != 0:
                mean_subj = sum(value1['оценки']) / len(value1['оценки'])
            else:
                continue
            means_lst.append(mean_subj)
        return round(sum(means_lst) / len(means_lst), 2)

    def full_raport(self):
        print(self.full_name())
        print('Предметы:')
        for key1, value1 in self.__subjects.items():
            print(key1)
            for key2, value2 in value1.items():
                print(f'\t{key2}:', end=' ')
                for i in value2:
                    print(i, end=', ')
                print()
        print(f'\nСредняя оценка по всем предметам: {self.mean_subjects()}')

    def __str__(self) -> str:
        return f'{self.full_name()}: {self.mean_subjects()}'


if __name__ == '__main__':
    std1 = Student('Петров', 'Петр', 'Петрович')

    std1.score = 3 # оценка
    std1('subj1') # сохранение оценок и тестов в с соответствующий предмет

    std1.test = 58 # тест
    std1('subj1') 

    std1.score = 2
    del std1.score # удаление последней введенной, но не сохраненной оценкии
    std1.score = 4
    std1.test = 72
    std1.score = 5
    std1('subj2') # сохранение оценок и тестов в с соответствующий предмет
    
    std1.score = 5
    std1.test = 84
    std1.test = 69
    std1('subj3')
    
    std1.full_raport() # полный отчет по предметам
    
    print(f'\nСредняя оценка по subj3: {std1.mean_scores("subj3")}') # среднее значение оценок по предмету
    print(f'Средний балл по тестам по subj3: {std1.mean_tests("subj3")}') # среднее значение тестов по предмету
    print(std1) # среднее значение оценок по всем предметам