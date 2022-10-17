"""
Алгоритмы и структуры данных на Python. Базовый курс.
Урок 2.
Задание 3.	Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
Не забудьте проверить на числе, которое оканчивается на 0.
1230 -> 0321
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

"""Исходный скрипт"""

@memory
def reversator(num, revers_num='Зеркальное число: '):
    if num == 0:
        return revers_num
    else:
        n = num % 10
        num = num // 10
    return reversator(num, str(revers_num + str(n)))


try:
    number = int(input('Введите число '))
    print(reversator(number))
except ValueError:
    print('Тип введенных данных не является числом')

"""Я выполнила оптимизацию, за счёт исключения рекурсии и решения задачи путём конвертации числа 
в строку и реверсивного вывода полученных элементов
Оптимизированный скрипт:"""


@memory
def reversator_2():
    return str(number)[::-1]


print(reversator_2())
