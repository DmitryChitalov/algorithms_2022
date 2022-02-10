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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

print(simple(10))
print(simple(100))
print(simple(1000))

print(timeit('simple(10)', globals=globals(), number=100))
print(timeit('simple(100)', globals=globals(), number=100))
print(timeit('simple(1000)', globals=globals(), number=100))


# 29
# 541
# 7919
# 0.0009221000000252388
# 0.11499799999728566
# 19.600520800002414



def eratosfen(n):
    sieve = list(range(100000))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if x != 0]
    return sieve1[n-1]

print(eratosfen(10))
print(eratosfen(100))
print(eratosfen(1000))

print(timeit('eratosfen(10)', globals=globals(), number=100))
print(timeit('eratosfen(100)', globals=globals(), number=100))
print(timeit('eratosfen(1000)', globals=globals(), number=100))

# 29
# 541
# 7919
# 1.5617869999987306
# 1.5599207000050228
# 1.6847534000044107

# Чем больше порядковый номер простого числа, тем эффективнее «Решето Эратосфена»