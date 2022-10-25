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
def bubble_sort(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1

def bubble_sort2(lst):
    for i in range(len(lst) - 1):
        check = True
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                check = False
        if check:
            break
    return lst
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
bubble_sort(array)
print('После сортировки:', array, sep='\n')
print(bubble_sort2(array))
print(timeit("bubble_sort(array[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(array[:])", globals=globals(), number=1000))
"""
Анализ
Доработка будет эффективной только если массив будет частично отсортирован
"""
