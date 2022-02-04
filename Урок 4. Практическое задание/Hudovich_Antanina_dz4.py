"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit, repeat

test1 = '''
numbers = [i for i in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


func_1(numbers)
'''
test1_time = timeit(test1, number=1000)
test1_repeat = repeat(test1, repeat=3, number=1000)

test1_just_f = '''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
'''
test1f_time = timeit(test1_just_f, number=1000)
test1f_repeat = repeat(test1_just_f, repeat=3, number=1000)

test2 = '''
numbers = [i for i in range(100)]


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


func_2(numbers)
'''
test2_time = timeit(test2, number=1000)
test2_repeat = repeat(test2, repeat=3, number=1000)

test2_just_f = '''
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr
'''
test2f_time = timeit(test2_just_f, number=1000)
test2f_repeat = repeat(test2_just_f, repeat=3, number=1000)

print('code sample 1: ', test1_time, min(test1_repeat))
print('code sample 2: ', test2_time, min(test2_repeat))

print('function sample 1: ', test1f_time, min(test1f_repeat))
print('function sample 2: ', test2f_time, min(test2f_repeat))

# test 1   numbers = [i for i in range(100)]
# code sample 1:  0.012298700000000003 0.012237599999999994
# code sample 2:  0.010947499999999999 0.010580900000000004
# function sample 1:  5.960000000000687e-05 5.9000000000003494e-05
# function sample 2:  6.290000000000462e-05 6.249999999999312e-05


# test 2   numbers = [i for i in range(1000)]
# code sample 1:  0.14539259999999998 0.12979040000000003
# code sample 2:  0.1158399 0.1170293
# function sample 1:  6.099999999997774e-05 6.030000000001312e-05
# function sample 2:  6.330000000009939e-05 6.28000000000295e-05


# test 3   numbers = [i for i in range(10000)]
# code sample 1:  1.3199447 1.2532946999999999
# code sample 2:  1.1911102000000007 1.201898
# function sample 1:  6.560000000011001e-05 6.4000000000064e-05
# function sample 2:  5.840000000034706e-05 7.860000000015077e-05


# Выводы: насколько я поняла, все таки 2-й вариант кода будет более эффективным при росте длины исходного списка


"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
print(num_100)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

# Не оптимизированная функция recursive_reverse
# 0.03400040000000001
# 0.03931509999999999
# 0.0516345
# Оптимизированная функция recursive_reverse_mem
# 0.0021060999999999996
# 0.0022474000000000105
# 0.002275499999999986

# Создается видимость сильного улучшения работы, но только за счет того, что setup  выполняется только 1 раз,
# т.е.убирается весь смысл импорта рандома и переворачивается постоянно одно и то же число.


"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from random import randint
from timeit import timeit


def time_search(f):
    def wrapper(*args):
        f_time = timeit(f'{f(*args)}', number=100)
        return f_time
    return wrapper


@time_search
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


@time_search
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


@time_search
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_my(n, i=0, get_start=0):
    while n % 10 == 0 and get_start == 0:
        n = n // 10
        i += 1
    if n // 10 == 0:
        return str(n)

    element = str(n % 10)
    get_start = 1
    return element + revers_my(n // 10, i, get_start)


my_var = 'revers_my(number)'

number = randint(10000000000000000000000000, 100000000000000000000000000)
print(revers(number))
print(revers_2(number))
print(revers_3(number))
print(timeit(my_var, globals=globals(), number=100))

# for number=100 000 000 in timer
# 0.9760355000000018
# 1.0047879999999978
# 1.0958572999999987
# 9.4916457

# for number=10 000 000 in timer
# 0.1168629000000001
# 0.1817858000000001
# 0.09770939999999984
# 1.0633511999999996

# for number=1 000 000 in timer
# 0.009695800000000032
# 0.009830600000000023
# 0.00990669999999999
# 0.09733019999999998

# Очевидно только то, что рекурсия самая медленная, среди остальных 3 функций очень близкие результаты,
# но небольшое преимущество у 1 варианта.

"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1, 5, 4, 6, 5, 7, 8, 6, 4, 3, 7, 8, 6, 5, 4, 3, 4, 5, 4, 5, 6, 5, 4, 5, 6, 7, 5, 4, 6, 6, 6]


def time_search(f):
    def wrapper():
        f_time = timeit(f'{f()}', number=1000000000)
        return f_time
    return wrapper


@time_search
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return print(f'Чаще всего встречается число {num}, ', f'оно появилось в массиве {m} раз(а)')


@time_search
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return print(f'Чаще всего встречается число {elem}, ', f'оно появилось в массиве {max_2} раз(а)')


@time_search
def my_count():
    from collections import Counter
    new_array = Counter(array)
    most_common = new_array.most_common(1)
    return print(f'Чаще всего встречается число {most_common[0][0]}, ',
                 f'оно появилось в массиве {most_common[0][1]} раз(а)')


print(func_1())
print(func_2())
print(my_count())
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 10.2181532
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 9.923623500000001
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 10.281952

# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 10.8813126
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 11.639720899999999
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 10.6993783

# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 12.2156515
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 11.6145361
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 11.457812999999998

# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 12.1285048
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 10.537306
# Чаще всего встречается число 5,  оно появилось в массиве 9 раз(а)
# 12.128896899999997

# Каждый раз цифры разные, поэтому скорее всего никакого значимого улучшения по скорости не получалось.


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


def time_search(f):
    def wrapper(*args):
        f_time = timeit(f'{f(*args)}', globals=globals())
        return f_time
    return wrapper


@time_search
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


@time_search
def simple_erat(each_one):
    length = 3
    prime_nums = []
    while len(prime_nums) < each_one:
        length += 1
        fool_list = list(range(2, length))
        for number in fool_list:
            if number != 0:
                for candidate in range(2 * number, length, number):
                    fool_list[candidate - 2] = 0
        prime_nums = list(filter(lambda x: x != 0, fool_list))
    return prime_nums.pop()


print(simple_erat(i))

# Введите порядковый номер искомого простого числа: 10
# 0.0230649000000005
# 0.009682799999999325  - min time v2
# Введите порядковый номер искомого простого числа: 10
# 0.02190890000000012
# 0.02160609999999963
# Введите порядковый номер искомого простого числа: 10
# 0.01034859999999993   - min time v1
# 0.009790500000000257

# Введите порядковый номер искомого простого числа: 100
# 0.009783899999999512   - min time v1
# 0.00958300000000012    - min time v2
# Введите порядковый номер искомого простого числа: 100
# 0.00991300000000006
# 0.009709100000000248
# Введите порядковый номер искомого простого числа: 100
# 0.022640899999999853
# 0.00980860000000039

# Введите порядковый номер искомого простого числа: 1000
# 0.02319099999999974
# 0.009671200000001434   - min time v2
# Введите порядковый номер искомого простого числа: 1000
# 0.009489999999999554   - min time v1
# 0.009804900000000671
# Введите порядковый номер искомого простого числа: 1000
# 0.009776899999999422
# 0.02176589999999834

# Я не вижу информативности в этих замерах, не понимаю, как вычисление 10го числа может быть медленнее вычисления 100-го
# Вывод наверное должен был быть о том, что решето эффективнее для 10 и 100, а для более высоких значений наоборот,
# но пока он о том, что скорее всего с моим кодом что-то не так.

