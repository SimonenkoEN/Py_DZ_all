#  Домашнее задание 1
#  Добавьте ко всем задачам с семинара строки документации и 
# методы вывода информации на печать.

#  Домашнее задание 2
#  Создайте класс Матрица. Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц


class Matrix():
    """Экземпляр класса Matrix ожидает на вхол матрицу и поддерживает методы для работы с матрицами:
    - вывод матрицы на печать,
    - операция сравение двух матриц (==),
    - операция сложение двух матриц (+),
    - операция умножение двух матриц (*)."""
    
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def __str__(self) -> str:
        max_length = 0
        for i in self.matrix:
            for j in i:
                if len(str(j)) > max_length:
                    max_length = len(str(j))
        s = '\n'
        for i in self.matrix:
            for j in i:
                s = f'{s}{j: >{max_length + 2}}'
            s = f'{s}\n'
        return s
    
    def __eq__(self, other: object) -> bool:
        if len(self.matrix) != len(other.matrix):
            return False
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return False
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[j] != other.matrix[j]:
                    return False
        return True
    
    def __add__(self, other: list) -> object:
        if len(self.matrix) != len(other.matrix):
            return None
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                return None
        result = []
        for i in range(len(self.matrix)):
            tmp = []
            for j in range(len(self.matrix[i])):
                tmp.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(tmp)
        return Matrix(result)

    def __mul__(self, other: object) -> object:
        if len(self.matrix[0]) != len(other.matrix):
            return None
        other_zip = list(zip(*other.matrix))
        result = []
        for i in range(len(self.matrix)):
            tmp_matrix = []
            for j in range(len(other_zip)):
                tmp = 0
                for k in range(len(self.matrix[i])):
                    tmp += self.matrix[i][k] * other_zip[j][k]
                tmp_matrix.append(tmp)
            result.append(tmp_matrix)
        return Matrix(result)
    
    def __repr__(self) -> str:
        return f'{type(self)}'


if __name__ == '__main__':
    m1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    m2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    
    matrix1 = Matrix(m1)
    matrix2 = Matrix(m2)
    print('Вывод на печать')
    print(f'matrix1 = {matrix1} matrix2 = {matrix2}')

    print('Сравнение')
    print(f'matrix1 = matrix2 : {matrix1 == matrix2}\n')

    print('Сложение')
    matrix3 = matrix1 + matrix2
    print(f'matrix1 + matrix2 = {matrix3}')

    print('Умножение')
    # для проверки матрицы взяты из учебника с готовым ответом 

    m3 = [[1, -2, 3],
         [4, 1, 7]]
    
    m4 = [[-9, 1, 0],
         [4, 1, 1],
         [-2, 2, -1]]

    matrix4 = Matrix(m3)
    matrix5 = Matrix(m4)
    print(f'matrix4 = {matrix4} matrix5 = {matrix5}')
    print(f'matrix4 * matrix5 = {matrix4 * matrix5}')
    
    print(repr(matrix2))