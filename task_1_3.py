"""
Курс: Алгоритмы и структуры данных на Python. Базовый курс
Урок: 5
Задание: 1
-----------------------------------------------------------------------------
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько вариантов решения этого задания,
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

from collections import Counter
from memory_profiler import memory_usage
from sys import getsizeof
from pympler.asizeof import asizeof

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


##############################################################################
"""
ИСХОДНОЕ РЕШЕНИЕ

Последовательность ввода значений:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: a
Через пробел введите прибыль данного предприятия: 1 2 3 4
Введите название предприятия: b
Через пробел введите прибыль данного предприятия: 1 2 3 5

Размер хранилища: 248 байт(а) <-- с помощью getsizeof
Размер хранилища: 432 байт(а) <-- с помощью asizeof
Используемая память: 0.03515625 Mib
"""

@decor
def origin():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
        cnt_profit = Counter()
        for i in range(n):
            name = input('Введите название предприятия: ')
            profit = sum([float(x) for x in input('Через пробел введите прибыль данного предприятия: ').split()])
            cnt_profit[name] = profit
        print('----------------------------------')
        print(f'Размер хранилища: {getsizeof(cnt_profit)} байт(а)')
        print(f'Размер хранилища: {asizeof(cnt_profit)} байт(а)')
        print('----------------------------------')
    except ValueError:
        print('Введите корректные данные!')
    else:
        cnt_profit['all_avg'] = sum(cnt_profit.values()) / len(cnt_profit)
        print(f'Средняя годовая прибыль всех предприятий: {cnt_profit["all_avg"]:.2f}')
        avg_idx = cnt_profit.most_common().index(('all_avg', cnt_profit['all_avg']))
        print('Предприятия, с прибылью выше среднего значения:', *dict(cnt_profit.most_common()[:avg_idx]).keys())
        print('Предприятия, с прибылью ниже среднего значения:', *dict(cnt_profit.most_common()[avg_idx+1:]).keys())


print('---> ИСХОДНОЕ РЕШЕНИЕ')
res, mem_diff = origin()
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')


##############################################################################
"""
ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ

Описание:
1) убрал списковое включение внутри sum, чтобы не создавался бессмысленный список
2) убрал лишние переменные для работы с вводимыми значениями
3) заменил словарь Counetr на список из кортежей

Последовательность ввода значений:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: a
Через пробел введите прибыль данного предприятия: 1 2 3 4
Введите название предприятия: b
Через пробел введите прибыль данного предприятия: 1 2 3 5

Размер хранилища: 248 байт(а) <-- с помощью getsizeof
Размер хранилища: 408 байт(а) <-- с помощью asizeof
Используемая память: 0.0 Mib
"""

@decor
def optimize():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
        lst_profit = []  # определяем пустой список вместо словаря
        for i in range(n):
            # убрал списковое включение внутри sum, чтобы не создавался бессмысленный список
            # теперь данная конструкция работает как генератор
            # дополнительно исключил лишние переменные name и profit
            lst_profit.append((
                input('Введите название предприятия: '),
                sum(float(x) for x in input('Через пробел введите прибыль данного предприятия: ').split())
            ))
        print('----------------------------------')
        print(f'Размер хранилища: {getsizeof(lst_profit)} байт(а)')
        print(f'Размер хранилища: {asizeof(lst_profit)} байт(а)')
        print('----------------------------------')
    except ValueError:
        print('Введите корректные данные!')
    else:
        avg_profit = sum(x[1] for x in lst_profit) / len(lst_profit)
        print(f'Средняя годовая прибыль всех предприятий: {avg_profit:.2f}')
        print('Предприятия, с прибылью выше среднего значения:', end='')
        print(*list(filter(lambda x: x[1] > avg_profit, avg_profit)))  # использовал filter вместо среза
        print('Предприятия, с прибылью ниже среднего значения:', end='')
        print(*list(filter(lambda x: x[1] > avg_profit, avg_profit)))  # использовал filter вместо среза


print('---> ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ')
res, mem_diff = origin()
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')