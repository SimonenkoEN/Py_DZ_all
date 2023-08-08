# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def get_result_file(fail_1:str, fail_2:str, fail_res:str='result.txt') -> None:
    with (open(fail_1, 'r', encoding='utf-8') as f1, 
          open(fail_2, 'r', encoding='utf-8') as f2,
    ):
        names = list(f2)
        numbers = list(f1)
    
    for idx in range(len(names)):
        names[idx] = names[idx][:-1]
    for idx in range(len(numbers)):
        a, b = numbers[idx][:-1].split('|')
        numbers[idx] = int(a) * float(b)

    with open(fail_res, 'w', encoding='utf-8') as f3:
        i, j = 0, 0
        for _ in range(max(len(names), len(numbers))):
            if i == len(names):
                i = 0
            if j == len(numbers):
                j = 0
            if numbers[j] < 0:
                f3.write(' '.join([names[i].lower(), str(abs(numbers[j])), '\n']))
            else:
                f3.write(' '.join([names[i].upper(), str(round(numbers[j])), '\n']))
            i += 1
            j += 1

if __name__ == '__main__':
    get_result_file('t1.txt', 't2.txt', 't3.txt')