"""
Алгоритмы и структуры данных на Python. Базовый курс.
Урок 4.
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper

"""Исходный код"""


@memory
def revers_5(enter_num):
    return ''.join(reversed(f'{enter_num}'))


enter_num = 77779999
print(revers_5(enter_num))

"""Я выполнила оптимизацию, за счёт замены return на yield
Оптимизированный скрипт:"""


@memory
def revers_(enter_num):
    yield reversed(str(enter_num))


enter_num = 77779999
print(revers_(enter_num))
