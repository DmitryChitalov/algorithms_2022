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

Это файл для третьего скрипта
"""
from memory_profiler import profile, memory_usage

from collections import namedtuple


def memory(func):
    def wrapper():
        start = memory_usage()
        my_func = func()
        stop = memory_usage()
        result = stop[0] - start[0]
        return my_func, print(result)

    return wrapper()


@memory
def accounting():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    company_add = {}
    for i in range(count):
        name_company = input('Введите название предприятия: ')
        x, y, z, v = input('Через пробел введите прибыль данного предприятия'
                           ' за каждый квартал(Всего 4 квартала): ').split(' ')
        RES = namedtuple('accounting', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        RESUME_NAME = RES(
            name=name_company,
            quarter_1=x,
            quarter_2=y,
            quarter_3=z,
            quarter_4=v
        )
        company_add[RESUME_NAME.name] = (int(RESUME_NAME.quarter_1) + int(RESUME_NAME.quarter_2)
                                         + int(RESUME_NAME.quarter_3) + int(RESUME_NAME.quarter_4)) / 4
    profit_max = [k for k, v in company_add.items() if v == max(company_add.values())][0]
    profit_min = [k for k, v in company_add.items() if v == min(company_add.values())][0]
    print('Средняя прибыль по', count, 'предприятиям', (sum(company_add.values())) / count, '\n',
          'Предприятие с максимальной прибылью,', profit_max, '-', company_add[profit_max], '\n',
          'Предприятие с минимальной прибылью,', profit_min, '-', company_add[profit_min])


# accounting()


@memory
def accounting_optimus():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    company_add = {}
    for i in range(count):
        name_company = input('Введите название предприятия: ')
        x, y, z, v = input('Через пробел введите прибыль данного предприятия'
                           ' за каждый квартал(Всего 4 квартала): ').split(' ')
        RES = namedtuple('accounting', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        RESUME_NAME = RES(
            name=name_company,
            quarter_1=x,
            quarter_2=y,
            quarter_3=z,
            quarter_4=v
        )
        company_add[RESUME_NAME.name] = (int(RESUME_NAME.quarter_1) + int(RESUME_NAME.quarter_2)
                                         + int(RESUME_NAME.quarter_3) + int(RESUME_NAME.quarter_4)) / 4
    profit_max = [k for k, v in company_add.items() if v == max(company_add.values())][0]
    profit_min = [k for k, v in company_add.items() if v == min(company_add.values())][0]
    print(f'Средняя прибыль по {count} предприятиям, {(sum(company_add.values())) / count} \n \
          Предприятие с максимальной прибылью {profit_max} -  {company_add[profit_max]} \n\
          Предприятие с минимальной прибылью {profit_min} - {company_add[profit_min]}')


# accounting_optimus()

'''Использовал f строку, так как она использует меньше оперативной памяти'''