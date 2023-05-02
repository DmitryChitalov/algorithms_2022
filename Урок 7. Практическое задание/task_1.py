"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from timeit import timeit
from random import randint



def bubble_sort_flag(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
    return lst_obj



def bubble_sort(lst_obj):
    for j in range(len(lst_obj)-1):
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]

    return lst_obj


orig_list = [randint(-100, 100) for i in range(10)]
print(
    timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=20))

orig_list = [randint(-100, 100) for i in range(100)]

print(
    timeit(
        "bubble_sort_flag(orig_list[:])",
        globals=globals(),
        number=20))

print(15*'*')

orig_list = [randint(-100, 100) for i in range(10)]
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=20))
orig_list = [randint(-100, 100) for i in range(100)]
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=20))

"""
0.0009989999999999999 bubble_sort_flag
0.08313849999999998 bubble_sort_flag
***************
0.0011471999999999871 bubble_sort
0.08609710000000001 bubble_sort
В функции bubble_sort оценивается полный список, а в функции bubble_sort_flag
предотвращается ненужную оценку, используя логический флаг и проверяя, были ли 
сделаны какие-либо свопы в предыдущем разделе.
Исходя из результатов доработка в функции bubble_sort_flag не оказалась ээфективней
вложенных циклов в bubble_sort.
"""
