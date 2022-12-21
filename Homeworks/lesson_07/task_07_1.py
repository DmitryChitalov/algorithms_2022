"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ, помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from timeit import timeit
from random import randint


def bubble_sort_reverse(lst):
    n = 0
    while n < len(lst)-1:
        for i in range(len(lst)-1-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def bubble_sort_reverse_check(lst):
    flag = True
    n = 0
    while n < len(lst)-1:
        for i in range(len(lst)-1-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = False
        if flag:
            break
        n += 1
    return lst


if __name__ == '__main__':

    print('Массив заранее не отсортирован')
    lst_test = [randint(-100, 99) for i in range(15)]
    print(lst_test)
    print(bubble_sort_reverse(lst_test[:]))
    print(bubble_sort_reverse_check(lst_test[:]))
    print(timeit("bubble_sort_reverse(lst_test[:])", globals=globals(), number=1000))
    print(timeit("bubble_sort_reverse_check(lst_test[:])", globals=globals(), number=1000))

    print('\nМассив заранее отсортирован')
    lst_ordered_test = [i for i in range(10000, 0, -1)]
    print(timeit("bubble_sort_reverse(lst_ordered_test[:])", globals=globals(), number=1))
    print(timeit("bubble_sort_reverse_check(lst_ordered_test[:])", globals=globals(), number=1))

# Доработка будет эффективной в том случае, если в функцию передаётся уже отсортированный массив.
# Тогда не будет совершаться лишних проходов по массиву.
