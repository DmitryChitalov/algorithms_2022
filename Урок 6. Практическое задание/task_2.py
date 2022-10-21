"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


@profile
def measuring(func):
    def wrapper(*args):
        res = func(*args)
        return res
    return wrapper


@measuring
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers(enter_num, revers_num)


n = 123456789
print(revers(n))

"""
Если профилировать рекурсию, мы получим столько таблиц,
сколько будет вызовов функции. 
Чтобы этого избежать можно обернуть рабочую функцию в другую функцию
и замерить использование памяти уже для неё
"""
