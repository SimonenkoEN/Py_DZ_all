# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint as rnd, choice as ch

MIN_NAME = 4
MAX_NAME = 7
VOWEL_LETTERS = 'aeijouy'
CONSONANT_LETTERS = 'bcdfghklmnpqrstvwxz'


def get_rnd_name(names:int, fail_name:str='name.txt') -> None:
    for _ in range(names):
        name = ''
        for i in range(rnd(MIN_NAME, MAX_NAME)):
            if i % 2:
                name = ''.join(name + ch(VOWEL_LETTERS))
            else:
                name = ''.join(name + ch(CONSONANT_LETTERS))
        name = name.capitalize()
        print(name)
        with open(fail_name, 'a', encoding='utf-8') as f:
            f.write(f'{name}\n')

if __name__ == '__main__':
    get_rnd_name(4, 't2.txt')