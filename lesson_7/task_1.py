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
print(timeit("bubble_sort_update(orig_list_10[:])", globals=globals(), number=1000))

# замеры 100
orig_list_100 = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort(orig_list_100[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_update(orig_list_100[:])", globals=globals(), number=1000))

# замеры 1000
orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort(orig_list_1000[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_update(orig_list_1000[:])", globals=globals(), number=1000))

print(orig_list_1000)
print(bubble_sort_update(orig_list_1000[:]))

"""
0.014321900000000005
0.014244099999999996
0.9257382000000001
0.9903584999999999
94.42873660000001
96.56741939999999

Не во всех замерах доработка была эффективна. 
Доработка будет помогать в зависимости от того, насколько массив уже упорядочен.
На эффективность также повлияет и размер массива. Чем меньше массив, тем больше шансов на уменьшение времени.
"""
