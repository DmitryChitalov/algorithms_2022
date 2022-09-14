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
import math
from timeit import timeit
from random import randint


def create_list(num):
    return [randint(0, 100) for _ in range(2 * num + 1)]


def gnome(array):
    """
    Гномья сортировка
    :param array: массив
    :return: отсортированный массив
    """
    i = 1
    size_lst = len(array)
    while i < size_lst:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


def shell_sort(array):
    """
    Сортировка Шелла
    :param array: массив
    :return: отсортированный массив
    """
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):
    """
    Сортировка кучей
    :param array: массив
    :return: отсортированный массив
    """
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


if __name__ == '__main__':
    my_lst = [1, 2, 3, 4, 5]
    my_lst1 = [5, 2, 1, 4, 3]
    my_lst2 = [70, 49, 30, 10, 39, 36, 75, 80, 93, 32, 31, 47, 91, 54, 74, 24, 39, 12, 88, 76, 36]
    print(gnome(my_lst[:])[2])
    print(gnome(my_lst1[:])[2])
    print(gnome(my_lst2[:])[10])
    print(shell_sort(my_lst[:])[2])
    print(shell_sort(my_lst1[:])[2])
    print(shell_sort(my_lst2[:])[10])
    print(heap_sort(my_lst[:])[2])
    print(heap_sort(my_lst1[:])[2])
    print(heap_sort(my_lst2[:])[10])

    orig_list = create_list(10)

    # замеры 10
    print(timeit("gnome(orig_list[:])[10]", globals=globals(), number=1000))
    print(timeit("shell_sort(orig_list[:])[10]", globals=globals(), number=1000))
    print(timeit("heap_sort(orig_list[:])[10]", globals=globals(), number=1000))

    orig_list = create_list(100)

    # замеры 100
    print(timeit("gnome(orig_list[:])[100]", globals=globals(), number=1000))
    print(timeit("shell_sort(orig_list[:])[100]", globals=globals(), number=1000))
    print(timeit("heap_sort(orig_list[:])[100]", globals=globals(), number=1000))

    orig_list = create_list(1000)

    # замеры 1000
    print(timeit("gnome(orig_list[:])[1000]", globals=globals(), number=1000))
    print(timeit("shell_sort(orig_list[:])[1000]", globals=globals(), number=1000))
    print(timeit("heap_sort(orig_list[:])[1000]", globals=globals(), number=1000))

    """
    Результаты замеров:
    m=10 Сортировка Гноья: 0.04678620002232492
    m=10 Сортировка Шелла: 0.016286199912428856
    m=10 Сортировка Кучей: 0.043166999937966466
    m=100 Сортировка Гноья: 3.607114400016144
    m=100 Сортировка Шелла: 0.22857549996115267
    m=100 Сортировка Кучей: 0.5781914000399411
    m=1000 Сортировка Гноья: 423.3251139000058
    m=1000 Сортировка Шелла: 4.822601700201631
    m=1000 Сортировка Кучей: 9.578077499987558

    """
