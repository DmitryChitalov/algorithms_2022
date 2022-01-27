"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

'''Первый вариант решения!'''

def number_even(number):
    if number == 0:
        return ''
    elif number % 10 % 2 == 0:
        return str(number % 10) + str(number_even(number // 10))
    else:
        return '' + str(number_even(number // 10))

def number_odd(number):
    if number == 0:
        return ''
    elif number % 10 % 2 != 0:
        return str(number % 10) + str(number_odd(number // 10))
    else:
        return '' + str(number_odd(number // 10))

number = int(input('Введите число: '))
print(f'Количество четных и нечетных цифр в числе равно: ({len(number_even(number))}, {len(number_odd(number))})')



'''Второй вариант решения!'''

def number_even_or_odd(number, _even, _odd):
    if number == 0:
        return {
            'even': _even,
            'odd': _odd
        }
    elif number % 10 % 2 == 0:
        _even += 1
    elif number % 10 % 2 != 0:
        _odd += 1
    return number_even_or_odd(number // 10, _even, _odd)

data = number_even_or_odd(int(input('Введите число: ')), 0, 0)
print(f'Количество четных и нечетных цифр в числе равно: ({data["even"]}, {data["odd"]})')


# def memorize(func):
#     def g(n, memory={}):
#         r = memory.get(n)
#         if r is None:
#             r = func(n)
#             memory[n] = r
#         return r
#     return g
#
#
# @memorize
# def f(n):
#     if n < 2:
#         return n
#     return f(n - 1) + f(n - 2)
#
#
# n = 8
# print(f(n))
