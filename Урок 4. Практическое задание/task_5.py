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
import math
from timeit import timeit
from functools import reduce


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


def sieve_of_eratosthenes(i):
    # оценка верхнего предела i-го простого числа
    n = math.ceil(i * math.log2(i) + i * math.log2(math.log2(i)) if i > 6 else i * 3)
    return sorted(reduce((lambda r, x: r - set(range(x ** 2, n, x)) if (x in r) else r), range(2, n),
                                         set(range(2, n))))[i - 1]


# i = int(input('Введите порядковый номер искомого простого числа: '))

print(f"simple(10) {timeit('simple(10)', globals=globals(), number=10)}")
print(f"simple(100) {timeit('simple(100)', globals=globals(), number=10)}")
print(f"simple(1000) {timeit('simple(1000)', globals=globals(), number=10)}")


print(f"sieve_of_eratosthenes(10) {timeit('sieve_of_eratosthenes(10)', globals=globals(), number=10)}")
print(f"sieve_of_eratosthenes(100) {timeit('sieve_of_eratosthenes(100)', globals=globals(), number=10)}")
print(f"sieve_of_eratosthenes(1000) {timeit('sieve_of_eratosthenes(1000)', globals=globals(), number=10)}")


"""
Вычеркивание делитей более эффективно, чем их перебор, однако, для малых значений перебору уступает.
"""