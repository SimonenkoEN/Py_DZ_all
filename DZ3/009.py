# ДЗ к семинару 3, задание 1
# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

from random import randint

my_list = [randint(1, 10) for i in range(10)]

res_list = []
my_set = set(my_list)
for i in my_set:
    counter = my_list.count(i)
    if counter > 1:
        res_list.append(i)

print (my_list)
print (res_list)