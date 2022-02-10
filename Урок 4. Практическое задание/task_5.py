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


def eratosfen(i):
    n = 0
    if i <= 100:
        n = 550
    elif i <= 200:
        n = 1250
    elif i <= 500:
        n = 3600
    elif i > 500:
        n = 10000
    sieve = sorted(
            set(range(2, n + 1)).difference(set((p * f) for p in range(2, int(n ** 0.5) + 2)
                                                for f in range(2, int(n / p) + 1))))
    return sieve[i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(f'Перебор делителей: {simple(i)} {timeit("simple(i)", globals=globals(), number=10)}')
print(f'Решето Эратосфена: {eratosfen(i)} {timeit("eratosfen(i)", globals=globals(), number=10)}')


"""
При малом значении порядкового номера функция simple(1) показывает лучший результат, но с порядкового номера 30 
решето Эратосфена показывает отличный результат, причём с увеличением порядкового номера
отрыв по времени значительно увеличивается.
"""
