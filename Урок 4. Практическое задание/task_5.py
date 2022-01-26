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
from math import log


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


def eratosthens_sieve(a):
    max_num = a
    need_num = max_num / log(max_num)
    while need_num < a:
        max_num += 1
        need_num = max_num / log(max_num)
    max_num = int(max_num)

    sieve = list(range(2, max_num + 1))
    for p in sieve:
        if p != 0:
            if p ** 2 > max_num:
                sieve = set(sieve)
                sieve = (list(sieve))
                sieve.sort()
                try:
                    return sieve[a]
                except IndexError:
                    # print(f'простое число с индексом {a} не входит в введенную последовательносмть чисел до {num}')
                    return None

            for j in range(sieve.index(p ** 2), len(sieve), p):
                sieve[j] = 0


print(" Поиск 5-ого числа ")
print("simple algorithm ", timeit("simple(5)", number=200, globals=globals()), "seconds")
print("eratosthens_sieve", timeit("eratosthens_sieve(5)", number=200, globals=globals()), "seconds")

print(" Поиск 10-ого числа ")
print("simple algorithm ", timeit("simple(10)", number=200, globals=globals()), "seconds")
print("eratosthens_sieve", timeit("eratosthens_sieve(10)", number=200, globals=globals()), "seconds")

print(" Поиск 100-ого числа ")
print("simple algorithm ", timeit("simple(100)", number=200, globals=globals()), "seconds")
print("eratosthens_sieve", timeit("eratosthens_sieve(100)", number=200, globals=globals()), "seconds")

print(" Поиск 1000-ого числа ")
print("simple algorithm ", timeit("simple(1000)", number=200, globals=globals()), "seconds")
print("eratosthens_sieve", timeit("eratosthens_sieve(1000)", number=200, globals=globals()), "seconds")



# Простой алгоритм работает примерно с той же скоростью , что и Алгоритм Эратосфена , когда порядковый номер искомого
# числа небольшой , Но уже после 7ми он работает медленнее, и далее ощутимо медленнее чем Эратосфена
#
# Поиск 5-ого числа
# simple algorithm  0.0018776999999999995 seconds
# eratosthens_sieve 0.0017362999999999962 seconds
#  Поиск 10-ого числа
# simple algorithm  0.007012300000000006 seconds
# eratosthens_sieve 0.0034655000000000033 seconds
#  Поиск 100-ого числа
# simple algorithm  0.7708813 seconds
# eratosthens_sieve 0.060604699999999956 seconds
#  Поиск 1000-ого числа
# simple algorithm  125.1447734 seconds
# eratosthens_sieve 1.0524969000000084 seconds

