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
from copy import deepcopy


def bubble_sort(lst_obj):
    """
Сортирует по убыванию методом "пузырька" одномерный целочисленный массив
    :param lst_obj: array
    :return: sorted array
    """
    for i in range(len(lst_obj) - 1):
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    return lst_obj


def bubble_sort_adv(lst_obj):
    """
Сортирует по убыванию методом "пузырька" одномерный целочисленный массив.
    :param lst_obj: array
    :return: sorted array
    """
    for i in range(len(lst_obj) - 1):
        count = 0
        for j in range(len(lst_obj) - i - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
                count += 1
        if count == 0:
            break
    return lst_obj


test_list = [randint(-100, 100) for _ in range(10)]
test_list_adv = deepcopy(test_list)


print(test_list)
print(bubble_sort(test_list))
print(
    timeit(
        "bubble_sort(test_list[:])",
        globals=globals(),
        number=1000))
print('------------------Обновлённая функция:')
print(test_list_adv)
print(bubble_sort_adv(test_list_adv))
print(
    timeit(
        "bubble_sort_adv(test_list[:])",
        globals=globals(),
        number=1000))

"""
Замеры времени обеих реализаций показали эффективность доработки 
работы функции как на малых, так и на больших массивах. Чем больше
сортируемый массив, тем выигрыш во времени больше:
--- на массиве из 10 элементов:
0.020008542000000018
0.005990272000000019
--- на массиве из 100 элементов:
1.0108404949999998
0.01933687500000003
--- на массиве из 1000 элементов:
73.43539755900001
0.20718251200000282
"""
