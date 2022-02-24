from memory_profiler import memory_usage
from collections import namedtuple
from recordclass import recordclass
from statistics import mean

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


def mem(func):
    def wrapper(*args):
        start = memory_usage()
        func(args[0])
        stop = memory_usage()
        memory = stop[0] - start[0]
        return memory
    return wrapper


@mem
def count_sum(count_company):
    """Расчет прибыли предприятий и сравнение между собой"""
    company = namedtuple('company', 'name first second third four total')
    company_list = []
    avg = []
    up_avg = []
    down_avg = []
    for i in range(count_company):
        name = input('Введите имя компании: ')
        profit = [int(i) for i in input(
            'через пробел введите прибыль данного предприятия '
            'за каждый квартал(Всего 4 квартала): ').split(' ')]
        try:
            new = company(
                name=name,
                first=profit[0],
                second=profit[1],
                third=profit[2],
                four=profit[3],
                total=sum(profit)
            )
        except IndexError:
            return f'Вы указали прибыль не за все кварталы (4)'
        company_list.append(new)
        avg.append(sum(profit))
    for i in range(len(company_list)):
        if company_list[i].total > mean(avg):
            up_avg.append(company_list[i].name)
        else:
            down_avg.append(company_list[i].name)
    return f'Предприятия, с прибылью выше среднего значения: {up_avg}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {down_avg}'


# Тестируем recordclass
@mem
def count_sum_2(count_company):
    company = recordclass('company', 'name first second third four total')
    company_list = []
    avg = []
    up_avg = []
    down_avg = []
    for i in range(count_company):
        name = input('Введите имя компании: ')
        profit = [int(i) for i in input(
            'через пробел введите прибыль данного предприятия '
            'за каждый квартал(Всего 4 квартала): ').split(' ')]
        try:
            new = company(
                name=name,
                first=profit[0],
                second=profit[1],
                third=profit[2],
                four=profit[3],
                total=sum(profit)
            )
        except IndexError:
            return f'Вы указали прибыль не за все кварталы (4)'
        company_list.append(new)
        avg.append(sum(profit))
    for i in range(len(company_list)):
        if company_list[i].total > mean(avg):
            up_avg.append(company_list[i].name)
        else:
            down_avg.append(company_list[i].name)
    del company_list
    del avg
    del profit
    del company
    del new
    return f'Предприятия, с прибылью выше среднего значения: {up_avg}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {down_avg}'


if __name__ == '__main__':
    print(count_sum(2))
    print(count_sum_2(2))


"""Протестировал рекорд класс и получил весьма странные результаты:
оригинальная функция занимает 0.0234375, в то время как функция с recordclass
занимает 0.03515625, при одиночных замерах, модифицировать память не получилось
замена встроенного именнованого кортежа, на recordclass результата
 на текущих данных не дала не дала."""
