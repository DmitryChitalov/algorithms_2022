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

test_array = [randint(-100, 100) for _ in range(10)]
test_array_2 = [randint(-100, 100) for _ in range(100)]
test_array_3 = [randint(-100, 100) for _ in range(200)]


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        counter = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                counter += 1
        if counter == 0:
            break
        n += 1
    return lst_obj

print(timeit('bubble_sort(test_array[:])', globals=globals(), number=1000))   # 0.01675860001705587
print(timeit('bubble_sort_2(test_array[:])', globals=globals(), number=1000)) # 0.01134159998036921

print(timeit('bubble_sort(test_array_2[:])', globals=globals(), number=1000))   # 1.3032110000494868
print(timeit('bubble_sort_2(test_array_2[:])', globals=globals(), number=1000)) # 1.4729992998763919

print(timeit('bubble_sort(test_array_3[:])', globals=globals(), number=1000))    # 4.417984300060198
print(timeit('bubble_sort_2(test_array_3[:])', globals=globals(), number=1000))  # 4.974659499945119

# Вывод: дороботка будет эффективной для небольших массивов