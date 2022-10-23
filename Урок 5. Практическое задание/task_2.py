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

# from collections import defaultdict


# def sum_nums_16(num1, num2):
  #  nums = defaultdict(list)

   # nums[f'{num1}'] = list(num1)
  #  nums[f'{num2}'] = list(num2)

 #   return list('%X' % sum([int(''.join(i), 16) for i in nums.values()]))


#def mult_nums_16(num1, num2):
  #  rez = 1
 #   nums = defaultdict(list)
#
  #  nums[f'{num1}'] = list(num1)
 #   nums[f'{num2}'] = list(num2)
#
  #  for i in nums.values():
 #       rez *= int(''.join(i), 16)
#
#    return list('%X' % rez)


#num1 = input('Введите первое 16-ое число: ').strip('')
#num2 = input('Введите второе 16-ое число: ').strip('')
#print(sum_nums_16(num1, num2))
#print(mult_nums_16(num1, num2))

class Num_16:
    def __init__(self, num):
        self.num = num.strip('')

    def __add__(self, other):
        return list(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:]


num1 = Num_16(input('Введите первое 16-ое число: '))
num2 = Num_16(input('Введите второе 16-ое число: '))

print(num1 + num2)
print(num1 * num2)
