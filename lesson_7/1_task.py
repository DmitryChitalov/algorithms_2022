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


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def upd_bubble_sort(lst):
    n = 1
    flag = True
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                flag = False
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        if flag:
            return lst
        n += 1
    return lst


ex_lst = [randint(-100, 100) for _ in range(100)]

print(bubble_sort(ex_lst[:]))
print(upd_bubble_sort(ex_lst[:]))

print(timeit('bubble_sort(ex_lst[:])', globals=globals(), number=1000))  # 0.55
print(timeit('upd_bubble_sort(ex_lst[:])', globals=globals(), number=1000))  # 0.57

bubble_sort(ex_lst)

print(timeit('bubble_sort(ex_lst[:])', globals=globals(), number=1000))  # 0.29
print(timeit('upd_bubble_sort(ex_lst[:])', globals=globals(), number=1000))  # 0.006

"""
Алгоритм работает в разы быстрее при передаче в функцию отсортированного списка, 
в противном случае разницы нет
"""
