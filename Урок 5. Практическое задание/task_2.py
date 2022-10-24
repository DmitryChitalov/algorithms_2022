"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import defaultdict
from functools import reduce


# 1 через defaultdict
def sum_func(*args):
    sum_res = 0
    for value in args:
        sum_res += int(''.join(value), 16)
    return list(f'{sum_res:X}')


def mult_func(*args):
    mult_res = 1
    for value in args:
        mult_res *= int(''.join(value), 16)
    return list(f'{mult_res:X}')


# 2 через ООП
# я не знаю, можно ли было список соединять обратно в строку, как в решении через defaultdict,
# поэтому здесь пошёл длинным путём. Получилась как-то громоздко. Вряд ли от меня это требовалось.
# но удалить рука не поднялась)

class HexNumber:
    def __init__(self, number):
        self.number = list(number)

    def pop(self):
        return self.number.pop()

    def __add__(self, number):
        num_1 = self.number.copy()
        num_2 = number.number.copy()
        if len(num_1) < len(num_2):
            num_2, num_1 = num_1, num_2
        result = []
        memory = 0
        for i in range(len(num_2)):
            temp = int(num_1.pop(), 16) + int(num_2.pop(), 16) + memory
            memory = temp // 16
            write = temp % 16
            result.append(f'{write:X}')

        for j in range(len(num_1)):
            if num_1[-1] == 'F':
                result.append('0')
                num_1.pop()
                memory = 1
            else:
                result.append(f'{int(num_1.pop(), 16) + memory:X}')
                memory = 0
        return result[::-1]

    def __mul__(self, number):
        num_1 = self.number.copy()
        num_2 = number.number.copy()
        result = []
        for i in range(1, len(num_1) + 1):
            level_result = []
            memory = 0
            for j in range(1, len(num_2) + 1):
                temp = int(num_1[-i], 16) * int(num_2[-j], 16) + memory
                memory = temp // 16
                write = temp % 16
                level_result.append(f'{write:X}')
            if memory:
                level_result.append(f'{memory:X}')
            result.append(HexNumber((level_result[::-1] + (i - 1) * ['0'])))
        res_sum = result[0]
        for i in range(1, len(result)):
            res_sum.number = res_sum + result[i]
        return res_sum.number


if __name__ == '__main__':
    first_number = 'A2'
    second_number = 'C4F'

    # 1 через defaultdict
    hex_numbers = defaultdict(list)
    hex_numbers['first'] = list(first_number)
    hex_numbers['second'] = list(second_number)
    sum_result = reduce(sum_func, hex_numbers.values())
    mult_result = reduce(mult_func, hex_numbers.values())
    print('сумма через defaultdict: ', sum_result)
    print('произведение через defaultdict: ', mult_result)

    # 1 через ООП
    frst = HexNumber(first_number)
    scnd = HexNumber(second_number)
    print('сумма через ООП: ', frst + scnd)
    print('произведение через ООП: ', frst * scnd)
