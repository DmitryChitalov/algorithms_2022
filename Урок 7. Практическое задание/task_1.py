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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_optimize(num):
    n = len(num)
    for i in range(n-1):
        s = 0
        for j in range(n-i-1):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
                s = 1
        if s == 0:
            break
    return num


print('----10----')
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(f'Standard {timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_sort(orig_list[:]))
print(f'Optimize {timeit("bubble_optimize(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_optimize(orig_list[:]))

print('----100----')
orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
print(f'Standard {timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_sort(orig_list[:]))
print(f'Optimize {timeit("bubble_optimize(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_optimize(orig_list[:]))

print('----1000----')
orig_list = [randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(f'Standard {timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_sort(orig_list[:]))
print(f'Optimize {timeit("bubble_optimize(orig_list[:])", globals=globals(), number=1000)}')
print(bubble_optimize(orig_list[:]))

"""
----10----
Standart 0.03020069999999997 
Optimize 0.031006900000000004

----100----
Standart 2.2669087
Optimize 2.1498822

----1000----
Standart 247.7347139
Optimize 245.68227369999997
"""

"""
Вывод: Оптимизированная функция выполняется быстрее но не намного
разница в 2 секунды на замерах в 1000, подводя итоги смысл доработки этой функции отсутствует
"""