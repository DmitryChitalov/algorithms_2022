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


def bubble_sort(obj):
    n = 1
    while n != len(obj):
        for i in range(len(obj)-n):
            if obj[i] < obj[i+1]:
                obj[i], obj[i+1] = obj[i+1], obj[i]
        n += 1
    return obj


def opt_bubble_sort(obj):
    n = 1
    is_sorted = False
    while n != len(obj) and not is_sorted:
        is_sorted = True
        for i in range(len(obj) - n):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
                is_sorted = False
        n += 1
    return obj


list_100 = [randint(-100, 100) for _ in range(100)]

print(timeit('bubble_sort(list_100[:])', globals=globals(), number=1000))
print(timeit('opt_bubble_sort(list_100[:])', globals=globals(), number=1000))
'''
1.2074991
1.0815759
'''

list_1000 = [randint(-100, 100) for _ in range(1000)]

print(timeit('bubble_sort(list_1000[:])', globals=globals(), number=1000))
print(timeit('opt_bubble_sort(list_1000[:])', globals=globals(), number=1000))
"""
102.5064725
103.9602727
"""
# Скорость примерно одинаковая
