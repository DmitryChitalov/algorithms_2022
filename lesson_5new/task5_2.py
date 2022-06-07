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
from collections import deque

# перевод из шестнадцатеричной системы в десятичную
def my_dec(string):
    dec = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dec += array_hex[num[i]] * 16 ** i
    return dec

# перевод из десятичной в шестнадцатеричную систему
def my_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in array_hex:
            if array_hex[i] == d:
                num.append(i)
                break
        numb //= 16
    num.reverse()
    return list(num)


num_hex = '0123456789ABCDEF'
array_hex = defaultdict(int)
coun_num = 0
for key in num_hex:
    array_hex[key] += coun_num
    coun_num += 1

num_1 = my_dec(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = my_dec(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')
