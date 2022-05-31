"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""

# Урок 5. Задание 2

from collections import deque
from itertools import zip_longest
from memory_profiler import profile

DEC_TO_HEX = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


@profile
def hex_add(n1: list, n2: list) -> list:
    # Сложение столбиком.
    # С помощью zip_longest формируется кортеж, состоящий из пар, которые будут складываться
    # если какой-то список короче, то недостающие элемены заполняются нулями
    tup_to_sum = tuple(zip_longest(reversed(n1), reversed(n2), fillvalue='0'))
    remainder = False
    res = deque()  # В дек будем складывать ответ, дополняя дек слева

    for itm in tup_to_sum:
        # По заданию разрешается пользоваться int(, 16). Поэтому использую этот метод, для преобразования в десятичную
        # систему. Хотя можно было бы сдалать словарь обратный словарю DEC_TO_HEX
        d = sum(map(lambda x: int(x, 16), itm)) + remainder
        if d >= 16:
            remainder = True
            d -= 16
        else:
            remainder = False
        res.appendleft(DEC_TO_HEX[d])
    del tup_to_sum
    if remainder:
        res.appendleft(DEC_TO_HEX[remainder])
    return list(res)


@profile
def hex_add_mem(n1: list, n2: list) -> list:
    # Сложение столбиком.
    # С помощью zip_longest формируется кортеж, состоящий из пар, которые будут складываться
    # если какой-то список короче, то недостающие элемены заполняются нулями
    tup_to_sum = zip_longest(reversed(n1), reversed(n2), fillvalue='0')
    remainder = False
    res = deque()  # В дек будем складывать ответ, дополняя дек слева

    for itm in tup_to_sum:
        # По заданию разрешается пользоваться int(, 16). Поэтому использую этот метод, для преобразования в десятичную
        # систему. Хотя можно было бы сдалать словарь обратный словарю DEC_TO_HEX
        d = sum(map(lambda x: int(x, 16), itm)) + remainder
        if d >= 16:
            remainder = True
            d -= 16
        else:
            remainder = False
        res.appendleft(DEC_TO_HEX[d])
    del tup_to_sum
    if remainder:
        res.appendleft(DEC_TO_HEX[remainder])
    return list(res)


if __name__ == '__main__':
    num1 = ''.join(('A2' for _ in range(10000)))
    num2 = ''.join(('C4F' for _ in range(10000)))
    hex_add(list(num1), list(num2))
    hex_add_mem(list(num1), list(num2))

"""
tup_to_sum = tuple(zip_longest(reversed(n1), reversed(n2), fillvalue='0'))
можно заменить на 
tup_to_sum =zip_longest(reversed(n1), reversed(n2), fillvalue='0')

так как нет необходимости в произвольном или повторном доступе к этим данным. Их нужно один раз обойти в цикле.
А метод zip_longest как раз возвращает итерируемый объект и потребляет меньше памяти.
"""
