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
from timeit import timeit


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


def eratosthenes(n):
    if n == 1:
        return 1
    else:
        sieve = list(range(n ** 2))
        sieve[1] = 0
        for i in sieve:
            if i > 1:
                for j in range(2 * i, len(sieve), i):
                    sieve[j] = 0
        sieve = list(set(sieve))
        del sieve[0]
        return sieve[n - 1]


print(timeit("simple(10)", setup="from __main__ import simple", number=1000))    # 0.0154305
print(timeit("simple(100)", setup="from __main__ import simple", number=1000))   # 1.6851123
print(timeit("simple(1000)", setup="from __main__ import simple", number=1000))  # 263.5214949


print(timeit("eratosthenes(10)", setup="from __main__ import eratosthenes", number=1000))    # 0.0214467
print(timeit("eratosthenes(100)", setup="from __main__ import eratosthenes", number=1000))   # 1.768089
print(timeit("eratosthenes(1000)", setup="from __main__ import eratosthenes", number=1000))  # 226.8141871


# Не понял где искать описание алгоритма "Решето Эратосфена" (в материалах преподавателя не нашел).
# Нашел алгоритм в интернете.

# Решето Эратосфена работает эффективнее на больших порядкомых номерах.
# При малых значениях порядкового номера наивный алгоритм работает несколько быстрее
