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
import re
import statistics


def base_questions() -> tuple:
    company_name = input("Введите название предприятия\n").title()
    company_profit = re.findall(r"\d+", input("Прибыль предприятия \33[32m%s\33[0m за каждый квартал "
                                              "(через пробел, всего 4 квартала) \n" % company_name))
    return company_name, company_profit


def company_stat(storage) -> str:
    if storage:
        average = statistics.mean((x.profit for x in storage))
        top_companies = ",".join([x.name for x in filter(lambda x: x.profit >= average, storage)])
        floor_companies = ",".join([x.name for x in filter(lambda x: x.profit < average, storage)])

        return "Средняя годовая прибыль всех предприятий:\33[34m %.2f \33[0m \nПредприятия, с прибылью выше среднего " \
               "значения:\33[32m %s \33[0m \nПредприятия, с прибылью ниже среднего значения:\33[31m %s \33[0m\n" % (
                   average, top_companies, floor_companies)


""" Вариант 1 namedtuple """
def fill_namedTuple(num: int) -> list:
    COMPANY = collections.namedtuple("company", "name profit q1 q2 q3 q4", defaults=["unknown", 0, 0, 0, 0, 0])
    lst = []
    for _ in range(0, num):
        company_name, company_profit = base_questions()
        try:
            lst.append(COMPANY(company_name, sum(map(float, company_profit)), *map(float, company_profit)))
        except TypeError:
            print("\33[31m Прибыль предприятия через пробел, всего 4 квартала\33[0m ")
            continue
    return lst


if __name__ == "__main__":
    number = int(input("Введите количество предприятий для расчета прибыли\n"))
    storage = fill_namedTuple(number)
    print(company_stat(storage))
