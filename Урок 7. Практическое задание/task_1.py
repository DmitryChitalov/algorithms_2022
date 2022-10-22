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


def from_max_to_min_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list_10 = [randint(-100, 100) for _ in range(10)]
print(from_max_to_min_bubble_sort(orig_list_10[:]))


def mody_from_max_to_min_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        counter = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                counter = 1
        if counter == 0:
            return lst_obj
        n += 1
    return lst_obj


print(mody_from_max_to_min_bubble_sort(orig_list_10[:]))


# замеры 10 from_max_to_min_bubble_sort
print(
    timeit(
        "from_max_to_min_bubble_sort(orig_list_10[:])",
        globals=globals(),
        number=1000))

orig_list_100 = [randint(-100, 100) for _ in range(100)]

# замеры 100 from_max_to_min_bubble_sort
print(
    timeit(
        "from_max_to_min_bubble_sort(orig_list_100[:])",
        globals=globals(),
        number=1000))

orig_list_1000 = [randint(-100, 100) for _ in range(1000)]

# замеры 1000 from_max_to_min_bubble_sort
print(
    timeit(
        "from_max_to_min_bubble_sort(orig_list_1000[:])",
        globals=globals(),
        number=1000))

# замеры 10 mody_from_max_to_min_bubble_sort
print(
    timeit(
        "mody_from_max_to_min_bubble_sort(orig_list_10[:])",
        globals=globals(),
        number=1000))

# замеры 100 mody_from_max_to_min_bubble_sort
print(
    timeit(
        "mody_from_max_to_min_bubble_sort(orig_list_100[:])",
        globals=globals(),
        number=1000))

# замеры 1000 mody_from_max_to_min_bubble_sort
print(
    timeit(
        "mody_from_max_to_min_bubble_sort(orig_list_1000[:])",
        globals=globals(),
        number=1000))


# Смысл в модификаци есть если часть элементов списка уже отсортированы.
# Чем больше элементов отсортированы тем сильнее модификация ускорит выполнение.
