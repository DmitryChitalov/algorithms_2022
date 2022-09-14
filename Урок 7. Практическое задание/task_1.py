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


# стандартная функция
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]

        n += 1

    return lst_obj


# оптимизированная функция
def bubble_sort_1(list_to_sort):
    ready = True  # делаем булеву переменную, пока True - мы в цикле
    n = 1
    while ready:
        ready = False
        for i in range(len(list_to_sort) - n):
            if list_to_sort[i] < list_to_sort[i + 1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                ready = True
                n += 1
    return list_to_sort


orig_list = [randint(-100, 100) for _ in range(10)]
print(bubble_sort(orig_list))
print(bubble_sort_1(orig_list))

# orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))
orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

'''
мои результаты:
0.006484999961685389 => стандартная функция на список(10)
0.001997400016989559 => оптимизированная функция на список(10)

0.4668027999578044 => стандартная функция на список(100)
0.01508270000340417 => оптимизированная функция на список(100)

52.45543390000239 => стандартная функция на список(1000)
0.1942577000008896 => оптимизированная функция на список(1000)

Выводы:
Оптимизация дала результаты, время выполнения кода сократилось в разы. Похоже, что такая оптимизация имеет смысл во 
всех случаях, при этом чем больше список тем больше эффективности показывает оптимизированная функция. Подозреваю, что
на небольших списках результат будет меньше заметен, плюс возможно многое будет зависеть от самого списка, насколько он
изначально близок к финальному отсортированному варианту.
'''
