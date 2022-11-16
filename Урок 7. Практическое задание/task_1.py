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


def sort_bubble_0(array_in):
    n = 1
    while n < len(array_in):
        for i in range(len(array_in) - n):
            if array_in[i] < array_in[i + 1]:
                array_in[i], array_in[i + 1] = array_in[i + 1], array_in[i]
        n += 1
    return array_in


# замеры 10
array = [randint(-100, 100) for i in range(10)]

print(array)
print(sort_bubble_0(array[:]))

print(timeit("sort_bubble_0(array[:])", globals=globals(), number=1000))

# замеры 100
array = [randint(-100, 100) for i in range(100)]
print(timeit("sort_bubble_0(array[:])", globals=globals(), number=1000))

# замеры 1000
array = [randint(-100, 100) for i in range(1000)]
print(timeit("sort_bubble_0(array[:])", globals=globals(), number=1000))


def sort_bubble_1(array_in):
    n = 1
    counter = 0
    while n < len(array_in):
        for i in range(len(array_in) - n):
            if array_in[i] < array_in[i + 1]:
                array_in[i], array_in[i + 1] = array_in[i + 1], array_in[i]
                counter += 1
        if counter == 0:
            break
        n += 1
    return array_in


# замеры 10
array = [randint(-100, 100) for i in range(10)]
print(timeit("sort_bubble_1(array[:])", globals=globals(), number=1000))

# замеры 100
array = [randint(-100, 100) for i in range(100)]
print(timeit("sort_bubble_1(array[:])", globals=globals(), number=1000))

# замеры 1000
array = [randint(-100, 100) for i in range(1000)]
print(timeit("sort_bubble_1(array[:])", globals=globals(), number=1000))


'''
Исходный - [81, 71, -22, -97, -32, 18, 5, 73, -53, -42]
Сортированный - [81, 73, 71, 18, 5, -22, -32, -42, -53, -97]
10 - 0.015857299999879615
100 - 1.108800599999995
1000 - 96.22113150000041

Модификация будет работать быстрее, если туда отдавать уже отсортированный список.
Если список не сортирован, тогда времени будет затрачено +- одинаково.

10 - 0.010567700000137847
100 - 0.9059455999995407
1000 - 104.59370459999991
'''