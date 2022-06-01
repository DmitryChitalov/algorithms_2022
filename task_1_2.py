"""
Курс: Алгоритмы и структуры данных на Python. Базовый курс
Урок: 2
Задание 3.
-----------------------------------------------------------------------------
Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
"""

from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        if args[0] == n:
            return res, mem_diff
        else:
            return res
    return wrapper


##############################################################################
"""
ИСХОДНОЕ РЕШЕНИЕ

Введенное значение: 12345678901234567890123456789012345678901234567890

Используемая память: 0.0859375 Mib
"""

@decor
def revers(n):
    return '' if n == 0 else str(n % 10) + revers(n // 10)


print('---> ИСХОДНОЕ РЕШЕНИЕ')
n = int(input('Введите число, которое требуется перевернуть: '))
res, mem_diff = revers(n)
print(f'Перевернутое число: {res}')
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')


##############################################################################
"""
ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ

Описание: алгоритм переписан через генератор, в результате чего не приходится
хранить весь набор переменных для всех шагов рекурсии одновременно 

Введенное значение: 12345678901234567890123456789012345678901234567890

Используемая память: 0.00390625 Mib
"""

def gen_revers(n):
    len_n = 1
    while n // pow(10, len_n) > 0:
        len_n += 1
    for i in range(len_n):
        yield (n // pow(10,i)) % 10

@decor
def optimize(n):
    return ''.join(str(x) for x in gen_revers(n))


print('---> ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ')
n = int(input('Введите число, которое требуется перевернуть: '))
res, mem_diff = optimize(n)
print(f'Перевернутое число: {res}')
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')