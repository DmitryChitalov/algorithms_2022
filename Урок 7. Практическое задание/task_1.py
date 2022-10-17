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

# Сортировка пузырьковая


def bubble_sort(numbers_list):
    x = 1
    count = 0
    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
        count += 1
        x += 1
    return f'{numbers_list} - отсортированный список № 1, количество циклов - {count} '


# Сортировка пузырьковая мод !!!

def bubble_sort_v_2(numbers_list):
    x = 1
    count = 0
    flag = False

    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                flag = True
        x += 1
        count += 1
        if not flag:
            break
    return f'{numbers_list} - отсортированный список № 2, количество циклов - {count} '


def bubble_sort_v_3(numbers_list):
    x = 1
    count = 0
    flag = False
    num = max(numbers_list)
    numbers_list.remove(num)
    numbers_list.insert(0, num)
    num = min(numbers_list)
    numbers_list.remove(num)
    numbers_list.append(num)
    del num

    while x < len(numbers_list):
        for i in range(len(numbers_list) - x):
            if numbers_list[i] < numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
                flag = True
        x += 1
        count += 1
        if not flag:
            break
    return f'{numbers_list} - отсортированный список № 3, количество циклов - {count} '


# Функция № 1
# Список 10
numbers_list = [randint(-100, 100) for i in range(10)]
print(f'{numbers_list} - исходный список')
time_func = timeit("bubble_sort(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func} - время выполнения функции № 1, Список 10')
# Список 100
numbers_list = [randint(-100, 100) for i in range(100)]
time_func = timeit("bubble_sort(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func} - время выполнения функции № 1, Список 100')
# Список 1000
numbers_list = [randint(-100, 100) for i in range(1000)]
time_func = timeit("bubble_sort(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func} - время выполнения функции № 1, Список 1000')


# Функция № 2
# Список 10
numbers_list = [randint(-100, 100) for i in range(10)]
print(f'{numbers_list} - исходный список')
time_func_2 = timeit("bubble_sort_v_2(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_2} - время выполнения функции № 2, Список 10')
# Список 100
numbers_list = [randint(-100, 100) for i in range(100)]
time_func_2 = timeit("bubble_sort_v_2(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_2} - время выполнения функции № 2, Список 100')
# Список 1000
numbers_list = [randint(-100, 100) for i in range(1000)]
time_func_2 = timeit("bubble_sort_v_2(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_2} - время выполнения функции № 2, Список 1000')


# Функция № 3
# Список 10
numbers_list = [randint(-100, 100) for i in range(10)]
print(f'{numbers_list} - исходный список')
time_func_3 = timeit("bubble_sort_v_3(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_3} - время выполнения функции № 3,  Список 10')
# Список 100
numbers_list = [randint(-100, 100) for i in range(100)]
time_func_3 = timeit("bubble_sort_v_3(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_3} - время выполнения функции № 3,  Список 100')
# Список 1000
numbers_list = [randint(-100, 100) for i in range(1000)]
time_func_3 = timeit("bubble_sort_v_3(numbers_list[:])", globals=globals(), number=1000)
print(f'{time_func_3} - время выполнения функции № 3,  Список 1000')

# Аналитика
# Как видим в первом варианте мы заходим в цикл столько раз сколько есть в нем элементов,
# Во втором варианте добавил флаг, он позволяет нам остановиться как только условие не выполниться,
# что сокращает кол-во цыклов
# В третьем варианте хотел проверить, измениться ли время,
# если я очевидно поставлю самый большой и самый маленький элемент на их позиции, как видим это увеличило время
# [66, -60, -25, 52, 23, 37, -60, -93, 77, -77] - исходный список
# 0.014531600289046764 - время выполнения функции № 1, Список 10
# 1.1794150993227959 - время выполнения функции № 1, Список 100
# 113.77043860033154 - время выполнения функции № 1, Список 1000
# [92, -84, 83, -10, 98, -90, -44, -60, 25, 29] - исходный список
# 0.01543780043721199 - время выполнения функции № 2, Список 10
# 1.1148466002196074 - время выполнения функции № 2, Список 100
# 120.07088469993323 - время выполнения функции № 2, Список 1000
# [-3, -48, 34, 92, 37, -22, 80, 20, -4, -59] - исходный список
# 0.016482099890708923 - время выполнения функции № 3,  Список 10
# 1.3139631999656558 - время выполнения функции № 3,  Список 100
# 120.70242819935083 - время выполнения функции № 3,  Список 1000

