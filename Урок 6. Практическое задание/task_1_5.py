"""
КУРС: "Основы языка Python". Урок 1: "Основы языка Python". Задание 2.
Создать список, состоящий из кубов нечётных чисел `от 1 до 1000`, к
каждому элементу списка добавить `17` и вычислить сумму тех чисел из
этого списка, сумма цифр которых делится нацело на `7`.
"""
from memory_profiler import memory_usage
from pympler.asizeof import asizeof


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# https://github.com/AzarnykhOleg/Python-Basics/pull/2
@decor
def sum_list_1():
    """
Возвращает сумму кубов нечётных чисел от 1 до 100000, увеличенных на 17,
сумма цифр которых делится нацело на `7`
    :return: int
    """
    my_list = []
    for i in range(1, 100000, 2):
        my_list.append(i ** 3 + 17)
    sum_2 = 0
    for number in my_list:
        counter = 0
        sum_number = 0
        while number % 10 ** counter < number:
            sum_number += number % 10 ** (counter + 1) // 10 ** counter
            counter += 1
        if sum_number % 7 == 0:
            sum_2 += number
    return sum_2


# Обновлённый вариант
@decor
def sum_list_2():
    """
Возвращает сумму кубов нечётных чисел от 1 до 1000, увеличенных на 17,
сумма цифр которых делится нацело на `7`
    :return: int
    """
    sum_2 = 0
    for number in map(lambda x: x ** 3 + 17, range(1, 100000, 2)):
        counter = 0
        sum_number = 0
        while number % 10 ** counter < number:
            sum_number += number % 10 ** (counter + 1) // 10 ** counter
            counter += 1
        if sum_number % 7 == 0:
            sum_2 += number
    return sum_2


res, mem_diff = sum_list_1()
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 1.08203125 Mib
print(asizeof(sum_list_1()))
print('----------------- Новый вариант -----------------')
res, mem_diff = sum_list_2()
print(res)
print(f"Выполнение заняло {mem_diff} Mib")  # Выполнение заняло 0.0 Mib
print(asizeof(sum_list_2()))

"""
Отказ от создания списка позволил сэкономить 1.08203125 Mib.
"""
