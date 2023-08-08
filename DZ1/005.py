# Задача 3, ДЗ, Семинар 1
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки

from random import randint

rnd = randint(0, 1000) 
print("Угадай число от 0 до 1000 за 10 попыток")
for i in range(1, 11):
    print("Попытка №", i, end=': ')
    number = int(input())
    if number == rnd:
        print("Верно! Загадано число ", rnd)
        break
    elif number > rnd:
        print("Нет! Загаданное число меньше")
    else:
         print("Нет! Загаданное число больше")
print("Конец игры!")


