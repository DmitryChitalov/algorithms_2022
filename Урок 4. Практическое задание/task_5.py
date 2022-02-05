"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (в материалах есть его описание)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
"""
from timeit import timeit, default_timer


# def time_it(n):
#     def deco(func):
#         def wrapper(*args):
#             t_sum = 0
#             for el in range(n):
#                 start_time = default_timer()
#                 func(*args)
#                 delta = default_timer() - start_time
#                 t_sum += delta
#             return t_sum
#         return wrapper
#     return deco


# @time_it(100)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# @time_it(100)
def eratosthenes(i):
    # O(n log(log n))
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]


idx = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(idx))
print(eratosfen(idx))

print(f"Наивный алгоритм 10: {timeit('simple(10)', globals=globals(), number=100)}")
print(f"Решето Эратосфена 10: {timeit('eratosfen(10)', globals=globals(), number=100)}\n")
#
print(f"Наивный алгоритм 100: {timeit('simple(100)', globals=globals(), number=10)}")
print(f"Решето Эратосфена 100: {timeit('eratosfen(100)', globals=globals(), number=10)}\n")

print(f"Наивный алгоритм 1000: {timeit('simple(1000)', globals=globals(), number=10)}")
print(f"Решето Эратосфена 1000: {timeit('eratosfen(1000)', globals=globals(), number=10)}")

print('\nВывод: я не смог найти Решето в интернете и материалах, взял у вас из примера. Решето работает быстрее')
