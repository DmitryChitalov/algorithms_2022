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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def sort_bubble_smart(lst_obj):
    """Функция с проверкой перестановок после прохода"""
    n = 1
    orig_list = lst_obj[:]
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if orig_list == lst_obj:
            break
        else:
            n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "sort_bubble_smart(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "sort_bubble_smart(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "sort_bubble_smart(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Функция с проверокой перестановок после каждого прохода не очень эффективна так как согласно замерам не даёт 
существенного выигрыша во времени, как показано на замерах 10, 100, 1000.
А в случае массива 1000 элементов, работает значительно дольше из-за проверок!
замеры 10:
0.02638279995881021
0.02913450001506135
замеры 100:
1.3651593000395223
1.132736700004898
замеры 1000:
141.38191529997857
178.0680571999983
"""
