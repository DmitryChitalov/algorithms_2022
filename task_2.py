# Collections

from collections import defaultdict


def calc():
    nums = defaultdict(list)
    for i in range(2):
        num = input('Введите число в шестнадцатеричной системе счисления: ')
        nums[f'{num}'] = list(num)
        
    print('Collections: ')
    sum_ = sum([int(''.join(i), 16) for i in nums.values()])
    a = [i for i in str(hex(sum_)).upper()[2:]]
    print(f'Сумма этих чисел: {a}')

    mul_ = int(''.join(nums.popitem()[1]), 16) * int(''.join(nums.popitem()[1]), 16)
    b = [i for i in str(hex(mul_)).upper()[2:]]
    print(f'Произведение этих чисел: {b}')


# ООП


class hex_num:
    def __init__(self, num: str):
        self.num = num

    def __mul__(self, other) -> list:
        a = [i for i in (hex(int(self.num, 16) * int(other.num, 16)).upper()[2:])]
        return a

    def __add__(self, other) -> list:
        b = [i for i in (hex(int("".join(self.num), 16) + int("".join(other.num), 16)).upper()[2:])]
        return b


if __name__ == '__main__':
    # Collections
    calc()
    # ООП
    print('ООП: ')
    print("Сумма: ", hex_num('A2') + hex_num('C4F'))
    print("Умножение: ", hex_num('A2') * hex_num('C4F'))
