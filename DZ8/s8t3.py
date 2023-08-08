# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def json_to_csv(json_file: str, csv_file: str) -> None:
    with open(json_file, 'r', encoding='utf-8') as j:
        j_data = json.load(j)
    j_list = []
    for level, user in j_data.items():
        for id_num, name in user.items():
            j_list.append({'level': int(level), 'ID': int(id_num), 'name': name})

    with open(csv_file, 'w', newline='', encoding='utf-8') as c:
        csv_write = csv.DictWriter(c, fieldnames=('level', 'ID', 'name'), dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(j_list)


if __name__ == '__main__':
    json_to_csv('s8t2.json', 's8t3.csv')