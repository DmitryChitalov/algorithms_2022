"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

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


import collections


# вариант 1
def add_firms(firms_count):
    """
    Функция создает на основе коллекции defaultdict словарь
    с введенными пользователем названием фирмы и ее прибыли по кварталам.
    Количество фирм передается в аргументе функции.
    """
    d = collections.defaultdict(int)
    while firms_count != 0:
        firms_info = [(input('Введите название фирмы: '),
                       (input('Введите прибыль фирмы за каждый квартал через пробел: ').split()))]
        for key, val in firms_info:
            val = sum([int(el) for el in val])
            d[key] = val
        firms_count -= 1
    return d


def count_firm_prof():
    """
    Функция запускает другую функцию - add_firms
    для получения данных о данных по фирмам,
    затем рассчитыват среднюю прибыль за год по всем фирмам
    и выводит списки фирм с прибылью больше и меньше среднегодовой.
    """
    f_count = int(input('Введите количество фирм для расчета прибыли: '))
    f_info = add_firms(f_count)
    average_prof = float(sum(f_info.values()) / f_count)
    return f'Средняя годовая прибыль всех предприятий: {average_prof}\n' \
           f'Предприятия, с прибылью выше среднего значения: {[k for k, v in f_info.items() if v > average_prof]}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {[k for k, v in f_info.items() if v < average_prof]}'


if __name__ == '__main__':
    print(count_firm_prof())


# вариант 2
class FirmInfo:
    firm_count = int(input('Введите число фирм: '))

    def __init__(self):
        self.info = collections.ChainMap()

    def get_info(self):
        while self.firm_count != 0:
            name = input('Введите назнание фирмы: ')
            prof_list = input('Введите прибыль за каждый квартал через пробел: ').split()
            prof = sum([int(el) for el in prof_list])
            self.info[name] = prof
            self.firm_count -= 1
        return self.info

    @staticmethod
    def count_aver():
        info = FirmInfo.get_info(FirmInfo())
        aver = float(sum(info.values()) / FirmInfo.firm_count)
        above_aver = [k for k, v in info.items() if v > aver]
        below_aver = [k for k, v in info.items() if v < aver]
        return f'Среднегодовая прибыль по всем фирмам: {aver}\n' \
               f'Предприятия с прибылью выше среднегодовой: {above_aver}\n' \
               f'Предприятия с прибылью ниже среднегодовой: {below_aver}'


if __name__ == '__main__':
    firms_prof = FirmInfo()
    print(firms_prof.count_aver())
