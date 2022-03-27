"""
Задание 1.

Это файл для второго скрипта
"""
from sys import getsizeof
from collections import namedtuple


#  Не оптимизированная
def num_translate():
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    print(getsizeof(numbers))
    return numbers.get('ten')


# Оптимизированная
def num_translate_tuple():
    dict_ = namedtuple('dict_', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
    d = dict_(one='один',
              two='два',
              three='три',
              four='четыре',
              five='пять',
              six='шесть',
              seven='семь',
              eight='восемь',
              nine='девять',
              ten='десять'
    )
    print(getsizeof(d))
    return d.ten


num_translate()
num_translate_tuple()

"""
с namedtuple мы выигрываем по памяти в 3 раза
"""