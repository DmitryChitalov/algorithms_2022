"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit
from memory_profiler import memory_usage


# Разделение массива на две части
def partition(arr, low, high):
    pivot = arr[high]  # Опорный элемент
    i = low - 1
    for j in range(low, high):
        # Элементы меньше или равные опорному идут в левую часть
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Рекурсивный поиск медианы
def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randint(low, high)  # Выбираем случайный опорный элемент
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)


# Функция для нахождения медианы.
def find_median(arr):
    n = len(arr)
    k = n // 2  # Индекс медианы в отсортированном массиве.
    return quickselect(arr, 0, n - 1, k)


# Функция для замера времени выполнения и потребляемой памяти.
def measure_time(n):
    arr = [randint(1, 10000) for _ in range(n)]

    mem_before = memory_usage()[0]
    print(f"Время выполнения программы для массива длиной {n}:\n"
          f"  {timeit(lambda: find_median(arr.copy()), number=10000)} секунд\n"
          f"Использовано памяти: {memory_usage()[0] - mem_before} MiB\n"
          f"{'-' * 80}")
    median = find_median(arr)
    return median


# Замеры на массивах длиной 10, 100, 1000 элементов
n_values = [10, 100, 1000]
for n in n_values:
    measure_time(n)
"""
Время выполнения программы для массива длиной 10:
  0.12644690000161063 секунд
Использовано памяти: 0.02734375 MiB
--------------------------------------------------------------------------------
Время выполнения программы для массива длиной 100:
  0.4662105000024894 секунд
Использовано памяти: 0.015625 MiB
--------------------------------------------------------------------------------
Время выполнения программы для массива длиной 1000:
  4.276059800002258 секунд
Использовано памяти: 0.11328125 MiB
--------------------------------------------------------------------------------
"""