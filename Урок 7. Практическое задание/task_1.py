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


rand_list_1 = [randint(-100, 100) for _ in range(10)]
rand_list_2 = [randint(-100, 100) for _ in range(100)]
rand_list_3 = [randint(-100, 100) for _ in range(1000)]


def default_bubble(list):
    n = 1
    while n < len(list):
        for i in range(len(list)-n):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
        n += 1
    return list


def check_bubble(list):
    n = 1
    check = True
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                check = False
        if check:
            break
        n += 1
    return list


print(rand_list_1, '\nСтандартная сортировка "пузырьком": ', timeit('default_bubble(rand_list_1[:])', globals=globals(), number=100), '\n', check_bubble(rand_list_1[:]), '\nСортировка "пузырьком" с проверкой: ', timeit('check_bubble(rand_list_1[:])', globals=globals(), number=100), '\n')
print(rand_list_2, '\nСтандартная сортировка "пузырьком": ', timeit('default_bubble(rand_list_2[:])', globals=globals(), number=100), '\n', check_bubble(rand_list_2[:]), '\nСортировка "пузырьком" с проверкой: ', timeit('check_bubble(rand_list_2[:])', globals=globals(), number=100), '\n')
print(rand_list_3, '\nСтандартная сортировка "пузырьком": ', timeit('default_bubble(rand_list_3[:])', globals=globals(), number=100), '\n', check_bubble(rand_list_3[:]), '\nСортировка "пузырьком" с проверкой: ', timeit('check_bubble(rand_list_3[:])', globals=globals(), number=100), '\n')


"""
Массив 10 элементов:
Стандартная сортировка "пузырьком":  0.0009985000069718808 
Сортировка "пузырьком" с проверкой:  0.0010604999988572672 

Массив 100 элементов:
Стандартная сортировка "пузырьком":  0.06856010000046808 
Сортировка "пузырьком" с проверкой:  0.06933450000360608 

Массив 1000 элементов:
Стандартная сортировка "пузырьком":  7.620501299999887 
Сортировка "пузырьком" с проверкой:  5.563932999997633 

При увеличении размера массива, сортировка 'пузырьком' с проверкой работает быстрее
В массивах небольших размеров доработка избыточна и не несет особой пользы

"""