# Задача 1 домашнего задания семинара 8
#  Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
#  Результаты обхода сохраните в файлы json, csv и pickle.
#  Для дочерних объектов указывайте родительскую директорию.
#  Для каждого объекта укажите файл это или директория.
#  Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий

import os
import json
import csv
import pickle


def get_data(json_file: str, csv_file: str, pickle_file: str, path_: str = None) -> None:
    data, _ = _get_data(path_)
    _data_to_json(data, json_file)
    _data_to_csv(data, csv_file)
    _data_to_pickle(data, pickle_file)

def _get_data(path_: str = None) -> list:
    if path_ is not None:
        os.chdir(path_)
    path_ = os.getcwd()
    list_dir = os.listdir(path_)
    list_all = []
    d_size = 0
    for i in range(len(list_dir)):
        tmp = os.getcwd().split('\\')
        parent = ''.join([tmp[-1], '\\'])
        current_path = os.path.join(os.getcwd(), list_dir[i])
        if os.path.isdir(list_dir[i]):
            tmp_list, tmp_size = _get_data(current_path)
            list_all.append([parent, list_dir[i], '<dir>', tmp_size])
            tmp_index = list_all.index([parent, list_dir[i], '<dir>', tmp_size])
            for j in tmp_list:
                if '<dir>' in j:
                    tmp_size += j[3]
                list_all.append(j)
            list_all[tmp_index][3] = tmp_size
            os.chdir('..')
        if os.path.isfile(list_dir[i]):
            f_size = os.path.getsize(list_dir[i])
            d_size += f_size
            list_all.append([parent, list_dir[i], '<file>', f_size])
    return [list_all, d_size]


def _data_to_json(lst: list, json_file: str) -> None:
    j_dict = {}
    for i in lst:
        j_dict[i[1]] = {'parent_dir': i[0],
                        'type': i[2], 
                        'size': i[3]}
    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(j_dict, jf, indent=2)


def _data_to_csv(lst: list, csv_file: str) -> None:
    csv_list = []
    for i in lst:
        obj_dir, obj, obj_type, size = i
        csv_list.append({'parent_dir': obj_dir,
                         'object': obj,
                         'type': obj_type,
                         'size': size})
    with open(csv_file, 'w', newline='', encoding='utf-8') as cf:
        csv_write = csv.DictWriter(cf, fieldnames=('parent_dir', 'object', 'type', 'size'), dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(csv_list)


def _data_to_pickle(lst: list, pickle_file: str) -> None:
    with open(pickle_file, 'wb') as pf:
        pickle.dump(lst, pf)


if __name__ == '__main__':
    get_data('data.json', 'data.csv', 'data.pickle')