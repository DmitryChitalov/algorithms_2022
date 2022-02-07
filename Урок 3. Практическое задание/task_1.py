"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time


def time_report(func):
    def report():
        start = time.time()
        func()
        print(f'функция: {str(func)}, время выполнения: {time.time() - start}')

    return report


lst = list()
dct = dict()


# a)

@time_report
def filling_out_list():
    for i in range(1000000):
        lst.append(i)  # O(n)


@time_report
def filling_out_dict():
    for i in range(1000000):
        dct[i] = 0  # O(1)


filling_out_list()
filling_out_dict()


# Сложность заполнения словаря – O(1), поскольку они реализованы как хеш-таблицы.
# Временная сложность поиска в списке – это O(n),
# словарь основан на хешировании, поэтому он намного быстрее, чем списк.


# b)


@time_report
def change_list():
    for i in range(1000000):
        lst[i] = 1  # O(1)
    for i in range(10000):
        lst.pop(i)  # O(n)


@time_report
def change_dict():
    for i in range(1000000):
        dct[i] = 1  # O(1)
    for i in range(10000):
        dct.pop(i)  # O(1)


change_list()
change_dict()

# обращение по индексу в списке и по ключу в словаре имеют одинаковую сложность в О-нотации;
# а удаление из словаря выполняется быстрее, т.к. не приходится смещать элементы как в списке
