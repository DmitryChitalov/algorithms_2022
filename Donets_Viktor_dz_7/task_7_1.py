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


def bubble_sort_1(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
    return lst_obj


# при 10 значениях
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_1(orig_list))
print('Не доработанный(10) -',
      timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print('Доработанный(10) -',
      timeit(
          "bubble_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))

# при 100
orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_1(orig_list))
print('Не доработанный(100) -',
      timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print('Доработанный(100) -',
      timeit(
          "bubble_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))

# при 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
print(bubble_sort_1(orig_list))
print('Не доработанный(1000) -',
      timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print('Доработанный(1000) -',
      timeit(
          "bubble_sort_1(orig_list[:])",
          globals=globals(),
          number=1000))


"""
[42, 20, 66, -17, 94, -2, -50, 18, -84, 38]
[94, 66, 42, 38, 20, 18, -2, -17, -50, -84]
[94, 66, 42, 38, 20, 18, -2, -17, -50, -84]
Не доработанный(10) - 0.00705649999963498
Доработанный(10) - 0.001070300000719726
[49, -6, 13, 53, -53, -7, 23, 43, 79, -69,.... 61, 95, -29, -37, 34, 66]
[96, 95, 89, 86, 83, 83, 83, 82, 80, 79, ... -75, -79, -82, -86, -88, -93, -97]
[96, 95, 89, 86, 83, 83, 83, 82, 80, 79, ... -75, -79, -82, -86, -88, -93, -97]
Не доработанный(100) - 0.335189000000355
Доработанный(100) - 0.006821300000410702
[-67, 33, 90, -47, 1, 38, 18, -7, 24, 66, ... 92, 37, 14, -21, 94, 28, 94]
[100, 100, 100, 100, 100, 99, 99, 98, 98, ... -99, -100, -100, -100, -100]
[100, 100, 100, 100, 100, 99, 99, 98, 98, ... -99, -100, -100, -100, -100]
Не доработанный(1000) - 34.930012999999235
Доработанный(1000) - 0.07703920000039943

Из выше полученного можно сделать вывод при доработке время выполнения 
функции уменьшилось в разы 
"""