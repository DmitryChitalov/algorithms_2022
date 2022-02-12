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


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            array[j], array[j + 1] = array[j + 1], array[j]
    return array


def optimized_bubble(array):
    n = len(array)
    is_sorted = True
    for i in range(n):
        for j in range(n - i - 1):
            is_sorted = True
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break
    return array


if __name__ == "__main__":
    my_list = [randint(-1000, 1000) for i in range(10)]
    print(timeit("bubble_sort(my_list[:])", number=1000, globals=globals()))
    print(timeit("optimized_bubble(my_list[:])", number=1000, globals=globals()))

    my_list = [randint(-1000, 1000) for i in range(100)]
    print(timeit("bubble_sort(my_list[:])", number=1000, globals=globals()))
    print(timeit("optimized_bubble(my_list[:])", number=1000, globals=globals()))

    my_list = [randint(-1000, 1000) for i in range(1000)]
    print(timeit("bubble_sort(my_list[:])", number=1000, globals=globals()))
    print(timeit("optimized_bubble(my_list[:])", number=1000, globals=globals()))

"""
0.03875980000000001
0.033959500000000004
1.4342278
0.8415855000000001
193.30284129999998
167.85086629999998

0.029741099999999993
0.02981220000000001
1.9181064
1.7198732999999997
187.06778640000002
80.78145699999996


0.02284590000000003
0.026988000000000012
1.546474
1.4816313
199.648535
129.8136095

Выйгрыш в производительности оптимизированного алгоритма зависит от исходных данных.
В самом худшем случае, когда массив отсортирован в обратном порядке выйгрыша от оптимизации не будет.
"""