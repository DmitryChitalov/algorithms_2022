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

# Курс "Алгоритмы и структуры данных на Python."
# Задание к уроку 5:
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.
# Подсказка:
# Для решения задачи обязательно примените коллекцию из модуля collections

# Примечание:
# Для уменьшения размера кода:
# были убраны лишние проверки, не влияющие на оптимизацию;
# чтобы избежать лишнего дублирования, ввод данных выполняется 1 раз.

from sys import getsizeof
from collections import namedtuple
from recordclass import recordclass


def size_set_obj(set_obj):
    size_all_obj = 0
    for obj in set_obj:
        size_all_obj += getsizeof(obj)
    return size_all_obj


companies_number = int(input('Введите количество предприятий для расчета прибыли: '))
Company_namedtuple = namedtuple('Company_namedtuple', ['company_name', 'annual_profit'])
Company_recordclass = recordclass('Company_recordclass', ['company_name', 'annual_profit'])
companies_namedtuple_list = []
companies_recordclass_list = []
sum_annual_profit = 0
_companies_number = companies_number
while _companies_number > 0:
    company_name = input('Введите название предприятия: ')
    quarterly_profit_list = input('Через пробел введите прибыль данного предприятия '
                                  'за каждый квартал (всего 4 квартала): ').split()
    annual_profit = sum([float(el) for el in quarterly_profit_list])
    sum_annual_profit += annual_profit
    company_namedtuple = Company_namedtuple(
        company_name,
        annual_profit
    )
    company_recordclass = Company_recordclass(
        company_name,
        annual_profit
    )
    companies_namedtuple_list.append(company_namedtuple)
    companies_recordclass_list.append(company_recordclass)
    _companies_number -= 1

avg_annual_profit = sum_annual_profit / companies_number
companies_above_avg_annual_profit = []
companies_below_avg_annual_profit = []

for cmp in companies_namedtuple_list:
    if cmp.annual_profit > avg_annual_profit:
        companies_above_avg_annual_profit.append(cmp.company_name)
    elif cmp.annual_profit < avg_annual_profit:
        companies_below_avg_annual_profit.append(cmp.company_name)

print(f'Средняя годовая прибыль всех предприятий: {avg_annual_profit}')
if companies_number > 1:
    print(f"Предприятия с прибылью выше среднего значения: "
          f"{', '.join(companies_above_avg_annual_profit)}")
    print(f"Предприятия с прибылью ниже среднего значения: "
          f"{', '.join(companies_below_avg_annual_profit)}")


print(f"Объём занимаемой объектами namedtuple памяти: {size_set_obj(companies_namedtuple_list)} байт(а).")
print(f"Объём занимаемой объектами recordclass памяти: {size_set_obj(companies_recordclass_list)} байт(а).")

# Для оптимизации памяти данные о компаниях хранятся в переменных типа recordclass.
# Вычисляется общий объём занимаемой памяти всеми компаниями.
# По результатам тестирования удалось добиться оптимизации памяти.
