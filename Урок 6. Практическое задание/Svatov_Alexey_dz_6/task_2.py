"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""

from memory_profiler import profile


@profile
def wrap_decoding(*args):
    return decoding(*args)


def decoding(first_symbol, last_symbol, count=1, result=''):
    if first_symbol <= last_symbol:
        return decoding(first_symbol + 1, last_symbol, count + 1,
                        result + f'{first_symbol} - {chr(first_symbol)} ') if count % 10 != 0 else decoding(
            first_symbol + 1, last_symbol, count + 1, result + f'{first_symbol} - {chr(first_symbol)}\n')
    else:
        return print(result)


wrap_decoding(32, 127)

"""
Проблема в том, что декоратор вызывается каждый раз, когда вызывается функция (в том числе рекурсивно).
Соответственно получается несколько результатов профилирования.

Вариант решения: функция-обёртка для декорируемой рекурсивной функции.
"""
