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


# Исходный
def bubble_sort_1(list_in: list):
    len_list = len(list_in)
    for i in range(len_list):
        for j in range(len_list - i - 1):
            if list_in[j] < list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
    return list_in


# Улучшенный
def bubble_sort_2(list_in: list):
    is_sorted = False
    len_list = len(list_in)
    for i in range(len_list):
        if is_sorted:
            return list_in
        is_sorted = True
        for j in range(len_list - i - 1):
            if list_in[j] < list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j + 1], list_in[j]
                is_sorted = False
    return list_in


if __name__ == '__main__':
    notsorted = [randint(-100, 100) for _ in range(50)]
    print('Исходный:' ,notsorted)
    print('Исходный метод "пузырька"' ,bubble_sort_1(notsorted[:]))
    print('Улучшенный метод "пузырька"', bubble_sort_2(notsorted[:]))
    print('Врямя выполнения исходного:', timeit("bubble_sort_1(notsorted[:])",
                                                                     globals=globals(), number=1000))
    print('Врямя выполнения улучшенного:', timeit("bubble_sort_2(notsorted[:])",
                                                                     globals=globals(), number=1000))
"""
Врямя выполнения исходного: 0.8835018
Врямя выполнения улучшенного: 0.7055652
Доработка имеет положительный эффект. Эффективность улучшенного метода тем выше, чем упорядоченней исходный массив.
"""
