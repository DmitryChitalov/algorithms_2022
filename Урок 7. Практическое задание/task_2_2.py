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


def search_median(arr):
    for i in range(len(arr) // 2):
        arr.remove(max(arr))
    return max(arr)


if __name__ == '__main__':
    # замеры 10
    m = 5
    orig_list = [randint(-100, 100) for _ in range(2*m+1)]
    print("Массив для обработки из 10 элементов:  ", orig_list)
    print(f'Отсортированный, для проверки, массив {sorted(orig_list)}')
    print(f'Медианой является число: {search_median(orig_list)}')
    print("Поиск медианы при 10 элементах массива   :  ", timeit(
            "search_median(orig_list[:])", globals=globals(), number=1000))

    # замеры 100
    print()
    m = 50
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(f'Медианой является число: {search_median(orig_list[:])}')
    print("Поиск медианы при 100 элементах массива  :  ", timeit(
            "search_median(orig_list[:])", globals=globals(), number=1000))

    # замеры 1000
    print()
    m = 500
    orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
    print(f'Медианой является число: {search_median(orig_list[:])}')
    print("Поиск медианы при 1000 элементах массива : ", timeit(
            "search_median(orig_list[:])", globals=globals(), number=1000))

"""
Массив для обработки из 10 элементов:   [92, -86, 87, 48, 97, 78, 51, -43, -89, -27, 2]
Отсортированный, для проверки, массив [-89, -86, -43, -27, 2, 48, 51, 78, 87, 92, 97]
Медианой является число: 48
Поиск медианы при 10 элементах массива   :   0.0009016001131385565

Медианой является число: 13
Поиск медианы при 100 элементах массива  :   0.057716900017112494

Медианой является число: 0
Поиск медианы при 1000 элементах массива :  5.415351500036195
"""
