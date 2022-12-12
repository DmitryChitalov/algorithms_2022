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
from functools import reduce
import collections

data = collections.defaultdict(int)
num1 = input('Введите первое шестнадцатеричных число - ')
data[int(num1, 16)] = [i for i in num1]
num2 = input('Введите второе шестнадцатеричных число - ')
data[int(num2, 16)] = [i for i in num2]
sum_num = [i for i in hex(reduce(lambda x, y: x + y, data))[2:]]
multi = [i for i in hex(reduce(lambda x, y: x * y, data))[2:]]
print(f'Сумма чисел из примера: {sum_num}, произведение - {multi}.')

