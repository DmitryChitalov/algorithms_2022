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
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(2))
# Проблема заключается в том, что декоратор @profile будет вызываться столько же раз
# сколько и рекурсивная функция вызыват сама себя. У меня два варианта решения данной проблемы.
# 1)


@profile
def fibonachi(num):
    lst = [1, 1]
    i = 2
    if num == 1:
        return 1
    else:
        while i != num:
            lst.append(lst[-2] + lst[-1])
            i += 1
    return lst[-1]


print(fibonachi(10))
# Заменил рекурсию на цикл.


# 2)
@profile
def decor(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci(n)


print(decor(10))
# Обернул рекурсивную функцию в обычную функцию.
