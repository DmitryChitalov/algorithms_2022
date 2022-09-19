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

from random import randrange
import timeit

def timer(n):
    def deco(func,*args):
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
def median(lst1):
    lst=lst1[:]
    n=(len(lst) - 1) // 2
    for i in range(n):
        lst.remove(max(lst))
    return max(lst)

print("11 чисел", end=' ')
median([randrange(-100,100) for _ in range(11)])
print("101 число", end=' ')
median([randrange(-100,100) for _ in range(101)])
print("1001 число", end=' ')
median([randrange(-100,100) for _ in range(1001)])
