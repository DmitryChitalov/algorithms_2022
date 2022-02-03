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


def s_o_e(soe):
    sieve = list(range(soe ** 2))
    sieve[1] = 0

    for item in sieve:
        if item > 1:
            for j in range(2 * item, len(sieve), item):
                sieve[j] = 0

    sieve = [item for item in sieve if item != 0]
    return sieve[soe]


print(
    f'Замер simple с 10: {timeit("simple(10)", "from __main__ import simple", number=10)}')
print(
    f'Замер s_o_e с 10: {timeit("s_o_e(10)", "from __main__ import s_o_e", number=10)}')
print(
    f'Замер simple с 100: {timeit("simple(100)", "from __main__ import simple", number=10)}')
print(
    f'Замер s_o_e с 100: {timeit("s_o_e(100)", "from __main__ import s_o_e", number=10)}')
print(
    f'Замер simple с 1000: {timeit("simple(1000)", "from __main__ import simple", number=10)}')
print(
    f'Замер s_o_e с 1000: {timeit("s_o_e(1000)", "from __main__ import s_o_e", number=10)}')

"""
Решето Эратосфена отрабатывает быстрее

3 замера:
Замер simple с 10: 9.510000000000074e-05
Замер s_o_e с 10: 0.00010929999999999968
Замер simple с 100: 0.0214793
Замер s_o_e с 100: 0.019236499999999997
Замер simple с 1000: 1.9831478
Замер s_o_e с 1000: 1.9300232

Замер simple с 10: 9.539999999999549e-05
Замер s_o_e с 10: 0.00010949999999999849
Замер simple с 100: 0.012129800000000003
Замер s_o_e с 100: 0.013342899999999998
Замер simple с 1000: 1.9636866999999998
Замер s_o_e с 1000: 1.8599640000000002

Замер simple с 10: 9.510000000000074e-05
Замер s_o_e с 10: 0.00011129999999999474
Замер simple с 100: 0.0146113
Замер s_o_e с 100: 0.014696
Замер simple с 1000: 1.9523849999999998
Замер s_o_e с 1000: 1.9136748
"""