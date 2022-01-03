"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для третьего скрипта
"""

from pympler import asizeof
from recordclass import recordclass

# ДЗ 3, Задание 1 из Основ. Написать функцию, которая переводит числа от 1 до 10 с английского на русский.
# Без оптимизации:

transl = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(eng_num):
    if eng_num not in transl.keys():
        return 'Ошибка ввода'
    return transl[eng_num]

print(num_translate(input()))
print(asizeof.asizeof(transl))

# С оптимизацией:

rc = recordclass('translations', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
transl_rc = rc(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')

def num_translate(eng_num):
    if eng_num == 'one':
        return transl_rc.one
    elif eng_num == 'two':
        return transl_rc.two
    elif eng_num == 'three':
        return transl_rc.three
    elif eng_num == 'four':
        return transl_rc.four
    elif eng_num == 'five':
        return transl_rc.five
    elif eng_num == 'six':
        return transl_rc.six
    elif eng_num == 'seven':
        return transl_rc.seven
    elif eng_num == 'eight':
        return transl_rc.eight
    elif eng_num == 'nine':
        return transl_rc.nine
    elif eng_num == 'ten':
        return transl_rc.ten
    else:
        return 'Ошибка ввода'

print(num_translate(input()))
print(asizeof.asizeof(transl_rc))

# До оптимизации: 1784, после оптимизации: 96.
# Что изменил: Изменил словарь на recordclass
