# Задание №5
#  Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# - загрузка данных (функция из задания 4)
# - вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# - добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

from s13_t3 import *
from s13_t4 import User, get_data


class MyProject():

    def __init__(self) -> None:
        self.__user = None
        self.__users = set()
        self.__project_users = set()

    def load_users(self, path: str) -> None:
        self.__users.update(get_data(path))

    def check_access(self, name: str, user_id: int, level: int = 0):
        tmp_user = User(name, user_id, level)
        if tmp_user not in self.__users:
            raise SetAccessEror()
        for i in self.__users:
            if tmp_user == i:
                self.__user = tmp_user
                print(self.__user)
    
    def add_in_proj(self, level: int):
        if level > self.__user.level:
            raise SetLevelEror()
        self.__project_users.add(self.user)
            

if __name__ == '__main__':
    proj1 = MyProject()
    proj1.load_users('DZ13/users.json')
    proj1.check_access('John', 1, 5)
