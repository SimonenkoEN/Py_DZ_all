#  Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
#  Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
#  Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import os
import pickle
import csv


def pickle_to_csv(pickle_file: str, csv_file: str) ->  None:
    if os.path.isfile(pickle_file):
        with open(pickle_file, 'rb') as pf:
            data = pickle.load(pf)
    data_list = []
    for level, user in data.items():
        for id_num, name in user.items():
            data_list.append({'level': int(level), 'ID': int(id_num), 'name': name})
    with open(csv_file, 'w', newline='', encoding='utf-8') as c:
        csv_write = csv.DictWriter(c, fieldnames=('level', 'ID', 'name'), dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data_list)
    

if __name__ == '__main__':
    pickle_to_csv('s8t2.pickle', 's8t6.csv')
