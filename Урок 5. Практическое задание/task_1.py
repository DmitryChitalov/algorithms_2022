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

class Company:

    def __init__(self):
        self.firms = {}
        self.quantity_firms = len(self.firms)

    def create_firms(self, n):
        for i in range(n):
            name_firm = input('Введите название предприятия: ')
            profit_firm = input('Через пробел введите прибыль данного предприятия '
                                'за каждый квартал(Всего 4 квартала): ')
            profit_firm = profit_firm.split(' ')
            FIRMS = namedtuple(f'{name_firm}', 'first_quarter, second_quarter, third_quarter, fourth_quarter')
            FIRM = FIRMS(first_quarter=int(profit_firm[0]), second_quarter=int(profit_firm[1]),
                         third_quarter=int(profit_firm[2]), fourth_quarter=int(profit_firm[3]))
            self.firms.setdefault(i+1, FIRM)

    def mid_profit_all(self, mid_all = 0):
        for i in range(len(self.firms)):
            mid_all = mid_all + self.mid_profit_one(i)
        mid_all = mid_all / len(self.firms)
        return mid_all

    def mid_profit_one(self, i = 0):
        comp = self.firms.get(i + 1)
        summ_num = comp[0] + comp[1] + comp[2] + comp[3]
        md_prof = summ_num / 4
        return md_prof


    def below_average(self, name_comp = ''):
        for i in range(len(self.firms)):
            if self.mid_profit_one(i) < self.mid_profit_all():
                name_comp = name_comp + type(self.firms.get(i+1)).__name__ + ' '
        return f'Предприятия, с прибылью ниже среднего значения: {name_comp}'

    def above_average(self, name_comp = ''):
        for i in range(len(self.firms)):
            if self.mid_profit_one(i) > self.mid_profit_all():
                name_comp = name_comp + type(self.firms.get(i+1)).__name__ + ' '
        return f'Предприятия, с прибылью выше среднего значения: {name_comp}'


n = int(input('Введите количество предприятий для расчета прибыли: '))
m = Company()
m.create_firms(n)
print(m.firms)
print(len(m.firms))
print(f'Средняя годовая прибыль всех предприятий: {m.mid_profit_all()}')
print(m.above_average())
print(m.below_average())