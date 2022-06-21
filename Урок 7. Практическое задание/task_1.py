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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_adv(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = False
        if flag:
            break
        n += 1
    return lst_obj


print('Обычная сортировка пузырьком:')
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))

# # замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))


print('"Продвинутая" сортировка пузырьком:')
orig_list1 = [randint(-100, 100) for _ in range(10)]
print(orig_list1)
print(bubble_sort_adv(orig_list1[:]))

# # замеры 10
print(
    timeit(
        "bubble_sort_adv(orig_list1[:])",
        globals=globals(),
        number=1000))

orig_list1 = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort_adv(orig_list1[:])",
        globals=globals(),
        number=1000))

orig_list1 = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort_adv(orig_list1[:])",
        globals=globals(),
        number=1000))

"""
Обычная сортировка пузырьком:
0.009227900000000004
0.5690528
56.913456000000004

"Продвинутая" соритровка пузырьком:
0.0087326
0.5559461
55.874699299999996


Замеры показывают, что отсекая проходы без перемещений цифр в массиве,
мы получаем небольшой прирост производительности соритровки
"""
