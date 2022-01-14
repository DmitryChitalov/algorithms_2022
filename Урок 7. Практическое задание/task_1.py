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


def rev_bubble_sort(lst):
    n = len(lst) - 1
    while n > 0:
        for i in reversed(range(len(lst) - n, len(lst))):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
        n -= 1
    return lst


def optimized_rev_bubble_sort(lst):
    n = len(lst) - 1
    while n > 0:
        count = 0
        for i in reversed(range(len(lst) - n, len(lst))):
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                count += 1
        n -= 1
        if not count:
            break
    return lst


new_list = [randint(-100, 100) for i in range(500)]
ordered_list = [i for i in range(500)]
almost_ordered_list = [i for i in range(500)]
almost_ordered_list[50] = 101

print(timeit("rev_bubble_sort(new_list[:])", globals=globals(), number=1000))                       # 9.26 сек
print(timeit("optimized_rev_bubble_sort(new_list[:])", globals=globals(), number=1000))             # 9.73 сек
print(timeit("rev_bubble_sort(ordered_list[:])", globals=globals(), number=1000))                   # 5.19 сек
print(timeit("optimized_rev_bubble_sort(ordered_list[:])", globals=globals(), number=1000))         # 0.02 сек
print(timeit("rev_bubble_sort(almost_ordered_list[:])", globals=globals(), number=1000))            # 5.19 сек
print(timeit("optimized_rev_bubble_sort(almost_ordered_list[:])", globals=globals(), number=1000))  # 0.90 сек

# Оптимизация не помогает, а наоборот увеличивает время работы (из-за лишних операций) на произвольных
# несортированных списках. Однако при получении отсортированного списка, не производятся ненужные вычисления, и
# поэтому время заметно сокращается. На почти полностью отсортированных списках время также существенно меньше у
# оптимизированного варианта.
