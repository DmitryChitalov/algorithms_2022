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


def create_list(num):
    return [randint(0, 100) for _ in range(2 * num + 1)]


def find_medians(lst):
    median_idx = len(lst) // 2
    for i in range(median_idx):
        lst.remove(max(lst))
    my_median = max(lst)
    return my_median


if __name__ == '__main__':
    my_lst = [1, 2, 3, 4, 5]
    my_lst1 = [5, 2, 1, 4, 3]
    my_lst2 = [70, 49, 30, 10, 39, 36, 75, 80, 93, 32, 31, 47, 91, 54, 74, 24, 39, 12, 88, 76, 36]
    print(find_medians(my_lst[:]))
    print(find_medians(my_lst1[:]))
    print(find_medians(my_lst2[:]))

    orig_list = create_list(10)
    print(orig_list)
    print(find_medians(orig_list[:]))

    # замеры 10
    print(timeit("find_medians(orig_list[:])", globals=globals(), number=1000))

    orig_list = create_list(100)

    # замеры 100
    print(timeit("find_medians(orig_list[:])", globals=globals(), number=1000))

    orig_list = create_list(1000)

    # замеры 1000
    print(timeit("find_medians(orig_list[:])", globals=globals(), number=1000))

    """
    Результаты замеров:
    
    m=10 : 0.010440699988976121
    m=100 : 0.39781470014713705
    m=1000 : 26.365068699931726
    
    """
