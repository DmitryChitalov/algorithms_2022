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
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort2(arr):
    for i in range(len(arr) - 1):
        check = True
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                check = False
        if check:
            break
    return arr


a = [randint(-100,100)for i in range(1000)]
print(f'{a}\n{bubble_sort(a[:])}')

print(timeit("bubble_sort(a[:])", globals=globals(), number=1000))  #38.117916041999706
print(timeit("bubble_sort2(a[:])", globals=globals(), number=1000)) #38.38662808400113

"""
Доработка будет эффективной только если массив будет частично отсортирован
"""

