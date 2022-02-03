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
    try:
        n = 2
        v = i**2
        sieve = [x for x in range(v)]
        sieve[1] = 0
        while n < v:
            if sieve[n] != 0:
                m = n * 2
                while m < v:
                    sieve[m] = 0
                    m += n
            n += 1
        return [p for p in sieve if p != 0][i - 1]
    except IndexError:
        return 2


idx = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(idx))
print(eratosfen(idx))

print(f"Наивный алгоритм 10: {timeit('simple(10)', globals=globals(), number=10)}")
print(f"Решето Эратосфена 10: {timeit('eratosfen(10)', globals=globals(), number=10)}\n")

print(f"Наивный алгоритм 100: {timeit('simple(100)', globals=globals(), number=10)}")
print(f"Решето Эратосфена 100: {timeit('eratosfen(100)', globals=globals(), number=10)}\n")

print(f"Наивный алгоритм 1000: {timeit('simple(1000)', globals=globals(), number=10)}")
print(f"Решето Эратосфена 1000: {timeit('eratosfen(1000)', globals=globals(), number=10)}")

print('\nВывод: я не смог найти Решето Эратосфена в интернете и в материалах, поэтому взял его у вас из примера. \n'
      'По подсчетам, "наивный" алгоритм срабатывает быстрее чем Решето Эратосфена. Плюс к этому, \n'
      'у вас в примере если ввести аргумент = 1, то в Решето будет ошибка, поэтому я добавил обработку исключений \n'
      'к функции (проверял и без нее, Решето быстрее не становится)')
