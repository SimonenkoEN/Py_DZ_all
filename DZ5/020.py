# ДЗ к семинару 5, задание 3
# Создайте функцию генератор чисел Фибоначчи


def fibonacci(n):
    fn1, fn2 = 0, 1
    for i in range(n + 1):
        if i < 2:
            yield i
        else:
            fn = fn1 + fn2
            fn1, fn2 = fn2, fn
            yield fn

if __name__ == '__main__':
    num = int(input('Введите целое число: '))

    for i in fibonacci(num):
        print(i, end='  ')