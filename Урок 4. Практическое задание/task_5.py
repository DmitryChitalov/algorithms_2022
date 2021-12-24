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


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
n1 = 10
n2 = 100
n3 = 1000
print(timeit("simple(10)", setup='from __main__ import simple, n1', number=1))
print(timeit("simple(100)", setup='from __main__ import simple, n2', number=1))
print(timeit("simple(1000)", setup='from __main__ import simple, n3', number=1))

n = int(input("Введите верхнюю границу диапазона: "))
sieve = set(range(2, n + 1))
while sieve:
    prime = min(sieve)
    print(prime, end="\t")
    sieve -= set(range(prime, n + 1, prime))
 # не сделал