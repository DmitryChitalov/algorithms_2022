"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для третьего скрипта
"""
# Курс алгоритмы, урок 2, задание 3.


from memory_profiler import memory_usage


def memor_dec(func):
    def wrapper(*args):
        start = memory_usage()
        res = func(*args)
        return f'Заняло пямяти = {memory_usage()[0] - start[0]}'

    return wrapper


@memor_dec
def original(nums, even=0, odd=0):
    if nums > 0:
        ev = nums % 10
        if ev % 2 == 0:
            even += 1
        else:
            odd += 1
        return original(nums // 10, even, odd)
    return even, odd


nums = int(123456789987654321123456789987654321123456789987654321123456789987654321)
print(original(nums))


@memor_dec
def optimized(enter_num, revers_num=''):
    while enter_num != 0:
        revers_num = revers_num + str(enter_num % 10)
        enter_num //= 10
    return revers_num


print(optimized(123456789987654321123456789987654321123456789987654321123456789987654321))

"""
Помогла замена рекурсии на цикл
До:    0.25390625 MiB
После: 0.0 MiB
"""
