# Задание 9 из семинара 1
# Выведите в консоль таблицу умножения от 2х2 до 9х10
# как на школьной тетрадке

for i in range(2, 11):
    for j in range(2, 6):
        if i == 10:
            print(j, 'x', i, '=', j * i, end='   ')
        elif (j*i) > 9:
            print(j, 'x', i, ' =', j * i, end='   ')
        else: 
            print(j, 'x', i, ' =', j * i, end='    ')
    print()
print()
for i in range(2, 11):
    for j in range(6, 10):
        if i == 10:
            print(j, 'x', i, '=', j * i, end='   ')
        else:
            print(j, 'x', i, ' =', j * i, end='   ')
    print()