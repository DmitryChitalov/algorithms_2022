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


def mediana(data):
    middle = len(data) // 2 + 1
    for item in data:
        d = n = 0
        for i in data:
            if i <= item:
                n += 1
            if i == item:
                d += 1
        if n - d < middle <= n:
            return item


if __name__ == "__main__":

    orig_list_11 = [randint(-100, 100) for _ in range(11)]

    print(
        timeit(
            "mediana(orig_list_11[:])",
            globals=globals(),
            number=1000))

    print(
        timeit(
            "mediana([randint(-100, 100) for _ in range(101)])",
            globals=globals(),
            number=1000))

    print(
        timeit(
            "mediana([randint(-100, 100) for _ in range(1001)])",
            globals=globals(),
            number=1000))

    """
    На массиве из 1001 элемента время составило 12.53 секунды. Но
    Есть такой момент, время замера сильно зависит от места, где
    окажется медиана. Если ближе к началу массива, то результат
    может быть получен и за единицы секунд, если же ближе к концу, то
    десятки. Но в среднем укладывается в ~20 секунд
    """