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



def simple2(n):
    sieve = set(range(3, n+1, 2))
    primes = [2]
    while sieve:
        prime = min(sieve)
        primes.append(prime)
        sieve -= set(range(prime, n+1, prime))
    return primes


def eratosfen(i):
    # O(n log(log n))
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = i**2
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < i:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


# print(timeit("simple2(100)", number=100, globals=globals()))

print(timeit("simple(10)", number=100, globals=globals()))
print(timeit("eratosfen(10)", number=100, globals=globals()))
print(timeit("simple(100)", number=100, globals=globals()))
print(timeit("eratosfen(100)", number=100, globals=globals()))
print(timeit("simple(1000)", number=100, globals=globals()))
print(timeit("eratosfen(1000)", number=100, globals=globals()))

"""
вероятно не самая оптимальная реализация Эратосфена
реализация для поиска простых чисел меньших N получилась быстрее 
но выйгрыш во времени выполнения получается

0.0060143
0.004820099999999994
0.5367216
0.4372595
82.64826070000001
57.97176060000001

"""
