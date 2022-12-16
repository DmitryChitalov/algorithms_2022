"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile, memory_usage
from pympler.asizeof import asizeof
def memory(func):
    def wrapper(*args, **kwargs):
        start = memory_usage()
        my_func = func(*args)
        stop = memory_usage()
        result = stop[0] - start[0]
        return my_func, result

    return wrapper

@memory
def revers_num2(num, list1=''):
    count = len(str(num))
    if count == 1:
        print(str(list1) + str(num % 10))
    else:
        count -= 1
        list1 = str(list1) + str(num % 10)
        num //= 10
        return revers_num2(num, list1)
print(asizeof(revers_num2(3699632345543212548)))

'''при профилировании памяти функции с рекурсией через @profile память считается за каждый вызов функции в рекурсии,
рабочий вариант, это Декоратор memory_usage обернутый в asizeof'''

