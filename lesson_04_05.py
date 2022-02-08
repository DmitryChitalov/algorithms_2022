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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


# Попробуйте решить эту же задачу, применив алгоритм "Решето Эратосфена" (в материалах есть его описание)
def eratosthenes_sieve(idx):
    sieve = list(range(idx ** 2))
    sieve[1] = 0

    for item in sieve:
        if item > 1:
            for i in range(2 * item, len(sieve), item):
                sieve[i] = 0

    sieve = [item for item in sieve if item != 0]
    return sieve[idx]


"""
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
***
Замер времени функции simple с параметром 10: 0.013731400000000005
Замер времени функции eratosthenes_sieve с параметром 10: 0.0152927
Замер времени функции simple с параметром 100: 1.8340937
Замер времени функции eratosthenes_sieve с параметром 100: 1.7274661
Замер времени функции simple с параметром 1000: 342.2271276
Замер времени функции eratosthenes_sieve с параметром 1000: 294.3841159
***
Решето Эратосфена эффективнее с большими числами, если в параметр передается маленькое значение, ф-ция simple
отработает быстрее
"""

print(f'Замер времени функции simple с параметром 10: {timeit("simple(10)", "from __main__ import simple", number=1000)}')
print(f'Замер времени функции eratosthenes_sieve с параметром 10: {timeit("eratosthenes_sieve(10)", "from __main__ import eratosthenes_sieve", number=1000)}')
print(f'Замер времени функции simple с параметром 100: {timeit("simple(100)", "from __main__ import simple", number=1000)}')
print(f'Замер времени функции eratosthenes_sieve с параметром 100: {timeit("eratosthenes_sieve(100)", "from __main__ import eratosthenes_sieve", number=1000)}')
print(f'Замер времени функции simple с параметром 1000: {timeit("simple(1000)", "from __main__ import simple", number=1000)}')
print(f'Замер времени функции eratosthenes_sieve с параметром 1000: {timeit("eratosthenes_sieve(1000)", "from __main__ import eratosthenes_sieve", number=1000)}')
