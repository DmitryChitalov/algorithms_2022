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
Это файл для второго скрипта
"""
import sys
from memory_profiler import memory_usage
from recordclass import recordclass
from collections import namedtuple


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

# ------------ Вариант до оптимизации ----------------------
@decor
def check_even_1():
    all_comp = []
    try:
        count_com = int(input('Введите количество предприятий для расчета прибыли: '))
        for i in range(count_com):
            name_com = input('Введите название компании: ')
            company = namedtuple(name_com, ['name_com', 'first_q', 'second_q', 'third_q', 'fourth_q', 'year']) # оптим
            income = [int(x) for x in input('Через пробел введите прибыль данного предприятия: ').split()]
            name_com = company(name_com, *income, sum(income))
            print(f'Объём занимаемой объектом namedtuple памяти:{sys.getsizeof(name_com)} байт(а)')
            all_comp.append(name_com)
    except Exception:
        print('Введите корректные данные')
    else:
        inc = 0
        for i in range(len(all_comp)):
            inc += all_comp[i].year
        inc = inc / len(all_comp)
        print(f'Средняя годовая прибыль всех предприятий: {inc}')
        print(*(f'Предприятия, с прибылью выше среднего значения:'
                f' {all_comp[i].name_com}' for i in range(len(all_comp)) if all_comp[i].year > inc), sep=' ')
        print(*(f'Предприятия, с прибылью ниже среднего значения:'
                f' {all_comp[i].name_com}' for i in range(len(all_comp)) if all_comp[i].year < inc), sep=' ')


if __name__ == '__main__':

    res, mem_diff = check_even_1()
    print(f"Выполнение заняло {mem_diff} Mib")


# ------------ Вариант после оптимизации ----------------------
@decor
def check_even_2():
    all_comp = []
    try:
        count_com = int(input('Введите количество предприятий для расчета прибыли: '))
        for i in range(count_com):
            name_com = input('Введите название компании: ')
            company = recordclass(name_com, ['name_com', 'first_q', 'second_q', 'third_q', 'fourth_q', 'year']) # оптим
            income = [int(x) for x in input('Через пробел введите прибыль данного предприятия: ').split()]
            name_com = company(name_com, *income, sum(income))
            print(f'Объём занимаемой объектом recordclass памяти:{sys.getsizeof(name_com)} байт(а)')
            all_comp.append(name_com)
    except Exception:
        print('Введите корректные данные')
    else:
        inc = 0
        for i in range(len(all_comp)):
            inc += all_comp[i].year
        inc = inc / len(all_comp)
        print(f'Средняя годовая прибыль всех предприятий: {inc}')
        print(*(f'Предприятия, с прибылью выше среднего значения:'
                f' {all_comp[i].name_com}' for i in range(len(all_comp)) if all_comp[i].year > inc), sep=' ')
        print(*(f'Предприятия, с прибылью ниже среднего значения:'
                f' {all_comp[i].name_com}' for i in range(len(all_comp)) if all_comp[i].year < inc), sep=' ')


if __name__ == '__main__':

    res, mem_diff = check_even_2()
    print(f"Выполнение заняло {mem_diff} Mib")

'''
Курс:"Алгоритмы и структуры данных на Python", ДЗ №2, task 7
Для двух фирм, получаем:
При использовании recordclass выполнение занимает 0.0390625 Mib, при namedtuple - 0.08984375 Mib,
Объём занимаемой объектом namedtuple памяти:88 байт(а), объём занимаемой объектом recordclass памяти:64 байт(а).
С точки зрения минимизации расходования памяти recordclass предпочтительнее. Кроме того, recordclass является 
изменяемым объектом.
'''