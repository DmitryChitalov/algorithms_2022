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
from memory_profiler import profile


lst = [randint(-100, 100) for _ in range(1, 100)]


@profile
def pop_method(lst: list):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


@profile
def new_pop(lst):
    has_wrapped = True
    total = 0
    while has_wrapped:
        has_wrapped = False
        for i in range(len(lst) - total - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            has_wrapped = True
        total += 1
        return lst


print(lst)
print(timeit('pop_method(lst)', globals=globals(), number=1))
print(timeit('new_pop(lst)', globals=globals(), number=1))
print(pop_method(lst))
print(new_pop(lst))
''' Новый метод совершает сортировку быстрее обычного пузырька так как с каждой итерацией
массив уменьшается '''