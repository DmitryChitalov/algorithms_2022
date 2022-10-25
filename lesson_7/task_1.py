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


# функция из примера
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
0.01498949999222532 => функция из примера список(10)
0.0017633999814279377 => оптимизированная функция на список(10)
1.7447138000279665 => функция из примера на список(100)
0.03845079999882728 => оптимизированная функция на список(100)
152.8702021999634 => функция из примера на список(1000)
0.41038810001919046 => оптимизированная функция на список(1000)

Выводы:
Оптимизация функция улучшила результаты, время выполнения кода сократилось в разы. Похоже, что такая оптимизация имеет 
смысл во всех случаях, при этом чем больше список тем больше эффективности показывает оптимизированная функция. При
небольших списках результат будет меньше заметен и насколько он изначально близок к финальному отсортированному варианту.
'''