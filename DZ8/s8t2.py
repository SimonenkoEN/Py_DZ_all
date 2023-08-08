#  Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
#  После каждого ввода добавляйте новую информацию в
# JSON файл.
#  Пользователи группируются по уровню доступа.
#  Идентификатор пользователя выступает ключём для имени.
#  Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
#  При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os


def add_user(path: str) -> None:
    tmp_set = set()
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as j:
            my_dict = json.load(j)
        for _, vol in my_dict.items():
            tmp_set.update(vol.keys())
        tmp_set = set(map(int, tmp_set))
        id_num = max(tmp_set) + 1
    else:
        my_dict = {str(i): {} for i in range(1, 8)}
        id_num = 1
        
    while True:
        print(tmp_set)
        print(id_num)
        name = input('Введите имя: ')
        if name == '':
            break
        level = input('Введите уровень доступа (1-7): ')
        tmp_set.add(str(id_num))
        my_dict[level].update({id_num:name})
        with open(path, 'w', encoding='utf-8') as j:
            json.dump(my_dict, j, ensure_ascii=False, indent=2)
        id_num += 1


if __name__ == '__main__':
    add_user('s8t2.json')
    # add_user('DZ13/user.json')