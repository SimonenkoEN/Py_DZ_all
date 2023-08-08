# Задание 8 из семинара 1
# Нарисовать в консоли ёлку спросив у пользователя 
# количество рядов

row = abs(int(input('Сколько рядов у ёлки? ')))
star = 1
space = row - 1
for i in range(1, row+1):
    print(' ' * space, '*' * star)
    space -= 1
    star += 2