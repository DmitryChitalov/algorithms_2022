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

def eratosthenes(n, a):
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать
    for i in sieve:
        if i > 1:
            for j in range(2*i, len(sieve), i):
                sieve[j] = 0
    sieve = set(sieve)
    sieve = list(sieve)
    return sieve[a]

print(eratosthenes(100, 10))

print(f'Вариант simple(10): {timeit("simple(10)", number=1000, globals=globals())}')
print(f'Вариант simple(100): {timeit("simple(100)", number=1000, globals=globals())}')
print(f'Вариант simple(200): {timeit("simple(200)", number=1000, globals=globals())}')
print(f'Вариант eratosthenes(10): {timeit("eratosthenes(100, 10)", number=1000, globals=globals())}')
print(f'Вариант eratosthenes(100): {timeit("eratosthenes(1000, 100)", number=1000, globals=globals())}')
print(f'Вариант eratosthenes(200): {timeit("eratosthenes(10000, 200)", number=1000, globals=globals())}')

# Вариант simple(10): 0.0660396999999997
# Вариант simple(100): 7.6420865
# Вариант simple(200): 35.724709
# Вариант eratosthenes(10): 0.059014699999998754
# Вариант eratosthenes(100): 0.5845838999999984
# Вариант eratosthenes(200): 7.008857599999999

'''
Вывод: решето эратосфена эфективно при больших массивах,
при маленьком массиве эффективнее первый метод
'''