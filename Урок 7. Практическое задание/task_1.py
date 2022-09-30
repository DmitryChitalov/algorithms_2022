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


# Берем функцию bubble_sort и для того, чтобы она сортировала от большего значения к меньшему меняем знак > на <.
def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1

    return lst_obj


# Делаем доработку алгоритма.
def bubble_sort_reverse_smart(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                count += 1
        if count == 0:
            break
        n += 1

    return lst_obj


# Проверяем правильность сортировки.
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_reverse(orig_list))

# замеры 10
print(timeit("bubble_sort_reverse(orig_list[:])", globals=globals(), number=1000))

# Делаем замеры работы функции с дорабокой.
print(timeit("bubble_sort_reverse_smart(orig_list[:])", globals=globals(), number=1000))

# замеры 100
orig_list_2 = [randint(-100, 100) for _ in range(100)]

print(timeit("bubble_sort_reverse(orig_list_2[:])", globals=globals(), number=1000))

# Делаем замеры работы функции с дорабокой.
print(timeit("bubble_sort_reverse_smart(orig_list_2[:])", globals=globals(), number=1000))

# замеры 1000

orig_list_3 = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort_reverse(orig_list_3[:])", globals=globals(), number=1000))

# Делаем замеры работы функции с дорабокой.
print(timeit("bubble_sort_reverse_smart(orig_list_3[:])", globals=globals(), number=1000))

"""
Результаты измерений:
Если в массив входят 10 элементов:
Без доработки: 0.008150000001478475
С доработкой: 0.0016276000023935921

Если в массив входят 100 элементов:
Без доработки: 1.1949542000002111
С доработкой: 1.1280787000068813

Если в массив входят 1000 элементов:
Без доработки: 108.04481909999595
С доработкой: 118.52697780000017

По результатам измерений видно, что доработка имеет смысл только в небольших массивах. Чем больше в массиве
элементов, тем меньше вероятность его сортировки.
"""
