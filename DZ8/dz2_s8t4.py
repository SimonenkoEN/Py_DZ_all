#  Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
#  Дополните id до 10 цифр незначащими нулями.
#  В именах первую букву сделайте прописной.
#  Добавьте поле хеш на основе имени и идентификатора.
#  Получившиеся записи сохраните в json файл, где каждая
# строка csv файла представлена как отдельный json словарь.
#  Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json


def data_modifications(csv_file: str, json_file: str) -> None:
    with open(csv_file, 'r', encoding='utf-8') as cf:
        data = list(cf)
    j_dict = {}
    for i in range(1, len(data)):
        level, id_user, name_user = data[i][:-1].split('\t')
        id_user = ''.join(['0' * (10 - len(id_user)), id_user])
        hash_user = hash(name_user + id_user)
        j_dict[id_user] = {'name': name_user, 
                           'hash': hash_user, 
                           'level': level}
    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(j_dict, jf, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    data_modifications('s8t3.csv', 's8t4.json')