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
import timeit

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


def resh_erat(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break
# def resh_erat(n):
#     d = [x for x in range(2, n+1) if x not in
#          [i for sub in [list(range(2 * j, n+1, j)) for j in range(2,
#              n // 2)] for i in sub]]
#     return d


s = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(s))
print(resh_erat(s))

print(timeit.timeit("simple(s)", globals=globals(), number=100))
print(timeit.timeit("resh_erat(s)", globals=globals(), number=100))

'''

В результате измерения было определено, что алгоритм решета Эратосфена 
эффективен для чисел от 5 до 1000
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))

Введите порядковый номер искомого простого числа: 5
11
11
0.0003485000000003069
0.0002038000000004203

Введите порядковый номер искомого простого числа: 200
1223
1223
0.7825467000000002
0.12069550000000007

Введите порядковый номер искомого простого числа: 1000
7919
7919
28.0542836
1.750439

'''
