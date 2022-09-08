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


def del_max_items(li):
    """Возврат медианы массива путём удаления максимальных элементов"""
    temp_li = li
    for i in range(len(li) // 2):
        temp_li.remove(max(temp_li))
    return max(temp_li)


# -----------------------------------------------------------------------------
m = 10
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# print(origin_list)
result = del_max_items(origin_list)
print(f"Медиана списка из 11 элементов: {result}")
# Измерение среднего время выполнения куска кода.
result_time = timeit(stmt="del_max_items(origin_list[:])",
                    number=100,
                    globals=globals())
print(f"{'%.8f' % result_time} seconds")

# -----------------------------------------------------------------------------
m = 100
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# Измерение среднего время выполнения куска кода.
result_time = timeit(stmt="del_max_items(origin_list[:])",
                     number=100,
                     globals=globals())
print(f"{'%.8f' % result_time} seconds")

# -----------------------------------------------------------------------------
m = 1000
origin_list = [randint(-100, 100) for _ in range(2 * m + 1)]
# Измерение среднего время выполнения куска кода.
result_time = timeit(stmt="del_max_items(origin_list[:])",
                     number=100,
                     globals=globals())
print(f"{'%.8f' % result_time} seconds")

"""
Медиана списка из 11 элементов: -36
0.00117190 seconds
0.04160020 seconds
3.62440460 seconds
"""
