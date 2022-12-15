"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опишите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile

@profile
def even_and_odd_count(number, even_count=0, odd_count=0):
    if number == 0:
        return f'Количество четных и нечетных цифр в числе равно: {even_count, odd_count}'
    else:
        if (number % 10) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        return even_and_odd_count(number//10, even_count, odd_count)


@profile
def helper_func(number):
    return even_and_odd_count(number)


if __name__ == "__main__":
    number_test = 243
    print(even_and_odd_count(number_test))
    print(helper_func(number_test))


# Проблема в том, что происходит замер потребляемой памяти на каждом рекурсивном шаге и на каждом возврате из стека вызовов.
# Решение: создание вспомогательной функции, которая возвращает результат выполнения рекурсивной функции, таким образом,
# во время вызова вспомогательной функции происходит замер потребляемой памяти всей рекурсивной функции.
