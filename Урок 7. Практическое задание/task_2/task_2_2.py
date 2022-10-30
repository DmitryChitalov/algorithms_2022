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
import random
from timeit import timeit


def generate_lst(n):
    lst = [random.randint(-100, 100) for i in range(2 * n + 1)]
    return lst


"""
Еще есть вариант через удаление максимального элемента, до того как длинна массива не станет равной m + 1,  и оттуда взять max"""
def mediana_without_sort(lst):
    n = len(lst) // 2
    while len(lst) > n + 1:
        lst.pop(lst.index(max(lst)))
    return max(lst)


# m = int(input())
# lst = generate_lst(m)
# print(lst)
# print(mediana_without_sort(lst))


lst_1 = generate_lst(10)
lst_2 = generate_lst(100)
lst_3 = generate_lst(1000)
print(timeit("mediana_without_sort(lst_1)", globals=globals(), number=1000))
print(timeit("mediana_without_sort(lst_2)", globals=globals(), number=1000))
print(timeit("mediana_without_sort(lst_3)", globals=globals(), number=1000))


"""
10 - 0.0002167999919038266
100 - 0.0004555000050459057
1000 - 0.023943099979078397
"""