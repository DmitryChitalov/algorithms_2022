"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage


def memory_using(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args, *kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        _, _, _, step = args
        if step == 0:
            return res, mem_diff
        return res

    return wrapper


@memory_using
def odd_even_count_recursion(number, odd_count, even_count, step):
    if number == 0:
        return odd_count, even_count
    else:
        digit = number % 10
        if digit % 2:
            even_count += 1
        else:
            odd_count += 1
        step += 1
        return odd_even_count_recursion(number // 10, odd_count, even_count, step)


if __name__ == '__main__':
    number = int(input('Введите число:  '))
    result, memory = odd_even_count_recursion(number, 0, 0, 0)
    print(f'Количество четных и нечетных цифр в числе равно: {result}')
    print(f'Затраченная память: {memory}')

    # Добавил внутрь основной функции номер шага рекурсии.
    # В декораторе, считающем память, возвращаю ее только на первом шаге рекурсии.
    # Не уверен, что это верное решение.
