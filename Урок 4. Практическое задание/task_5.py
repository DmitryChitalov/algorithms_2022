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


#i = int(input('Введите порядковый номер искомого простого числа: '))
#print(simple(i))

def simple_2(n):
    a = [i for i in range(n+1)]
    a[1] = 0
    i = 2
    while i <= n ** 0.5:
        if a[i] != 0:
            j = i ** 2
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a


for func in (simple_2, simple):
    for num in (10, 100, 1000):
       print(f'{func.__name__} on number {num}. Result: {timeit("func(num)", globals=globals(), number=100)} s')

