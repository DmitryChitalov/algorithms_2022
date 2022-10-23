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

def bubble_reverse(obj):
    for j in range(len(obj) - 1):
        for i in range(len(obj) - 1 - j):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
    return obj

object = [randint(-100, 100) for _ in range(10)]

print('Исходный массив:', object)
print('Обратная пузырьковая:', bubble_reverse(object[:]))
print(timeit('bubble_reverse(object[:])', globals=globals, number=1000))
