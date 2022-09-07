"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


def prove_equality(n, total=0):
    if n < 1:
        return total
    else:
        total += n
    return prove_equality(n - 1, total)


@profile
def main(n):
    return n


n = 500
if __name__ == '__main__':
    print(main(prove_equality(n)))
    # prove_equality(n)
    print(prove_equality(n) == n * (n + 1) / 2)

"""
При каждом вызове рекурсии вызывается профайлер, в результате мы не видим общего значения потребления памяти.
Чтобы видеть реальный результат нужно делать декоратор или вызывать из другой функции
"""
