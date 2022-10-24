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

# сортировка Гномья
def gnome_sort(arr):
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


# сортировка Шелла
def shell_sort(arr):
    count = len(arr) // 2
    while count:
        for i in range(count, len(arr)):
            j = i
            tmp = j - count
            while tmp >= 0 and arr[tmp] > arr[j]:
                arr[tmp], arr[j] = arr[j], arr[tmp]
                j = tmp
                tmp = j - count
        count //= 2
    return arr


# сортировка Кучей
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == '__main__':
    # замеры 10
    m = 5
    orig_list = [randint(-100, 100) for _ in range(2*m+1)]
    #print("Массив для сортировки из 10 элементов:  ", orig_list)
    #print(gnome_sort(orig_list))
    #print(shell_sort(orig_list))
    #print(heap_sort(orig_list))
    print(f'Медианой является число: {gnome_sort(orig_list[:])[m]}')
    print("сортировка Гномья при 10 элементах массива  :  ", timeit(
            "gnome_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {shell_sort(orig_list[:])[m]}')
    print("сортировка Шелла при 10 элементах массива   :  ", timeit(
            "shell_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {heap_sort(orig_list[:])[m]}')
    print("сортировка Кучей при 10 элементах массива   :  ", timeit(
        "heap_sort(orig_list[:])", globals=globals(), number=1000))

    # замеры 100
    print()
    m = 50
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(f'Медианой является число: {gnome_sort(orig_list[:])[m]}')
    print("сортировка Гномья при 100 элементах массива :  ", timeit(
            "gnome_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {shell_sort(orig_list[:])[m]}')
    print("сортировка Шелла при 100 элементах массива  :  ", timeit(
            "shell_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {heap_sort(orig_list[:])[m]}')
    print("сортировка Кучей при 100 элементах массива  :  ", timeit(
        "heap_sort(orig_list[:])", globals=globals(), number=1000))

    # замеры 1000
    print()
    m = 500
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(f'Медианой является число: {gnome_sort(orig_list[:])[m]}')
    print("сортировка Гномья при 1000 элементах массива : ", timeit(
            "gnome_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {shell_sort(orig_list[:])[m]}')
    print("сортировка Шелла при 1000 элементах массива :  ", timeit(
            "shell_sort(orig_list[:])", globals=globals(), number=1000))
    print(f'Медианой является число: {heap_sort(orig_list[:])[m]}')
    print("сортировка Кучей при 1000 элементах массива :  ", timeit(
        "heap_sort(orig_list[:])", globals=globals(), number=1000))


"""
Медианой является число: 6
сортировка Гномья при 10 элементах массива  :   0.008433999959379435
Медианой является число: 6
сортировка Шелла при 10 элементах массива   :   0.004162100027315319
Медианой является число: 6
сортировка Кучей при 10 элементах массива   :   0.011356699978932738

Медианой является число: 7
сортировка Гномья при 100 элементах массива :   0.6031220000004396
Медианой является число: 7
сортировка Шелла при 100 элементах массива  :   0.08941340004093945
Медианой является число: 7
сортировка Кучей при 100 элементах массива  :   0.19342380005400628

Медианой является число: 2
сортировка Гномья при 1000 элементах массива :  64.31102300004568
Медианой является число: 2
сортировка Шелла при 1000 элементах массива :   1.5168330000014976
Медианой является число: 2
сортировка Кучей при 1000 элементах массива :   2.919256199966185
"""
