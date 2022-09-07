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


def sum_number(num_1, num_2):
    """
    Функция сложения 10-ной системе и преобразование результата в 16-ную
    :param num_1: int
    :param num_2: int
    :return: list
    """
    total = hex(num_1 + num_2)
    return list(str(total).upper())[2:]


def mul_number(numb_1, numb_2):
    """
    Функция умножения чисел в 10-ной системе и преобразование результата в 16-ную
    :param numb_1: int
    :param numb_2: int
    :return: list
    """
    total = hex(numb_1 * numb_2)
    return list(str(total).upper())[2:]


def calculation_number():
    """
    Функция для запроса чисел от пользователя и конвертации
    их в списки элемментов и далее преоборазует 10-ную
    """
    user_inp_1 = list(input('Введите число в 16-ной системе: '))
    user_inp_2 = list(input('Введите второе число в 16-ной системе: '))
    number_1 = int(''.join(user_inp_1), 16)
    number_2 = int(''.join(user_inp_2), 16)
    print(f'Сумма чисел: {sum_number(number_1, number_2)}')
    print(f'Произведение чисел: {mul_number(number_1, number_2)}')


if __name__ == '__main__':
    calculation_number()


# Через ООП

class CalcNum:
    def __init__(self, num):
        self.num = int(''.join(num), 16)

    def __add__(self, other):
        total = str(hex(self.num + other.num))[2:].upper()
        return list(total)

    def __mul__(self, other):
        total = str(hex(self.num * other.num))[2:].upper()
        return list(total)


user_1 = list(input('Введите число в 16-ной системе: '))
user_2 = list(input('Введите второе число в 16-ной системе: '))

num_one = CalcNum(user_1)
num_two = CalcNum(user_2)

print(num_one + num_two)
print(num_one * num_two)
