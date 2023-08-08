# ДЗ к семинару 4, задание 1
# Напишите функцию для транспонирования матрицы


def transposing_matrix(matrix):
    t_matrix, tmp = [], []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            tmp.append(matrix[j][i])
        t_matrix.append(tmp.copy())
        tmp.clear()
    return t_matrix


def transposing_matrix_2(matrix):
    return list(zip(*matrix))


if __name__ == '__main__':
    print(transposing_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(transposing_matrix_2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))