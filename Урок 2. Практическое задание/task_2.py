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


def check_num(number):
    even_numbers = 0
    odd_numbers = 0
    while number != 0:
        num = number % 10
        if num % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
        number = number // 10
    else:
        return print(even_numbers, odd_numbers)


def check_num2(number, even_numbers=0, odd_numbers=0):
    if number == 0:
        return print(even_numbers, odd_numbers)
    if number % 10 % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    return check_num2(number // 10, even_numbers, odd_numbers)


check_num(34560)
check_num2(34560)
