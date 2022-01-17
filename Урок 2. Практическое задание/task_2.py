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
from enum import Enum


class OddOrEven(Enum):
    ODD = 1
    EVEN = 2

def get_number(mess):
    try:
        num = int(input(mess))
        return num
    except ValueError:
        print('You enter wrong number')
        return get_number(mess)

def calc_odd_even(number):
    odd_even = {'odd': 0, 'even': 0}

    def recursion_calc(number):
        if number < 10:
            odd_even['odd'] += 1
            return OddOrEven.EVEN

        number = number // 10

        if recursion_calc(number) == OddOrEven.ODD:
            odd_even['odd'] += 1
            return OddOrEven.EVEN
        else:
            odd_even['even'] += 1
            return OddOrEven.ODD

    recursion_calc(number)
    return odd_even

def calc_odd_even2(number):
    if number < 10:
        return {'odd': 1, 'even': 0}

    number = number // 10
    odd_even = calc_odd_even2(number)
    is_even_number_now = bool((odd_even['odd'] + odd_even['even']) % 2)
    if is_even_number_now:
        return {'odd': odd_even['odd'], 
                'even': odd_even['even'] + 1}
    else:
        return {'odd': odd_even['odd'] + 1, 
                'even': odd_even['even']}

num = get_number('Enter number for calculater odd and even digits: ')

print(calc_odd_even(num))

print(calc_odd_even2(num))