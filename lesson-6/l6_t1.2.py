from memory_profiler import profile
from random import random


@profile
def wr_rev_num(num):
    def reverse_num(num, answ=''):
        if num // 10 == 0:
            answ += str(num % 10)
            return f'Перевернутое число: {answ}'
        return reverse_num(num // 10, answ + str(num % 10))

    return reverse_num(num)


@profile
def reverse_num(num):
    return int(str(num)[::-1])


num = round(random() * (10 ** 100))

print(wr_rev_num(num))
print(reverse_num(num))

# убираем рекурсию срезом для уменьшения требуемой памяти
