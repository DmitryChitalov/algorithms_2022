"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
import memory_profiler
import sys

sys.setrecursionlimit(3000)

def recursive_series_of_numbers(n: int, num: float = 1.0) -> float:
    """
    Задание 4, Урок 2.
    Найти сумму n элементов следующего ряда чисел:
    1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры.
    """
    return num if n <= 1 else num + recursive_series_of_numbers(n-1, num=num / -2)

@memory_profiler.profile
def wrapper(recursive_func, arg):
    result = recursive_func(arg)
    return result


if __name__ == "__main__":
    print(wrapper(recursive_series_of_numbers, 2950))

    """
    Проблема: 
        Каждый раз когда рекурсивная функция вызывает сама себя, профилировщй профилирует именно этот вызов функции,
        тоесть если функция вызовет сама себя n колличество раз, профилировщик будет замерять n колличество раз вызов 
        функции.
        
    Решение: 
        Завернуть рекурсивную функцию в функцию обертку и замерить потребление памяти функцией, таким образом 
        профилировщик вызовется 1 раз. Из минусов не видно сколько раз функция сама себя вызвала.
        
        Так же можно написать свой декоратор который будет замерять расход памяти, но решение будет 
        примерно таким же.
        
    Профилирование памяти: 
    
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        38     18.8 MiB     18.8 MiB           1   @memory_profiler.profile
        39                                         def decor_for_recursive(recursive_func, arg):
        40     20.5 MiB      1.7 MiB           1       result = recursive_func(arg)
        41     20.5 MiB      0.0 MiB           1       return result
    """