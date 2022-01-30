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
from math import sqrt

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


def eratosfen(num):
    n = num * 10

    a = [2, 3]

    for i in range(4, n):                          # 10 * seq_num
        k = int(sqrt(i))
        for j in range(2, k + 1):                  # sqrt(10 * seq_num)
            if i % j == 0:
                break
            elif j == k:
                a.append(i)
    return a[num - 1]



# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(eratosfen(i))


print(timeit("simple(10)", globals=globals(), number=1000))              # 0.016007800000000003
print(timeit("eratosfen(10)", globals=globals(), number=1000))           # 0.086578
# при небольшом порядковом номере простого числа наивный перебор работает быстрее

print(timeit("simple(100)", globals=globals(), number=1000))            # 2.3815280999999997
print(timeit("eratosfen(100)", globals=globals(), number=1000))         # 0.8231405

print(timeit("simple(1000)", globals=globals(), number=100))           # 25.1762107
print(timeit("eratosfen(1000)", globals=globals(), number=100))        # 1.0716357999999993
# по мере увеличения порядкового номера простого числа время наивного перебора значительно вырастает
# по сравнению с алгоритмом "Решето Эратосфена"

