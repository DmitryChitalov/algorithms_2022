"""
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
from collections import defaultdict


def av_income():
    entered_list = input(
        "Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ").split()
    sum_num_list = sum(list(map(int, entered_list)))
    return sum_num_list


def firm_income():
    n = counter
    while n > 0:
        firm_name = input("Фирма - ")
        firm_t = namedtuple('firms', 'firm_name income')
        firms = firm_t(
            firm_name=firm_name,
            income=av_income()
        )
        n -= 1
        print(f'{firm_name}-{firms.income}')
        my_dict[firms.firm_name] = firms.income
    return f''

def main():
    firm_income()
    av_sum = sum(my_dict.values()) / counter
    more_av = []
    less_av = []
    for k, v in my_dict.items():
        if v > av_sum:
            more_av.append(k)
        else:
            less_av.append(k)

    return f'Предприятия,с прибылью выше среднего значения {" ".join(more_av)}, меньше {" ".join(less_av)}'


counter = int(input("Количество фирм "))
my_dict = defaultdict(int)
print(main())
