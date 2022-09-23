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
from random import randrange
from timeit import timeit


def reverse_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def reverse_bubble_new(lst):
    n = 1
    length = len(lst)
    while n < length:
        f = 0
        for i in range(length - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                f = 1
        if f == 0:
            break
        n += 1
    return lst


data = [randrange(-100, 100) for _ in range(1000)]
code1 = "reverse_bubble(data[:])"
code2 = "reverse_bubble_new(data[:])"
print("Неоптимизированная сортировка")
print(timeit(code1, globals=globals(), number=10))
print("Оптимизированная сортировка")
print(timeit(code2, globals=globals(), number=10))

"""
Доработала. Умнее не стал - даже дольше работает. Видимо, время, которое уходит на проверку,
сравнимо с выигрышем нескольких проходок
"""
