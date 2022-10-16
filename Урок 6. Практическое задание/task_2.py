"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage
from memory_profiler import profile


# Вариант 1.
# Этот вариант запускается столько раз, сколько выполняется рекурсия, поэтому замеры получаются на каждый
# запуск отдельные

@profile
def count(num, even=0, odd=0):
    if num < 1:
        print(f'Четных цифр {even}, нечетных цифр {odd}')
        return
    else:
        if (num % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return count(num // 10, even, odd)


if __name__ == "__main__":
    count(12345)


# Вариант 2.
# Чтобы нам замерить результаты выполнение функции в целом мы можем использовать  обертку (wrapper).

@profile
def wrapper(number):
    def count_2(num, even=0, odd=0):
        if num < 1:
            print(f'Четных цифр {even}, нечетных цифр {odd}')
            return
        else:
            if (num % 10) % 2 == 0:
                even += 1
            else:
                odd += 1
            return count_2(num // 10, even, odd)

    return count_2(number)


if __name__ == "__main__":
    mem_diff = wrapper(12345)
