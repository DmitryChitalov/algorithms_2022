from random import randint
from timeit import timeit
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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_update(lst_obj):
    n = 1
    j = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                j += 1
        if j == 0:
            return lst_obj
        n += 1
    return lst_obj


# замеры 10
orig_list_10 = [randint(-100, 100) for _ in range(10)]
print(timeit("bubble_sort(orig_list_10[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_10[:])", globals=globals(), number=1000))

# замеры 100
orig_list_100 = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list_100[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_100[:])", globals=globals(), number=1000))

# замеры 1000
orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list_1000[:])", globals=globals(), number=1000))
print(timeit(
    "bubble_sort_update(orig_list_1000[:])", globals=globals(), number=1000))

print(orig_list_1000)
print(bubble_sort_update(orig_list_1000[:]))

"""
Результаты:
0.024795799981802702
0.012791899964213371
0.7300142000894994
0.7805131000932306
81.16229269979522
89.59933080011979

Вывод:
Не во ввсех случаях будет полезна и поможет, все зависит от того, насколько
передаваемый массив уже упорядочен
"""