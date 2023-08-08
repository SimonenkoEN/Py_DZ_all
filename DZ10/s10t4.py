#  Создайте класс Сотрудник.
#  Воспользуйтесь классом человека из прошлого задания.
#  У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from s10t3 import Person


class Employee(Person):

    MAX_LEVEL = 7

    def __init__(self, emp_id: int, *args, **kwargs) -> None:
        if 100_000 <= emp_id <= 999_999:
            self.__emp_id = emp_id
        else:            
            self.__emp_id = 123456
        super().__init__(*args, **kwargs)

    def get_id(self) -> int:
        return self.__emp_id

    def access_level(self):
        return sum([int(num) for num in str(self.__emp_id)]) % self.MAX_LEVEL


if __name__ == '__main__':
    emp1 = Employee(1, 'Ivanov', 'Ivan', 'Ivanovich', 35)
    print(f'{emp1.get_id()} {emp1.full_name()} {emp1.access_level()}')