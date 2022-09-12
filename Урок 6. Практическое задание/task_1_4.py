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

Это файл для четвертого скрипта
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple
from recordclass import recordclass
from memory_profiler import profile


def filling_data():
    structure = namedtuple('Enterprise', 'name values')
    enterprises_list = list()
    try:
        for _ in range(int(input('Введите количество организаций: '))):
            name = input('Введите название организации: ')
            while True:
                four_quarters_income = input(
                    'Через пробел введите прибыль каждого предприятия (всего 4 квартала): ').split(' ')
                if len(four_quarters_income) == 4:
                    four_quarters_income = list(map(float, four_quarters_income))
                    break
                else:
                    print('Вы ввели не 4 значения, попробуйте ещё раз!')
            enterprises_list.append(structure(name, four_quarters_income))
        return enterprises_list
    except ValueError:
        print('Вы ввели не число, попробуйте ещё раз!')


def filling_data_record():
    structure = recordclass('Enterprise', 'name values')
    enterprises_list = list()
    try:
        for _ in range(int(input('Введите количество организаций: '))):
            name = input('Введите название организации: ')
            while True:
                four_quarters_income = input(
                    'Через пробел введите прибыль каждого предприятия (всего 4 квартала): ').split(' ')
                if len(four_quarters_income) == 4:
                    four_quarters_income = list(map(float, four_quarters_income))
                    break
                else:
                    print('Вы ввели не 4 значения, попробуйте ещё раз!')
            enterprises_list.append(structure(name, four_quarters_income))
        return enterprises_list
    except ValueError:
        print('Вы ввели не число, попробуйте ещё раз!')


def calculation_average_total_income(ent_lst):
    val_lst = [sum(el.values) for el in ent_lst]
    return sum(val_lst) / len(val_lst)


def div_enterprises_by_av_income(ent_lst, avg_income):
    smaller_income_lst = list()
    bigger_income_lst = list()
    for el in ent_lst:
        if sum(el.values) < avg_income:
            smaller_income_lst.append(el.name)
        else:
            bigger_income_lst.append(el.name)
    return smaller_income_lst, bigger_income_lst


def printing_result(average_inc, smaller_income_list, bigger_income_list):
    print(f'Средняя годовая прибыль всех предприятий: {average_inc}')
    if not smaller_income_list:
        print(f'Оборот всех компаний равен')
    else:
        print(f'Название компаний с оборотом выше среднего значения: {" ".join(bigger_income_list)}')
        print(f'Название компаний с оборотом ниже среднего значения: {" ".join(smaller_income_list)}')


@profile
def main():
    enterprises_lst = filling_data()
    average_income = calculation_average_total_income(enterprises_lst)
    smaller_inc_lst, bigger_inc_lst = div_enterprises_by_av_income(enterprises_lst, average_income)
    printing_result(average_income, smaller_inc_lst, bigger_inc_lst)


@profile
def main_with_record():
    enterprises_lst = filling_data_record()
    average_income = calculation_average_total_income(enterprises_lst)
    smaller_inc_lst, bigger_inc_lst = div_enterprises_by_av_income(enterprises_lst, average_income)
    printing_result(average_income, smaller_inc_lst, bigger_inc_lst)


if __name__ == '__main__':
    main()
    main_with_record()

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   127     20.2 MiB     20.2 MiB           1   @profile
   128                                         def main():
   129     20.2 MiB      0.1 MiB           1       enterprises_lst = filling_data()
   130     20.3 MiB      0.0 MiB           1       average_income = calculation_average_total_income(enterprises_lst)
   131     20.3 MiB      0.0 MiB           1       smaller_inc_lst, bigger_inc_lst = div_enterprises_by_av_income(
   132     20.3 MiB      0.0 MiB           1       printing_result(average_income, smaller_inc_lst, bigger_inc_lst)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   135     20.2 MiB     20.2 MiB           1   @profile
   136                                         def main_with_record():
   137     20.2 MiB      0.0 MiB           1       enterprises_lst = filling_data_record()
   138     20.2 MiB      0.0 MiB           1       average_income = calculation_average_total_income(enterprises_lst)
   139     20.2 MiB      0.0 MiB           1       smaller_inc_lst, bigger_inc_lst = div_enterprises_by_av_income(
   140     20.2 MiB      0.0 MiB           1       printing_result(average_income, smaller_inc_lst, bigger_inc_lst)
   
   Заменили namedTuple на recordclass, за счет чего смогли выиграть немного по памяти.
'''