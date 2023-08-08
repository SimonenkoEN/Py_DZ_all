# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов

import os
import json
import pickle


def json_to_pickle(path_dir: str = None) -> None:
    if path_dir is not None:
        os.chdir(path_dir)
    for element in os.listdir():
        if os.path.isfile(element) and element[-4:] == 'json':
            print(element)
            with (open(element, 'r', encoding='utf-8') as jf,
                  open(f'{element[:-4]}pickle', 'wb') as pf
            ):
                data = json.load(jf)
                pickle.dump(data, pf)


if __name__ == '__main__':
    json_to_pickle()