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

Это файл для первого скрипта
"""


from collections import namedtuple
from memory_profiler import memory_usage
from random import randint

def memory_decor(func):
    def wrapper():
        m1 = memory_usage()
        func()
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper

def get_mean(array):
    return sum(array) / len(array)

'''
Скрипт из урока 5 задания 1. Я только немного поменяла, а именно:
- запихнула все в функцию
- чтобы память заполонялась, заменила ввод пользователем нужных данных на генерацию 10000 компаний
'''

@memory_decor
def analyze_companies():
    COMP = namedtuple('Company', 'name yearly_profit')
    companies = []

    number_of_comps = 10000
    while number_of_comps > 0:
        comp_name = str(number_of_comps)
        quarters = [randint(100, 1000) for i in range(4)]
        curr_comp = COMP(
            name=comp_name,
            yearly_profit=sum(quarters)
            )
        companies.append(curr_comp)
        number_of_comps -= 1

    average_yearly_profit = get_mean([comp.yearly_profit for comp in companies])

    companies_with_low_profit = []
    companies_with_high_profit = []

    for comp in companies:
        if comp.yearly_profit < average_yearly_profit:
            companies_with_low_profit.append(comp.name)
        elif comp.yearly_profit > average_yearly_profit:
            companies_with_high_profit.append(comp.name)

    print('Средняя годовая прибыль всех предприятий: ' + str(average_yearly_profit))
    print('Предприятия, с прибылью выше среднего значения: ' + ', '.join(companies_with_high_profit))
    print('Предприятия, с прибылью ниже среднего значения: ' + ', '.join(companies_with_low_profit))
    return

'''
В оптимизированной версии следующие изменения:
1. заменила namedtuple на recordclass
2. информацию о кварталах держу в котреже, а не списке
3. заменила вывод обычных строк на вывод f-строк
'''

@memory_decor
def analyze_companies_2():
    # Изменение 1
    COMP = recordclass('Company', 'name yearly_profit')
    companies = []

    number_of_comps = 10000
    while number_of_comps > 0:
        comp_name = str(number_of_comps)
        # Изменение 2
        quarters = tuple([randint(100, 1000) for i in range(4)])
        curr_comp = COMP(
            name=comp_name,
            yearly_profit=sum(quarters)
            )
        companies.append(curr_comp)
        number_of_comps -= 1

    average_yearly_profit = get_mean([comp.yearly_profit for comp in companies])

    companies_with_low_profit = []
    companies_with_high_profit = []

    for comp in companies:
        if comp.yearly_profit < average_yearly_profit:
            companies_with_low_profit.append(comp.name)
        elif comp.yearly_profit > average_yearly_profit:
            companies_with_high_profit.append(comp.name)

    # Изменение 3
    print(f'Средняя годовая прибыль всех предприятий: {average_yearly_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(companies_with_high_profit)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(companies_with_low_profit)}')
    return

print(analyze_companies())
print(analyze_companies_2())

'''
Мои результаты:

analyze_companies()     - 0.58203125
analyze_companies_2()   - 0.43359375

Оптимизированная версия занимает меньше памяти
'''
