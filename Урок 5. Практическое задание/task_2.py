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

def sum():
    lst = [('one',list(input('Введите первое число: '))),('two',list(input('Введите второе число: ')))]
    nums = defaultdict(list)
    print(*nums)
    for key,values in lst:
        nums[key] = values
    print(nums)

    sum = hex(int(''.join(nums['one']),16) + int(''.join(nums['two']),16))
    mult = hex(int(''.join(nums['one']),16) * int(''.join(nums['two']),16))
    print(f' сумма: {list(str(sum))}')
    print(f' Произведение: {list(str(mult))}')

class MyOperations():

    def __init__(self,num):
        self.value = list(str(num))

    def __add__(self, other):
        sum = hex(int(''.join(self.value),16) + int(''.join(other.value),16))
        return MyOperations(sum)

    def __mul__(self, other):
        mult = hex(int(''.join(self.value), 16) * int(''.join(other.value), 16))
        return MyOperations(mult)


if __name__ == '__main__':

sum()

obj = MyOperations('f') + MyOperations(1)
print(f'summa: {obj.value}')
obj = MyOperations('f') * MyOperations('f')
print(f'multiplaction: {obj.value}')
