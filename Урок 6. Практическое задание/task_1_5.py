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
from recordclass import recordclass
from pympler import asizeof

'''
За основу взято задание 3.1 основы питона. Идея - заменить словарь на recordclass и посмотреть, что выйдет. К сожалению
изящного решения с recordclass у меня не получилось, но в части памяти эффект был. Так, размер словаря из первого
решения составил 2208, в то время как оптимизированный аналогичный словарь под recordclass всего 104.
'''


# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский
# вариант из домашнего задания
def num_translate(number):
    """number - число от 0 до 10 на английском"""
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
               'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return numbers[number]


# вариант с recordclass
def num_translate_2(number):
    """number - число от 0 до 10 на английском"""
    optim_var = recordclass('optim_var', ('zero', 'one', 'two', 'three', 'four', 'five',
                                          'six', 'seven', 'eight', 'nine', 'ten'))
    numbers = optim_var(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять',
                        six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')
    # return numbers.number не работает, поэтому пришлось через if, наверное есть более изящный способ(
    if number == 'zero':
        return numbers.zero
    elif number == 'one':
        return numbers.one
    elif number == 'two':
        return numbers.two
    elif number == 'three':
        return numbers.three
    elif number == 'four':
        return numbers.four
    elif number == 'five':
        return numbers.five
    elif number == 'six':
        return numbers.six
    elif number == 'seven':
        return numbers.seven
    elif number == 'eight':
        return numbers.eight
    elif number == 'nine':
        return numbers.nine
    elif number == 'ten':
        return numbers.ten


print(num_translate('zero'))
numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
           'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
print(asizeof.asizeof(numbers))  # => 2208
print(num_translate_2('zero'))
optim_var = recordclass('optim_var', ('zero', 'one', 'two', 'three', 'four', 'five',
                                      'six', 'seven', 'eight', 'nine', 'ten'))
numbers = optim_var(zero='ноль', one='один', two='два', three='три', four='четыре', five='пять',
                    six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')
print(asizeof.asizeof(numbers))  # => 104

