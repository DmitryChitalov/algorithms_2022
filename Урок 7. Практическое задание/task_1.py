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


lst_mass = [-50, 82, -88, -82, -53, -22, -74, -51, -61, 26, 69, -47,
            88, 92, -96, -91, 91, -42, 80, -11, -61, 95, 58, -95, 98]
# lst_mass =[]
# for i in range(200):
#     lst_mass.append(randint(-100, 100))


def buble_sort(lst):
    lst_copy = lst[:]
    lst_len = (len(lst_copy)-1)
    for x in range(lst_len):
        i = 0
        while i < lst_len - x:
            if lst_copy[i] < lst_copy[i + 1]:
                lst_copy[i], lst_copy[i + 1] = lst_copy[i + 1], lst_copy[i]
            i += 1
    return lst_copy


def buble_sort_mod(lst):
    lst_copy = lst[:]
    lst_len = (len(lst_copy)-1)
    j = 0
    for x in range(lst_len):
        i = 0
        if j == lst_len - 1:
            break
        while i < lst_len - x and j != lst_len - 1:
            if lst_copy[i] < lst_copy[i + 1]:
                lst_copy[i], lst_copy[i + 1] = lst_copy[i + 1], lst_copy[i]
                j = 0
            if lst_copy[i] > lst_copy[i + 1]:
                j += 1
            i += 1
    return lst_copy


# lst_sorted = buble_sort(lst_mass)
lst_sorted = [98, 95, 92, 91, 88, 82, 80, 69, 58, 26, -11, -22, -42, -47,
              -50, -51, -53, -61, -61, -74, -82, -88, -91, -95, -96]

print('*********** Исходный список *****************')
print(lst_mass)
print("*********** Сортировка списка buble_sort'ом *****************")
print(buble_sort(lst_mass))
print("*********** Замеры времени не сортированного списка buble_sort'ом *****************")
print(timeit("buble_sort(lst_mass)", globals=globals(), number=1000))
print("*********** Замеры времени сортированного списка buble_sort'ом *****************")
print(timeit("buble_sort(lst_sorted)", globals=globals(), number=1000))
print("*********** Сортировка списка buble_sort_mod'ом *****************")
print(buble_sort_mod(lst_mass))
print("*********** Замеры времени не сортированного списка buble_sort_mod'ом *****************")
print(timeit("buble_sort_mod(lst_mass)", globals=globals(), number=1000))
print("*********** Замеры времени сортированного списка buble_sort_mod'ом *****************")
print(timeit("buble_sort_mod(lst_sorted)", globals=globals(), number=1000))


"""
Модифицированная функция отрабатывает быстрее если список уже отсортированный,
но в случаее если список не отсортированный обычная версия функции работает быстрее.
"""
