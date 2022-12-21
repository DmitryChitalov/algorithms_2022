"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
from memory_profiler import memory_usage

user_number = 100


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# @decor
# def recur_sum(number):
#     if number == 1:
#         return number
#     else:
#         return recur_sum(number-1)[0] + number
#
#
# recur_check, mem1 = recur_sum(user_number)
# print(recur_check)
# if recur_check == user_number * (user_number + 1) / 2:
#     print('Равенство верно!')
#  print(mem1)
# Выполнение заняло 0.20703125 Mib

# Используем цикл
@decor
def cycle_sum(number):
        s = 0
        for num in range(1, number + 1):
            s += num
        return s


cycle_check, mem2 = cycle_sum(user_number)
if cycle_check == user_number * (user_number + 1) / 2:
    print('Равенство верно!')
print(mem2)
# Выполнение заняло 0.00390625 Mib