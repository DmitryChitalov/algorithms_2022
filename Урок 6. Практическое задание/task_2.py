"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage, profile

lst = []  # здесь будет храниться инфа по затраченной памяти


# свой декоратор, который сохраняет во внешний список данные по памяти во время каждого рекурсивного вызов
def mem_usage_decorator(some_func):
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        lst.append(str(memory_usage()))  # добавляем в список
        # значение задействованной памяти
        return result

    return wrapper


@mem_usage_decorator
def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        _ = [el for el in range(10 ** 6)]  # добавляем затратные
        # для памяти вычисления для тестирования
        return a * factorial(a - 1)


# Функция - обертка для рекурсивной функции. Замеряем память по ней
@profile
def wrapper_(b):
    def factorial_2(a):
        if a == 1 or a == 0:
            return 1
        else:
            return a * factorial_2(a - 1)

    return factorial_2(b)


if __name__ == '__main__':
    print('Способ N 1:')
    print(f'Задействованная память до запуска рекурсивной функции: '
          f'{str(memory_usage())} MB')
    print(f'Факториал числа: {factorial(10)}')

    for i, memory in enumerate(list(reversed(lst)), 1):
        print(f'Задействованная память после рекурсивного вызова '
              f'{i}-й раз: {memory} MB')

    print(f'Способ N 2:\n {wrapper_(10)}')
