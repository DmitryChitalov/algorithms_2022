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
from random import randrange
import timeit


def timer(n):
    def deco(func, *args):
        def wrapper(*args):
            result = 0
            for _ in range(n):
                start = timeit.default_timer()
                ret = func(*args)
                result += timeit.default_timer() - start
            print(f"Время выполнения {result:.5f}")
            return ret

        return wrapper

    return deco


@timer(100)
def shell_sort(lst):
    length = len(lst)
    ciura = (0, 1, 4, 10, 23, 57, 132, 301, 701, 1750)
    dif_index = -1
    while ciura[dif_index] > length // 2:
        dif_index -= 1
    step = ciura[dif_index]
    while step > 0:
        for i in range(step):
            now = i
            counter = 1
            while now + step < length:
                while lst[now + step] < lst[now] and now >= 0:
                    lst[now + step], lst[now] = lst[now], lst[now + step]
                    now -= step
                    counter += 1
                now += counter * step
                counter = 1
        dif_index -= 1
        step = ciura[dif_index]
    return lst[(length - 1) // 2]


@timer(100)
def gnom_sort(lst):
    now = 1
    seed = 2
    length = len(lst)
    while now < length - 2:
        if lst[now] > lst[now + 1]:
            lst[now], lst[now + 1] = lst[now + 1], lst[now]
            now -= 1 if now > 0 else 0
        else:
            now = seed
            seed += 1
    return lst[(length - 1) // 2]


print("Гномья сортировка")
print("11 чисел", end=' ')
gnom_sort([randrange(-100, 100) for _ in range(11)])
print("101 число", end=' ')
gnom_sort([randrange(-100, 100) for _ in range(101)])
print("1001 число", end=' ')
gnom_sort([randrange(-100, 100) for _ in range(100001)])

print("Сортировка Шелла (вроде)")
print("11 чисел", end=' ')
shell_sort([randrange(-100, 100) for _ in range(11)])
print("101 число", end=' ')
shell_sort([randrange(-100, 100) for _ in range(101)])
print("1001 число", end=' ')
shell_sort([randrange(-100, 100) for _ in range(100001)])
