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
    primes = []
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            primes.append(n)
            if count == i:
                break
            count += 1
        n += 1
    # return n
    return primes


def simple2(n):
    sieve = set(range(3, n+1, 2))
    primes = [2]
    while sieve:
        prime = min(sieve)
        primes.append(prime)
        sieve -= set(range(prime, n+1, prime))
    return primes


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(simple2(i+446))
print(timeit("simple(100)", number=100, globals=globals()))
print(timeit("simple2(499)", number=100, globals=globals()))

"""
реализовать решето Эратосфена для i-го простого числа не получилось 
"""
