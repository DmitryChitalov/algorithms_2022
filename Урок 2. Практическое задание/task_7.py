"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать функцибю-рекурсию только для левой части выражения!
Результат нужно сверить с правой частью.

Решите через рекурсию. Решение через цикл не принимается.
"""


def sequence_sum(num, current_num=1, sum1=0):
    print(f'{current_num}', end='')
    sum1 += current_num
    if current_num == num:
        print(f' = {sum1} ')
        return
    current_num += 1
    print(f' + ', end='')
    sequence_sum(num, current_num, sum1)


if __name__ == '__main__':
    for number in range(1, 10):
        print(f'\n for  N = {number} :')
        sequence_sum(number)
        print (f'{number} * ({number} + 1)/2  = {int(number * (number + 1) / 2)} ')

# Script Listing:
#
#  for  N = 1 :
# 1  = 1
# 1 * (1 + 1)/2  = 1
#
#  for  N = 2 :
# 1 + 2  = 3
# 2 * (2 + 1)/2  = 3
#
#  for  N = 3 :
# 1 + 2 + 3  = 6
# 3 * (3 + 1)/2  = 6
#
#  for  N = 4 :
# 1 + 2 + 3 + 4  = 10
# 4 * (4 + 1)/2  = 10
#
#  for  N = 5 :
# 1 + 2 + 3 + 4 + 5  = 15
# 5 * (5 + 1)/2  = 15
#
#  for  N = 6 :
# 1 + 2 + 3 + 4 + 5 + 6  = 21
# 6 * (6 + 1)/2  = 21
#
#  for  N = 7 :
# 1 + 2 + 3 + 4 + 5 + 6 + 7  = 28
# 7 * (7 + 1)/2  = 28
#
#  for  N = 8 :
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8  = 36
# 8 * (8 + 1)/2  = 36
#
#  for  N = 9 :
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9  = 45
# 9 * (9 + 1)/2  = 45
#
# Process finished with exit code 0