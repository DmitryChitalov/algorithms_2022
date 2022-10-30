from memory_profiler import profile
from copy import deepcopy
from json import loads, dumps
from pympler import asizeof

"""
Задание из курса основ Python.
Написать функцию num_translate(), переводящую числительные от 0 до 10 c
английского на русский язык. Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где
лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи.
"""

@profile
def num_translate(num):
    num_en = deepcopy(num_base)
    return num_en.get(num)

@profile
def num_translate_1(num):
    num_en = loads(dumped_num_base)
    return num_en.get(num)


num_base = {
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
dumped_num_base = dumps(num_base)
print('Перевод:',
      num_translate(input('Ведите число на английском: ')))

print('Перевод:',
      num_translate_1(input('Ведите число на английском: ')))

print('Размер dict: ', asizeof.asizeof(num_base))
print('Размер json: ', asizeof.asizeof(dumped_num_base))


"""
Ведите число на английском: six

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    16     31.8 MiB     31.8 MiB           1   @profile
    17                                         def num_translate(num):
    18     31.8 MiB      0.0 MiB           1       num_en = deepcopy(num_base)
    19     31.8 MiB      0.0 MiB           1       return num_en.get(num)


Перевод: шесть

Ведите число на английском: six

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21     31.8 MiB     31.8 MiB           1   @profile
    22                                         def num_translate_1(num):
    23     31.8 MiB      0.0 MiB           1       num_en = loads(dumped_num_base)
    24     31.8 MiB      0.0 MiB           1       return num_en.get(num)


Перевод: шесть
Размер dict:  1784
Размер json:  456
"""
"""
При сериализаци словаря в формат json-строк мы видим, что хранение в json 
формате успользует памяти в несколько раз меньше, чем словарь
"""
