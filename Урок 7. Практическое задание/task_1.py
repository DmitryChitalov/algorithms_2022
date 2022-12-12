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
import random
from timeit import timeit


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for idx in range(len(arr) - n):
            if arr[idx] < arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        n += 1
    return arr


def bubble_sort_optimized(arr):
    n = 1
    triger = False
    while triger is False and n < len(arr):
        no_changes = 0
        for idx in range(len(arr) - n):
            if arr[idx] < arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            else:
                no_changes += 1
            if no_changes == len(arr) - n:
                triger = True
                break

        n += 1

    return arr


def rand_array(lenght):
    return [random.randint(-100, 100) for i in range(lenght)]


if __name__ == '__main__':
    # check
    uns_array = rand_array(10)
    print(bubble_sort(uns_array[:]))
    # 10
    print('10')
    print(
        timeit(
            "bubble_sort(uns_array[:])",
            globals=globals(),
            number=1000))
    print(
        timeit(
            "bubble_sort_optimized(uns_array[:])",
            globals=globals(),
            number=1000))
    # 100
    uns_array = rand_array(100)
    print('100')
    print(
        timeit(
            "bubble_sort(uns_array[:])",
            globals=globals(),
            number=1000))
    print(
        timeit(
            "bubble_sort_optimized(uns_array[:])",
            globals=globals(),
            number=1000))

    # # 1000
    #
    # uns_array = rand_array(1000)
    # print('1000')
    #
    # print(
    #     timeit(
    #         "bubble_sort(uns_array[:])",
    #         globals=globals(),
    #         number=1000))
    # print(
    #     timeit(
    #         "bubble_sort_optimized(uns_array[:])",
    #         globals=globals(),
    #         number=1000))
    #
    # # 10000
    # uns_array = rand_array(10000)
    # print('10000')
    #
    # print(
    #     timeit(
    #         "bubble_sort(uns_array[:])",
    #         globals=globals(),
    #         number=1000))
    # print(
    #     timeit(
    #         "bubble_sort_optimized(uns_array[:])",
    #         globals=globals(),
    #         number=1000))

"""
Тесты выше 1000 занимают очень много времени 
10
0.018340500013437122
0.023298499989323318
100
0.8475460999761708
1.2257504999870434

оптимищация не помогла скорее всего алгоритм во многих случаях просто тратит время на счетчик.
оптимизация быстрее только если на вход у нас отсортированый или полу отсортированный
"""