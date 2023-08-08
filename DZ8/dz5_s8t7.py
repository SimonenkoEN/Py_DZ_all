#  Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
#  Распечатайте его как pickle строку

import csv
import pickle


def csv_to_pickle_str(csv_file: str) ->  bytes:
    with open(csv_file, 'r', encoding='utf-8') as cf:
        data = list(cf)
    return pickle.dumps(data)


if __name__ == '__main__':
    print(csv_to_pickle_str('s8t6.csv'))