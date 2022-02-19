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
    cnt = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            cnt += 1
        n += 1
    return cnt, lst_obj


def bubble_sort_flag(array):
    cnt = 0
    flag = True
    for j in range(len(array) - 1):
        if not flag:
            return cnt, array
        flag = False
        for i in range(len(array) - 1 - j):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = True
            cnt += 1
    return cnt, array


my_list = [randint(-100, 100) for x in range(1000)]
print('Пузырек = ',
      timeit('bubble_sort(my_list[:])', globals=globals(), number=100))
print('Пузырек с флагом = ',
      timeit('bubble_sort_flag(my_list[:])', globals=globals(), number=100))
# 1000 элементов
my_sorted_list = list(reversed([x for x in range(1000)]))

print('Пузырек сортированного списка = ',
      timeit('bubble_sort(my_sorted_list[:])', globals=globals(), number=100))
print('Пузырек с флагом для сортированного списка = ',
      timeit('bubble_sort_flag(my_sorted_list[:])', globals=globals(), number=100))

"""
Пузырек =  11.2184103
Пузырек с флагом =  10.9897246
Пузырек сортированного списка =  6.128959599999998
Пузырек с флагом для сортированного списка =  0.0124215999999997

Делаем вывод :доработка пузырька с помощью флага будет эфективен если список более-менее отсортирован
"""