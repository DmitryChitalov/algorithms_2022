"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


def heapsort(lst):
    for start in range(int((len(lst) - 2) / 2), -1, -1):
        siftdown(lst, start, len(lst) - 1)

    for end in range(len(lst) - 1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst


def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def find_m_1_gnome(size, n=1000):
    """
    Считаю, чтто неинтересно и не совсем наглядно замерять один и тот же массив 1000 раз, по этому в данной функции
    на каждое новое измерение будет генерироваться новый массив, а возвращать функция будет список из медиан, найденных
    для каждого измерения
    Используем гномью сортировку
    :param size: Размер списка
    :param n: Длинна элементов массива, в котором ведеться поиск (учитывая формулу из задания 2m + 1 и то, что
    на сортировку отправляем массивы 10, 100, 1000 элементов, увиличиваем этот параметр на 1 в функции)
    :return: список найденных медиан.
    """
    median_list = []
    for i in range(n):
        temp_list = [randint(-100, 100) for _ in range(size + 1)]
        m = gnome(temp_list[:])[int(size / 2)]
        median_list.append(m)
    return median_list


def find_m_1_heap(size, n=1000):
    """
    Считаю, чтто неинтересно и не совсем наглядно замерять один и тот же массив 1000 раз, по этому в данной функции
    на каждое новое измерение будет генерироваться новый массив, а возвращать функция будет список из медиан, найденных
    для каждого измерения
    Используем сортировку кучей
    :param size: Размер списка
    :param n: Длинна элементов массива, в котором ведеться поиск (учитывая формулу из задания 2m + 1 и то, что
    на сортировку отправляем массивы 10, 100, 1000 элементов, увиличиваем этот параметр на 1 в функции)
    :return: список найденных медиан.
    """
    median_list = []
    for i in range(n):
        temp_list = [randint(-100, 100) for _ in range(size + 1)]
        m = heapsort(temp_list[:])[int(size / 2)]
        median_list.append(m)
    return median_list


def find_m_1_shell(size, n=1000):
    """
    Считаю, чтто неинтересно и не совсем наглядно замерять один и тот же массив 1000 раз, по этому в данной функции
    на каждое новое измерение будет генерироваться новый массив, а возвращать функция будет список из медиан, найденных
    для каждого измерения
    Используем сортировку кучей
    :param size: Размер списка
    :param n: Длинна элементов массива, в котором ведеться поиск (учитывая формулу из задания 2m + 1 и то, что
    на сортировку отправляем массивы 10, 100, 1000 элементов, увиличиваем этот параметр на 1 в функции)
    :return: список найденных медиан.
    """
    median_list = []
    for i in range(n):
        temp_list = [randint(-100, 100) for _ in range(size + 1)]
        m = shell(temp_list[:])[int(size / 2)]
        median_list.append(m)
    return median_list


print('Замеры для "гномьей" сортировки:')
print("Замер 10 элементов:")
print(timeit("find_m_1_gnome(10)", globals=globals(), number=1))
print("Замер 100 элементов:")
print(timeit("find_m_1_gnome(100)", globals=globals(), number=1))
print("Замер 1000 элементов:")
print(timeit("find_m_1_gnome(1000)", globals=globals(), number=1))

print('Замеры для сортировки "кучей":')
print("Замер 10 элементов:")
print(timeit("find_m_1_heap(10)", globals=globals(), number=1))
print("Замер 100 элементов:")
print(timeit("find_m_1_heap(100)", globals=globals(), number=1))
print("Замер 1000 элементов:")
print(timeit("find_m_1_heap(1000)", globals=globals(), number=1))

print('Замеры для сортировки Шелла:')
print("Замер 10 элементов:")
print(timeit("find_m_1_shell(10)", globals=globals(), number=1))
print("Замер 100 элементов:")
print(timeit("find_m_1_shell(100)", globals=globals(), number=1))
print("Замер 1000 элементов:")
print(timeit("find_m_1_shell(1000)", globals=globals(), number=1))
"""
Мои  результаты измерений:
Замеры для "гномьей" сортировки:
Замер 10 элементов:
0.01418050000211224
Замер 100 элементов:
0.6515776000160258
Замер 1000 элементов:
174.6005966999801
Замеры для сортировки "кучей":
Замер 10 элементов:
0.016390600008890033
Замер 100 элементов:
0.3824523000221234
Замер 1000 элементов:
8.52833170001395
Замеры для сортировки Шелла:
Замер 10 элементов:
0.0328944000066258
Замер 100 элементов:
0.43981690000509843
Замер 1000 элементов:
6.296321200003149
В общем, для "гнома" видим данные характерные для сложности O(n^2), так что как не изворачивайся, от сложности не 
уйти...
Сортировка "кучей" и Шелла - шикарные результаты, сложность для "кучи" - n log n, для Шелла - в лучшем случае О(n)!!

"""
