# Задание №4
#  Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
#  Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
#  Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json


class User():

    def __init__(self, name: str, user_id: int, level: int) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self) -> str:
        return f'{self.user_id} : {self.name} - {self.level}'


def get_data(path: str) -> set:
    users = set()
    try:
        with open(path, 'r', encoding='utf-8') as jf:
            data = json.load(jf)
    except FileNotFoundError:
        print('Файл не найден')
        data = {}
    for level, value in data.items():
        for user_id, name in value.items():
           users.add(User(name, int(user_id), int(level))) 
    return users

if __name__ == '__main__':
    data = get_data('DZ13/users.json')
    for i in data:
        print(i)