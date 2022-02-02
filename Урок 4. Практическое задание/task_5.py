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


import cProfile


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


def simple_2(i):
    """С использованием «Решета Эратосфена»"""
    num = 2
    edge = i**2
    sieve = [el for el in range(edge)]
    sieve[1] = 0
    while num < edge:
        if sieve[num] != 0:
            m = num * 2
            while m < edge:
                sieve[m] = 0
                m += num
        num += 1
    return [el for el in sieve if el != 0][i-1]


if __name__ == '__main__':
    i = int(input('Введите порядковый номер искомого простого числа: '))


    def main():
        print(simple(i))
        print(simple_2(i))

    cProfile.run('main()')

#  import модуля перенес вверх кода (в предыдущем варианте ДЗ был после инструкции if __name__ == '__main__)
#  результаты с реализацией функций с разбора (i = 1000):
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.236    0.236    0.236    0.236     task_5.py:20(simple)
#     1    0.283    0.283    0.339    0.339     task_5.py:40(simple_2)



