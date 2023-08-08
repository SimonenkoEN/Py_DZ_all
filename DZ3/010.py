# ДЗ к семинару 3, задание 2
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

def get_formated_text(my_str_):
    my_str_ = my_str_.lower()
    symb_list = ['.', ',', ';', ':', '!', '?', '"', '(', ')']
    for i in symb_list:
        counter = my_str_.find(i)
        if counter > 0:
            my_str_ = my_str_.replace(i, '')
        my_list = my_str_.split(' ')
    return my_list

def counting_words(my_list_):
    my_set = set(my_list_)
    my_dict = dict()
    for i in my_set:
        counter = my_list_.count(i)
        my_dict[i] = counter
    return my_dict

def get_top10_words(my_dict_):
    my_keys = []
    my_vol = []
    for key, value in my_dict_.items():
        my_keys.append(key)
        my_vol.append(value)
    for i in range(0, len(my_vol)):
        for j in range(i + 1, len(my_vol)):
            if my_vol[j] > my_vol[i]:
                my_keys[i], my_keys[j] = my_keys[j], my_keys[i]
                my_vol[i], my_vol[j] = my_vol[j], my_vol[i]
    for i in range(10):
        if my_vol[i] in (2, 3, 4):
            print (f'{i + 1}. "{my_keys[i]}" встречается {my_vol[i]} раза')
        else:
            print (f'{i + 1}. "{my_keys[i]}" встречается {my_vol[i]} раз')

if __name__ == '__main__':
    big_text = 'Корова дает, корова не дает, корова дура. Дура она корова! Она как полная дура вообще? Остальные коровы тоже не очень умные. Они дуры, как и эта корова'
    words_list = get_formated_text(big_text)
    words_dict = counting_words(words_list)
    get_top10_words(words_dict)