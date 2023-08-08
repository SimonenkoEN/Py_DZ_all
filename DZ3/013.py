# Задание 8 из семинара 3
# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

my_dict = {'Коля': ("спички","презервативы", "палатка", "спальник", "водка"),
           'Имануил': ("стаканы","презервативы", "спальник","удочка"),
           'Бро': ("тушонка", "презервативы", "водка", "шахматы"),
           }
my_keys = []
my_vol = []
for key, volume in my_dict.items():
    my_keys.append(key)
    my_vol.append(set(volume))

# Какие вещи взяли все три друга
not_all_set = my_vol[1]
for i in range (len(my_keys)):
    not_all_set = not_all_set & my_vol[i]
print(f"{not_all_set} есть у всех")

# Какие вещи уникальны, есть только у одного друга
for i in range(len(my_keys)):
    singl_set = my_vol[i]
    for j in range (len(my_vol)):
        if i == j:
            continue
        singl_set = singl_set - my_vol[j]
    print(f"Уникальные вещи: {my_keys[i]}  - {singl_set}")

# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
all_set = set()
for i in my_vol:
    all_set = all_set | i

my_list = []
for i in all_set:
    counter = 0
    for j in my_vol:
        if i in j:
            counter += 1
    if counter == len(my_keys)-1:
        my_list.append(i)
for i in my_list:
    for j in range(len(my_vol)):
        if i not in my_vol[j]:
            print(f"{i} нет у {my_keys[j]}")