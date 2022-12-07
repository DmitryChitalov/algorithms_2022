"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import memory_usage, profile


def memory(func):
    def wrapper(*args):
        mem_1 = memory_usage(max_usage=True)
        func(*args)
        mem_2 = memory_usage(max_usage=True)
        mem_diff = mem_2 - mem_1
        return mem_diff
    return wrapper


@memory
def odd_or_even(number: int, odd_count=0, even_count=0):
    """
    Функция принимает в качестве аргументов исходное натуральное число и начальные значения счетчиков (четных
    и нечетных чисел), которые по умолчанию равны нулю, и выводит на экран количество четных и нечетных чисел,
    входящих в данное число.
    :param number: Исходное натуральное число
    :param odd_count: Начальное значение счетчика нечетных чисел
    :param even_count: Начальное значение счетчика четных чисел
    :return:
    """
    left = number // 10
    right = number % 10
    if right % 2 != 0:
        odd_count += 1
    else:
        even_count += 1
    if left != 0:
        odd_or_even(left, odd_count, even_count)
    else:
        print(f'Нечетных чисел {odd_count}, четных чисел {even_count} (включая нули)')


@profile
@memory
def odd_or_even_opt(number: str, odd_count=0, even_count=0):
    for i in range(len(number)):
        if int(number[i]) % 2 != 0:
            odd_count += 1
        else:
            even_count += 1
    print(f'Нечетных чисел {odd_count}, четных чисел {even_count} (включая нули)')


@profile
def do_other_func(number: int):
    return odd_or_even(number)


if __name__ == "__main__":
    print('\nЗа основу взят скрипт task_1_4.py из текущего д/з.\n'
          'Рекурсивная функция odd_or_even вызывается из вспомогательной функции do_other_func.\n'
          'В основной части программы вызывается вспомогательная функция.\n'
          'Профилирование выполняется именно для вспомогательной функции,\n'
          'и за счет этого предотвращются множественные вызовы функции вывода модуля memory_profiler')
    print('\nРаботу какой функции вы хотите проверить? (1 - исходная, 2 - оптимизированная): ', end='')
    mode = input()
    user_number = '45288179046261480180626678776300392807572401632'
    print(f'Число для разбора {user_number}')
    if mode == '1':
        mem = do_other_func(int(user_number))
        print(f'Выполнение заняло {mem} MiB')
    elif mode == '2':
        mem = odd_or_even_opt(user_number)
        print(f'Выполнение заняло {mem} MiB')
