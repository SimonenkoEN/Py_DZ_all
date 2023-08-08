# ДЗ к семинару 3, задание 3
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

backpack = int(input ("Введите грузоподьемность рюкзака: "))
things_dict = {'спальник' : 3, 
               'спички' : 0.2,
               'тулетная_бумага' : 1,
               'перочинный_нож' : 0.3,
               'дождевик' : 2,
               'фляжка_с_водой' : 1,
               'тушонка' : 3,
               'макароны' : 2,
               'шахматы' : 2,
               'презервативы' : 0.5,
               'две_бутылки_вина' : 3,
               'бутылка_водки' : 1.5,
              }
my_keys = []
my_vol = []
for key, value in things_dict.items():
    my_keys.append(key)
    my_vol.append(value)
for i in range(0, len(my_vol)):
    for j in range(i + 1, len(my_vol)):
        if my_vol[j] < my_vol[i]:
            my_keys[i], my_keys[j] = my_keys[j], my_keys[i]
            my_vol[i], my_vol[j] = my_vol[j], my_vol[i]
res = 0
for i in range(1, len(my_vol)):
    res += my_vol[i]
    if res <= backpack:
        print(my_keys[i])
    else:
        res -= my_vol[i]
        break
print(f'Всего вещей на {res} кг')