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

def bubble_sort(list_obj):
    n = 1
    while n < len(list_obj):
        for i in range(len(list_obj) - 1):
            if list_obj[i] < list_obj[i - 1]:
                list_obj[i], list_obj[i - 1] = list_obj[i - 1], list_obj[i]
        n += 1
    return list_obj

def bubble_sort_2(list_obj):
    count = 0
    flag = True
    for i in range(len(list_obj) - 1):
        if flag is False:
            return count, list_obj
        flag = False
        for j in range(len(list_obj) - 1 - i):
            if list_obj[j + 1] > list_obj[j]:
                list_obj[j], list_obj[j + 1] = list_obj[j + 1], list_obj[j]
                flag = True
            count += 1
    return count, list_obj

list_1 = [randint(-100, 100) for x in range(10)]

print('Пузырек 10 элементов = ',
      timeit('bubble_sort(list_1[:])', globals=globals(), number=1000))
print('Пузырек_2 10 элементов = ',
      timeit('bubble_sort_2(list_1[:])', globals=globals(), number=1000))
# Пузырек 10 элементов =  0.042360099999999984
# Пузырек_2 10 элементов =  0.032833500000000015

list_1 = [randint(-100, 100) for x in range(100)]
print('Пузырек 100 элементов = ',
      timeit('bubble_sort(list_1[:])', globals=globals(), number=1000))
print('Пузырек_2 100 элементов = ',
      timeit('bubble_sort_2(list_1[:])', globals=globals(), number=1000))

# Пузырек 100 элементов =  3.5059751
# Пузырек_2 100 элементов =  3.1685647000000006

list_1 = [randint(-100, 100) for x in range(500)]
print('Пузырек 500 элементов = ',
      timeit('bubble_sort(list_1[:])', globals=globals(), number=1000))
print('Пузырек_2 500 элементов = ',
      timeit('bubble_sort_2(list_1[:])', globals=globals(), number=1000))
# Пузырек 500 элементов = 111.17879389999999
# Пузырек_2 500 элементов = 91.0835901
# Доработка пузырькового метода не оказалась эффективной

















