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
Попытайтесь решить это задание в двух вариантах.
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from functools import reduce
from collections import defaultdict

print('1-й вариант')
# 1-й вариант. Для тренировки defaultdict создаем вложенную структуру

# Собираем операции умножения и деления в defaultdict со следующей структурой, нпр для 0xA9 и 0xf:
# {0: {'hex': [['a', '9'], ['f']], 'dec': [169, 15], 'sum': ['b', '8'], 'mul': ['9', 'e', '7']}}

dd = defaultdict(lambda: defaultdict(list))


def next_stm(op1, op2):
    new_key = 0 if not dd else max(dd.keys()) + 1
    dd[new_key]['hex'] = [list(op1), list(op2)]
    dd[new_key]['dec'] = [int(op1, 16), int(op2, 16)]
    dd[new_key]['sum'] = list(hex(reduce(lambda x, y: x + y, [dd[new_key]['dec'][0], dd[new_key]['dec'][1]]))[2:])
    dd[new_key]['mul'] = list(hex(reduce(lambda x, y: x * y, [dd[new_key]['dec'][0], dd[new_key]['dec'][1]]))[2:])
    return new_key


def print_dict_values():
    if dd:
        for i in dd:
            print(f"[{''.join(dd[i]['hex'][0])}, {''.join(dd[i]['hex'][1])}]:", end=' ')
            print(f"Сумма: {''.join(dd[i]['sum'])}, произведение: {''.join(dd[i]['mul'])}")
    else:
        print('Словарь пустой')


[next_stm(i, j) for i, j in [('a2', 'c4f'), ('fff', 'fff'), ('a000', 'c001'), ('ee01', 'a0')]]
print_dict_values()

print('2-й вариант')


# 2-й вариант. Создаем класс HexNumber и определяем для него операции '*', '+' и строковое представление
class HexNumber:
    def __init__(self, number):
        self.num = list(number)

    def __add__(self, other):
        return HexNumber(''.join(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16))[2:]))

    def __mul__(self, other):
        return HexNumber(''.join(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16))[2:]))

    def __str__(self):
        return ''.join(self.num)


print(HexNumber('a2') + HexNumber('c4f'))  # cf1
print(HexNumber('a2') * HexNumber('c4f'))  # 7c9fe
