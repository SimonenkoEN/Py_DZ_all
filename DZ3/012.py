# Задание 7 из семинара 3
# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях

def without_count_func(my_str_):
    my_str_ = my_str_.replace(' ','')
    my_set = set(my_str_)
    my_dict = dict()
    for i in my_set:
        count = 0
        for j in my_str_:
            if i == j:
                count += 1
        my_dict[i] = count
    print (my_dict)

def with_count_func(my_str_):
    my_str_ = my_str_.replace(' ','')
    my_set = set(my_str_)
    my_dict = dict()
    for i in my_set:
        count = my_str_.count(i)      
        my_dict[i] = count
    print (my_dict)

text = input("Введите строку текста: ")

without_count_func(text)
with_count_func(text)