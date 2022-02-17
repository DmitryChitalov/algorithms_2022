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


# для выполнения задания воспользуюсь сортировкой Шелла и различными алгоритмами вычисления следующего размера шага,
# дающиими разную общую вычислительную сложность алгоритма сортировки Шелла
# Хиббард O(N**(3/2))
# Седжевик O(N**(4/3))
# Кнут O(N**(3/2))
# Дональд Шелл O(N**2)
# На базе этой сортировки сделаю вычисление медианы и замеры.


def hibbard_gen(len_, num=1):
    while 2 ** num - 1 < len_:
        num += 1
    while num > 0:
        num -= 1
        yield 2 ** num - 1


def sedgewick_gen(len_, num=0):
    number = 9 * (2 ** num - 2 ** (num // 2)) + 1
    while number < len_:
        num += 1
        if num % 2 == 0:
            number = 9 * (2 ** num - 2 ** (num // 2)) + 1
        else:
            number = 8 * 2 ** num - 6 * 2 ** (num + 1) // 2 + 1
    while num > 0:
        num -= 1
        if num % 2 == 0:
            step = 9 * (2 ** num - 2 ** (num // 2)) + 1
        else:
            step = 8 * 2 ** num - 6 * 2 ** (num + 1) // 2 + 1
        yield step
    yield 0


def knuth_gen(len_, num=1):
    while (3 ** num - 1) // 2 < len_ // 3:  # первый шаг
        num += 1
    while num >= 0:
        yield (3 ** num - 1) // 2
        num -= 1


def shell_gen(len_, num=0):
    num = len_
    while num > 0:
        num = num // 2
        yield num


def shell_sort(lst, f_gen):
    n = len(lst)
    gen = f_gen(n)
    step = next(gen)
    while step > 0:
        for i in range(step, n):
            j = i
            while j >= step and lst[j] < lst[j - step]:
                lst[j], lst[j - step] = lst[j - step], lst[j]
                j = j - step
        step = next(gen)
    return lst


# Наконец, решение задачи
def median_shell(lst, f):  # средний, если len(list_) нечет, или среднее от двух средних значений
    q, r = divmod(len(lst), 2)
    lst = shell_sort(lst, f)
    return sorted(lst)[q] if r else sum(sorted(lst)[q - 1:q + 1]) / 2


def median_sorted(lst):  # средний, если len(list_) нечет, или среднее от двух средних значений
    q, r = divmod(len(lst), 2)
    return sorted(lst)[q] if r else sum(sorted(lst)[q - 1:q + 1]) / 2


# проверка результатов сортировки с разными генераторами шагов
# x = [5, 0, -2, 7, 3, 0, -2, 7, 3, 5, 7, 8, 9, 0, 70, 3, 90, 33, -5, -9, 77, 99]
# print(shell_sort(x, shell_gen))
# print(shell_sort(x, knuth_gen))
# print(shell_sort(x, sedgewick_gen))
# print(shell_sort(x, hibbard_gen))
# print(median_shell(x, shell_gen))
# print(median_sorted(x))

# замеры на массивах длиной 10, 100, 1000 элементов
print('замеры на массиве длиной 11 элементов')
x0 = [randint(-100, 100) for _ in range(11)]
print(timeit("median_shell(x0[:], shell_gen)", globals=globals(), number=300))  # 0.0013926000000000008
print(timeit("median_shell(x0[:], knuth_gen)", globals=globals(), number=300))  # 0.0017613000000000004
print(timeit("median_shell(x0[:], sedgewick_gen)", globals=globals(), number=300))  # 0.0019924000000000053
print(timeit("median_shell(x0[:], hibbard_gen)", globals=globals(), number=300))  # 0.0019475000000000048
print(timeit("median_sorted(x0[:])", globals=globals(), number=100))  # 0.00004339999999999899
print('замеры на массиве длиной 101 элемент')
x1 = [randint(-100, 100) for _ in range(101)]
print(timeit("median_shell(x1[:], shell_gen)", globals=globals(), number=300))  # 0.025568599999999997
print(timeit("median_shell(x1[:], knuth_gen)", globals=globals(), number=300))  # 0.026271100000000006
print(timeit("median_shell(x1[:], sedgewick_gen)", globals=globals(), number=300))  # 0.027370900000000004
print(timeit("median_shell(x1[:], hibbard_gen)", globals=globals(), number=300))  # 0.026667200000000002
print(timeit("median_sorted(x1[:])", globals=globals(), number=300))  # 0.0008591000000000015
print('замеры на массиве длиной 1001 элемент')
x2 = [randint(-100, 100) for _ in range(1001)]
print(timeit("median_shell(x2[:], shell_gen)", globals=globals(), number=300))  # 0.5390604
print(timeit("median_shell(x2[:], knuth_gen)", globals=globals(), number=300))  # 0.547249
print(timeit("median_shell(x2[:], sedgewick_gen)", globals=globals(), number=300))  # 0.5218182
print(timeit("median_shell(x2[:], hibbard_gen)", globals=globals(), number=300))  # 0.5133222
print(timeit("median_sorted(x2[:])", globals=globals(), number=300))  # 0.02006500000000022


# лучшая вычислительную сложность для шага Седжвика, проверим на больших массивах
print()
x3 = [randint(-100, 100) for _ in range(10001)]
print(timeit("shell_sort(x3[:], shell_gen)", globals=globals(), number=30))  # 0.8920439
print(timeit("shell_sort(x3[:], knuth_gen)", globals=globals(), number=30))  # 0.7967882000000004
print(timeit("shell_sort(x3[:], sedgewick_gen)", globals=globals(), number=30))  # 0.7249669000000001
print(timeit("shell_sort(x3[:], hibbard_gen)", globals=globals(), number=30))  # 0.7441097999999995
# да, так оно и есть, шага Седжвика дает лучший результат
