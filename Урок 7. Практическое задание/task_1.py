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
from random import randint
from timeit import timeit




t_lst_2000 = [randint(-100, 100) for i in range(2000)]
t_lst_1000 = [randint(-100, 100) for i in range(1000)]
t_lst_10 = [randint(-100, 100) for i in range(10)]


def bubble_sort_reverse(lst):
    """пузырёк по убыванию"""
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_reverse_f(lst):
    """пузырёк по убыванию с проверкой на готовность"""
    for i in range(len(lst)):
        flag = False
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                flag = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if flag is False:
            return lst
    return lst
#bubble_sort_reverse(t_lst)

print(timeit("bubble_sort_reverse(t_lst_2000[:])", globals=globals(), number=100))
print(timeit("bubble_sort_reverse_f(t_lst_2000[:])", globals=globals(), number=100))

print(timeit("bubble_sort_reverse(t_lst_1000[:])", globals=globals(), number=100))
print(timeit("bubble_sort_reverse_f(t_lst_1000[:])", globals=globals(), number=100))

print(timeit("bubble_sort_reverse(t_lst_10[:])", globals=globals(), number=100))
print(timeit("bubble_sort_reverse_f(t_lst_10[:])", globals=globals(), number=100))

"""
76.409380239
74.201837013
эффективней на ~3%
18.888349093999977
18.44169581099999
эффективней на ~3%
0.002240833000001885
0.0017053579999810609
эффективней на ~25%

модернизированная функция работает быстрее, но максимальная эффективность на малых списках
"""
