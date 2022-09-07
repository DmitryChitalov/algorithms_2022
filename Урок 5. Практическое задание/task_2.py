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


class IncreaseNumbers:
    """ Сложениу и умножение двух шестнадцатеричных чисел """

    def __init__(self, num):
        self.num = list(num)

    def __repr__(self):
        return self.num

    def __str__(self):
        return f'Число сохранено : {self.num}'

    def __add__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        add_nums = list(hex(int(self.num, 16) + int(other.num, 16)).upper())
        return f'Сумма чисел: {add_nums[2:]}'

    def __mul__(self, other):
        self.num = ''.join(self.num)
        other.num = ''.join(other.num)
        mul_nuns = list(hex(int(self.num, 16) * int(other.num, 16)).upper())
        return f'Произведение - {mul_nuns[2:]}'


if __name__ == '__main__':
    first_number = input('Введите первое число: ')
    first_num = IncreaseNumbers(first_number)
    print(first_num)
    second_number = input('Введите второе число: ')
    second_num = IncreaseNumbers(second_number)
    print(second_num)
    print(first_num + second_num)
    print(first_num * second_num)
