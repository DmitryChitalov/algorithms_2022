from collections import defaultdict
from functools import reduce

dict_num = defaultdict(list)

num_1 = input('Введите первое число: ')
num_2 = input('Введите второе число: ')

dict_num[num_1] = list(num_1)
dict_num[num_2] = list(num_2)

print(dict_num)

sum_nums = reduce(lambda a, b: a+b, [int(''.join(i), 16) for i in dict_num.values()])
mult_nums = reduce(lambda a, b: a*b, [int(''.join(i), 16) for i in dict_num.values()])
print(sum_nums, '\n', mult_nums, sep='')

sum_nums_hex = list(f'{sum_nums:X}')
mult_nums_hex = list(f'{mult_nums:X}')

print(f'Сумма введенных вами чисел: {sum_nums_hex}\nПроизведение: {mult_nums_hex}')
