# Задание №2
#  Создайте функцию аналог get для словаря.
#  Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
#  При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
#  Реализуйте работу через обработку исключений.


def my_get(self_dict: dict, key, value = None):
    tmp = value
    try:
        tmp = self_dict[key]
    except KeyError as e:
        pass
    return tmp


if __name__ == '__main__':
    d = {'a': 15}
    print(my_get(d, 'a'))