"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
 """
Проблема при замерах рекурсии - это то что выдаются данные  большого количества таблиц.
 Решением этого может являться декоратор либо обертка, которая сведет все в одну таблицу
 """
from memory_profiler import memory_usage

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


numbers_list = []


@decor
def reversed_number(number):
    rev_num = ''.join(numbers_list)
    if number == 0:
        return rev_num
    else:
        new_number = str(number % 10)
        numbers_list.append(new_number)
        return reversed_number(number // 10)



my_number = 123859423651489621233194648783928465473829284645592927
print(reversed_number(my_number))
