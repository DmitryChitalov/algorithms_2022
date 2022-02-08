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
def circuit():
    def recursive_reverse_mem(number):
        return '' if number == 0 else f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
    return recursive_reverse_mem


if __name__ == '__main__':
    print(circuit()(1234567890))

# Используем замыкание функции, чтобы profile не отрабатывал каждый вызов рекурсивной функции.
# profile вызывает теперь circuit, которая возвращает результат recursive_reverse_mem.
