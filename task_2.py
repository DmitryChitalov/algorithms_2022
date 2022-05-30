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

##############################################################################
"""
Вариант 1: через collections
"""

from collections import defaultdict


def list_to_defaultdict(value):
    # базовые словари для работы с шестнадцатиричной системой
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # преобразование слагаемого в defaultdict:
    # ключ - порядковый номер разряда (справа налево)
    # значение - значение разряда в десятичной системе
    return defaultdict(int, {len(value) - i - 1: hex_to_dec[value[i]] for i in range(len(value)-1,-1,-1)})


def defaultdict_to_list(value):
    # базовые словари для работы с шестнадцатиричной системой
    hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec_to_hex = {val: key for key, val in hex_to_dec.items()}

    return [dec_to_hex[value[i]] for i in range(len(value)-1,-1,-1)]


def add_oper(a, b):
    # преобразование слагаемых в defaultdict:
    a = list_to_defaultdict(a)
    b = list_to_defaultdict(b)

    # сложение столбиком
    c = defaultdict(int)
    add_next = 0
    n = max(len(a),len(b))
    for i in range(n):
        c[i] = (a[i] + b[i] + add_next) % 16
        add_next = (a[i] + b[i] + add_next) // 16
    if add_next > 0:
        c[n] = add_next

    return defaultdict_to_list(c)


def add_mul(a, b):
    # преобразование слагаемых в defaultdict:
    a = list_to_defaultdict(a)
    b = list_to_defaultdict(b)

    # умножение столбиком
    c = defaultdict(int)
    for j in range(len(b)):
        temp = defaultdict(int)
        add_next = 0
        for i in range(len(a)):
            temp[i] = (a[i] * b[j] + add_next) % 16
            add_next = (a[i] * b[j] + add_next) // 16
        if add_next > 0:
            temp[len(a)] = add_next

        # сложение с результатом умножения на очередной разряд
        c = defaultdict_to_list(c)
        temp = defaultdict_to_list(temp)
        temp.extend(['0' for k in range(j)])
        c = list_to_defaultdict(add_oper(c, temp))

    return defaultdict_to_list(c)


def check_add(a, b):
    a = '0x' + ''.join(a)
    b = '0x' + ''.join(b)
    return list(hex(eval(f'{a} + {b}')).upper()[2:])


def check_mul(a, b):
    a = '0x' + ''.join(a)
    b = '0x' + ''.join(b)
    return list(hex(eval(f'{a} * {b}')).upper()[2:])

# Тестирование
a = list(input('Введите 1-ое шестнадцатиричное число: '))  # A2
b = list(input('Введите 2-ое шестнадцатиричное число: '))  # C4F
print('========= Вариант 1 =========')
print('\t--------- СЛОЖЕНИЕ ---------')
print(f'\tРезультат: {add_oper(a, b)}')
print(f'\tПроверка:  {check_add(a, b)}')
print('\t--------- УМЕОЖЕНИЕ ---------')
print(f'\tРезультат: {add_mul(a, b)}')
print(f'\tПроверка:  {check_mul(a, b)}')
print()

##############################################################################
"""
Вариант 2: через ООП
Комментарий: чтобы не повторять код, перегрузил методы с помощью написанных
в Варианте 1 функций
"""

class Hex():
    def __init__(self, value):
        self.list_value = value

    def __add__(self, other):
        return Hex(add_oper(self.list_value, other.list_value))

    def __mul__(self, other):
        return Hex(add_mul(self.list_value, other.list_value))

    @property
    def value(self):
        return '0x' + ''.join(self.list_value).upper()


# Тестирование
print('========= Вариант 2 =========')
a_hex = Hex(a)
b_hex = Hex(b)
print(f'Число a: {a_hex.value}')
print(f'Число b: {b_hex.value}')
c_hex = a_hex + b_hex
print(f'Результат сложения: {c_hex.value}')
c_hex = a_hex * b_hex
print(f'Результат умножения: {c_hex.value}')