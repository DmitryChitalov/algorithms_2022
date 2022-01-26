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


def eratosphen(n):
    elems = 8000
    nums = [x for x in range(elems + 1)]
    nums[1] = 0
    i = 2
    while i <= elems ** 0.5:
        if nums[i] != 0:
            j = i ** 2
            while j <= elems:
                nums[j] = 0
                j += i
        i += 1
    nums = [x for x in nums if x != 0]
    return nums[n - 1]


print('simple(10) = ', timeit('simple(10)', globals=globals(), number=1000))
print('simple(100) = ', timeit('simple(100)', globals=globals(), number=1000))
print('simple(1000) = ', timeit('simple(1000)', globals=globals(), number=50))

print('eratosphen(10) = ', timeit('eratosphen(10)', globals=globals(), number=1000))
print('eratosphen(100) = ', timeit('eratosphen(100)', globals=globals(), number=1000))
print('eratosphen(1000) = ', timeit('eratosphen(1000)', globals=globals(), number=1000))


"""
Результаты проверок:
                    simple(10) =  0.06085269999999998
                    simple(100) =  6.2314483
                    simple(1000) =  52.518800199999994
                    eratosphen(10) =  4.773119499999993
                    eratosphen(100) =  4.6039770999999945
                    eratosphen(1000) =  4.485030199999997

Вывод:
        На дальней дистанции мой алгоритм выигрывает.
        Если порядковый номер меньше 100, то лучше использовать
        функцию simple(n).
        PS: думаю можно уменьшить скорость работы моего алгоритма
        путем замены lc на что-то пошустрее, но не дошел до реализации.
"""