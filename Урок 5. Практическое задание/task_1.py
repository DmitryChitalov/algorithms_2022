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
import re
from collections import Counter


class MyApp:
    """ "Приложение" """

    def __init__(self):
        self.count = 0
        self.total_of_total = 0.0
        self.last_name = ''
        self.counter = Counter()
        self.request_count()

    def request_count(self):
        """ Запрос количества предприятий """
        count = input('Введите количество предприятий для расчета прибыли: ').strip()
        try:
            self.count = int(count)
            self.request_company()
        except ValueError:
            print('Введено неверное значение, попробуйте еще раз')
            self.request_count()

    def request_company(self):
        """ Запросить название предприятия """
        name = input('Введите название предприятия: ').strip()
        if name == '':
            print('Введено неверное значение, попробуйте еще раз')
            self.request_company()
        self.counter[name] = 0
        self.last_name = name
        self.request_income()
        if len(self.counter) < self.count:
            self.request_company()
        else:
            self.finish()

    def calc_income(self, income) -> float:
        """ Посчитать тотальный инком """
        total = 0.0
        if len(income) != 4:
            return
        try:
            for x in income:
                total += float(x)
        except ValueError:
            return
        self.total_of_total += total
        return total

    def get_avg(self) -> float:
        """ Получить среднее значение """
        avg = float(self.total_of_total / float(self.count))
        return avg

    def split_avg(self):
        """ Получить выше среднего и ниже """
        avg = self.get_avg()
        # result = [
        #     filter(lambda v: v[1] > avg, self.counter.items()),
        #     filter(lambda v: v[1] < avg, self.counter.items())
        # ]
        result = [[],[]]
        for k, v in self.counter.items():
            kk = 0 if v >= avg else 1
            result[kk].append(k)
        return result

    def request_income(self):
        """ Запросить доход по 4 квартала """
        income = input('через пробел введите прибыль данного '
                       'предприятия за каждый квартал(Всего 4 квартала): ').strip()
        values = re.sub(r"\s+", ' ', income).split(' ')
        calc = self.calc_income(values)
        if calc is None:
            print('Введено неверное значение, вводите через пробел, 4 числовых значения')
            self.request_income()
        self.counter[self.last_name] = calc

    def finish(self):
        """ Финиш """
        print("Средняя годовая прибыль всех предприятий: %f" % (self.get_avg()))
        r = self.split_avg()
        print(f"Предприятия, с прибылью выше среднего значения: {' '.join(r[0])}")
        print(f"Предприятия, с прибылью ниже среднего значения: {' '.join(r[1])}")

app = MyApp()
