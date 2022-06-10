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


def simple(j):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= j:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == j:
                break
            count += 1
        n += 1
    return n


# l = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(l))


def eratosfen(n, j):  # я не совсем правильно сделал, заполнил исходя из
    # простых чисел меньше n = 1000
    if n < 4:  # 123 - простые
        return
    array = [i for i in range(n + 1)]
    # те числа, что не простые - задам нулем
    array[1] = 0  # зануляем единичку
    index = 2
    while index < n:
        if array[index] != 0:
            k = 2 * index
            while k < n:
                array[k] = 0  # заменить на 0, т е вычеркиваем
                k = k + index
        index += 1
    simple_arr = []
    for el in array:
        if el != 0:
            simple_arr.append(el)
    return simple_arr[j-1]


# print(eratosfen(1000, 10))
# print(timeit('simple(50)', number=10000, globals=globals()))  # 5.108128859
# print(timeit('eratosfen(1000, 50)', number=10000, globals=globals()))  # 3.5427145520000005
# На 2 секунды лучше!
# print(timeit('simple(10)', number=10000, globals=globals()))  # 0.26861295500000004
# print(timeit('eratosfen(1000, 10)', number=10000, globals=globals()))  # 3.572375371
# на данных меньше 50 выигрыавет первый алгоритм, т к во втором куча заполнения по сути
# лишнего, зато есть список всех простых чисел до 1000. Начиная от 45 второй алгоритм
# начичнает выигрывать
# print(timeit('simple(45)', number=10000, globals=globals()))  # 4.052764866
# print(timeit('eratosfen(1000, 45)', number=10000, globals=globals()))  # 3.3745733639999997
# print(timeit('simple(100)', number=10000, globals=globals()))  # 25.160996277
print(timeit('eratosfen(1000, 100)', number=10000, globals=globals()))  # 3.7556393210000003
# Причем флуктуация времени работы второго алгоритма достаточная низкая, хотя это связано
# с константностью макс знач 1000
# Сложность 1 - O(N^2)
# сложность 2 - не знаю, посмотрю в семинаре
