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


# создадим одинаковые условия для профилирования: для этого минимально переделал исходную функцию:
# создаем список всех простых чисел не превышающих натуральное число n. Как в алгоритме «Решета Эратосфена».
# во втором цикле делаем перебор только по простым делителям
def simple_0(n):  # Без использования «Решета Эратосфена»
    ls = []
    for next_num in range(2, n + 1):
        for i in ls:  # перебор только по уже найденным простым (искл. 4,6,8,9...)
            if next_num % i == 0:
                break
        else:
            ls.append(next_num)
    return ls


# Из огромного количества примеров реализации алгоритма 'Решето Эратосфена' выберем те,
# что предложены в https://ru.wikibooks.org/wiki/Реализации_алгоритмов/Решето_Эратосфена
# Из предложенных вариантов заменил 1, 2, 4. Они оказались медленнее простешего алгоритма.

def simple_1(n):  # Вариант 1 Faster & more memory-wise pure Python code
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def simple_2(n):  # Вариант 2  starting with half sieve
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def simple_3(n):  # Вариант 3
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    return list(filter(lambda x: x != 0, numbers))


def simple_4(n):  # Вариант 4
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def simple_5(n):  # Вариант 5
    sieve = list(range(n + 1))
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [x for x in sieve if x != 0]


def simple_6(n):  # Написал таки свой на основе предыдущих. simple_1 использует какой-то улучшенный алг-м
    sieve = [True] * n
    for i in range(2, n):
        if sieve[i]:  # пропускаем дырки в решете (от деления на 2, 3 ...)
            sieve[i + i:: i] = [False] * ((n - i - 1) // i)  # делаем новые ( делитель только простое число)
    return [x for x, b in zip(range(2, n), sieve[2:]) if b]  # формула длины среза из (n-2*i)//i -> ((n-2*i)+i-1)//i


# Проверяем два алгоритма без использования «Решета Эратосфена» на simple(1000) = 7919
# print(timeit("simple(1000)", setup='from __main__ import simple', number=10))  # 2.464с
# print(timeit("simple_0(7919)", setup='from __main__ import simple_0', number=10))  # 0.179с
# думаю существенный выигрыш дало ограничение перебора делителей, списком прстых чисел,
# полученными на предыдущей итерации внешнего цикла.

max_num = 7920
print('запуск функций и вывод последних 5 результатов')
[print(f"simple_{i}: {eval(f'simple_{i}(max_num)[-6:-1]')}") for i in range(0, 7)]
# профилировка каждого алгоритма через timeit
print('До 100')
max_num = 100
times = [timeit(f"simple_{n}(max_num)", f"from __main__ import simple_{n}, max_num", number=100) for n in range(0, 7)]
t_otn = sorted([(t / min(times), f"simple_{i}") for i, t in enumerate(times)])
print('Результаты в величинах относительно функции с минимальным временем выполнением')
[print(f'{p}:{t:8.3f}') for t, p in t_otn]
print('До 1000')
number = 1000
times = [timeit(f"simple_{n}(max_num)", f"from __main__ import simple_{n}, max_num", number=100) for n in range(0, 7)]
t_otn = sorted([(t / min(times), f"simple_{i}") for i, t in enumerate(times)])
print('Результаты в величинах относительно функции с минимальным временем выполнением')
[print(f'{p}:{t:8.3f}') for t, p in t_otn]
print('До 10 000')
max_num = 10000
times = [timeit(f"simple_{n}(max_num)", f"from __main__ import simple_{n}, max_num", number=100) for n in range(0, 7)]
t_otn = sorted([(t / min(times), f"simple_{i}") for i, t in enumerate(times)])
print('Результаты в величинах относительно функции с минимальным временем выполнением')
[print(f'{p}:{t:8.3f}') for t, p in t_otn]

'''
Получили следующие результаты:
Результаты в величинах относительно функции с минимальным временем выполнением
Повторов вычислений 100. Массив простых чисел ограничевается числами 100, 1000, 10000
     До 100                 До 1000                До 10000
simple_1:   1.000      simple_1:   1.000      simple_1:   1.000
simple_2:   1.071      simple_2:   1.112      simple_2:   1.198
simple_6:   3.196      simple_6:   2.988      simple_6:   4.749
simple_5:   3.564      simple_5:   3.627      simple_5:   6.329
simple_4:   4.025      simple_4:   4.031      simple_4:   9.605
simple_0:   4.353      simple_0:   4.576      simple_3:   9.896
simple_3:   4.745      simple_3:   4.784      simple_0: 124.409
Хорошия алгоритм при правильной реализации дает прирост в десятки-сотни раз.
Алгоритм "Решето Эратосфена" сильнее проявляется на поиске больших простых чисел.
Если на малых числах "simple0 (через перебор делителей" пытается конкурировать с
"решетом Эратосфена", то на больших сильно отстает.
Порадовало, что моя реализация, написанная после изучения предыдущих, оказалась на 3-м месте.
Первая, написанная в лоб, отставала даже от simple_0. Было откровением для меня операция типа:
xxx[0::2] = [0] * (len(xxx) // 2) и то что работает она в 15 раз быстрее цикла, и, то что изменения в срезе
списка происходят в самом списке. Думал, что срез создает новый список в памяти. Очень полезная задача!
'''
