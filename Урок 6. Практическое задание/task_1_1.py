"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

# Урок 2, задание 2

from memory_profiler import memory_usage


def mem_profiler(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        result = func(*args, **kwargs)
        m2 = memory_usage()
        print(m2[0] - m1[0])
        return result
    return wrapper


@mem_profiler
def wrap(var):
    def counting_even_odd(number, even_count=0, odd_count=0):
        """Подсчет количества четных и нечетных цифр числа number"""
        if number == 0:
            return even_count, odd_count

        last_digit = number % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        return counting_even_odd(number // 10, even_count, odd_count)

    return counting_even_odd(var)


@mem_profiler
def optimized(number):
    even_count = 0
    odd_count = 0
    while number != 0:
        last_digit = number % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10
    return even_count, odd_count


num = 742234523452345234523453742234523452345234523453
# wrap(num)
optimized(num)

"""
Замена рекурсии на цикл снизило выделение памяти
"""
