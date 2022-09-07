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
# Исходный код: Урок 5. Практическое задание task_1.py
#
# Способ 5 минимизации расходования памяти. Использование возможностей
# модуля recordclass
#
from sys import getsizeof
from collections import namedtuple
from recordclass import recordclass


def enter_information(b_namedtuple=True):
    _companies = []
    _lst = ['profit1', 'profit2', 'profit3', 'profit4']

    count = int(input("Введите количество предприятий для расчета прибыли: "))
    for i in range(count):
        name = input("Введите название предприятия: ")
        str_profits = (input("Через пробел введите прибыль данного "
                             "предприятия за каждый квартал"
                             "(Всего 4 квартала): ")).split()
        int_profits = list(map(int, str_profits))
        if b_namedtuple:
            Company = namedtuple(name, _lst)
            company = Company(*int_profits)
            print(f"Объём занимаемой объектом namedtuple памяти: "
                  f"{getsizeof(company)} байт(а)")
        else:
            Company = recordclass(name, _lst)
            company = Company(*int_profits)
            print(f"Объём занимаемой объектом recordclass памяти: "
                  f"{getsizeof(company)} байт(а)")
        _companies.append(company)
    return _companies


def get_average_annual_profit(lst_companies):
    result = 0
    for company in lst_companies:
        result += company.profit1 + company.profit2 \
                  + company.profit3 + company.profit4
    return result / len(lst_companies)


def show_efficiency(lst_companies, limit_value):
    lst_bad = []
    lst_good = []
    lst_average = []
    for company in lst_companies:
        company_annual_profit = company.profit1 + company.profit2 \
                                + company.profit3 + company.profit4
        if company_annual_profit < limit_value:
            lst_bad.append(str(company).split('(')[0])
        elif company_annual_profit > limit_value:
            lst_good.append(str(company).split('(')[0])
        else:
            lst_average.append(str(company).split('(')[0])

    if lst_good:
        print(f"Предприятия, с прибылью выше среднего значения: "
              f"{''.join(lst_good)}")
    if lst_bad:
        print(f"Предприятия, с прибылью ниже среднего значения: "
              f"{''.join(lst_bad)}")
    if lst_average:
        print(f"Предприятия, с прибылью равной среднему значению: "
              f"{''.join(lst_average)}")


def use_namedtuple():
    companies = enter_information()
    average_annual_profit = get_average_annual_profit(companies)
    print(f"Средняя годовая прибыль всех предприятий: {average_annual_profit}")
    show_efficiency(companies, average_annual_profit)


def use_recordclass():
    companies = enter_information(b_namedtuple=False)
    average_annual_profit = get_average_annual_profit(companies)
    print(f"Средняя годовая прибыль всех предприятий: {average_annual_profit}")
    show_efficiency(companies, average_annual_profit)


def main():
    use_namedtuple()  # вызвать решение на основе namedtuple
    use_recordclass()  # вызвать решение на основе recordclass


if __name__ == "__main__":
    main()
