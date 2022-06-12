from memory_profiler import profile
from random import random


@profile
def w_qua_n(num):
    def qua_n(num, e=0, o=0):
        e_count = 0
        o_count = 0
        if num % 10 % 2 == 0:
            e_count = 1
        else:
            o_count = 1
        if num // 10 == 0 and e_count:
            return e + 1, o
        elif num // 10 == 0 and o_count:
            return e, o + 1
        return qua_n(num // 10, e + e_count, o + o_count)

    return f'четных чисел - {qua_n(num)[0]} \nнечетных чисел - {qua_n(num)[1]}'


@profile
def mod_qua_n(num):
    return f'четных чисел - {len(list(el for el in str(num) if int(el) % 2 == 0))}' \
           f' \nнечетных чисел - {len(list(el for el in str(num) if int(el) % 2 != 0))}'


num = round(random() * (10 ** 100))

print(w_qua_n(num))
print(mod_qua_n(num))

# убираем рекурсию генератором для уменьшения требуемой памяти
