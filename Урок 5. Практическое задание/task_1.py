"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить                       среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль                    выше среднего и отдельно
вывести наименования предприятий,                                 чья прибыль ниже среднего

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
from collections import Counter
from collections import namedtuple

def getData():
    n = int(input("Number of enterprises: "))
    Enterprise = namedtuple('Ntrprise',['i1','i2','i3','i4'])
    d = {}
    for i in range(n):
        name = input("Name ")
        while name in d.keys():
            name = input("Already exists, try another: ")
        f = int(input("income from 1st quartal "))
        s = int(input("income from 2nd quartal "))
        t = int(input("income from 3rd quartal "))
        fr = int(input("income from 4th quartal "))

        d[name] = Enterprise(f,s,t,fr)
    return d

def getAnnual(d: dict) -> Counter:
    res = Counter()
    for k in d.keys():
        res[k] = d[k][0] + d[k][1] + d[k][2] + d[k][3] #используется перебор по индексам для совместимости с обычными
        # кортежами
    return res


def getMTA_LTA(d: dict, avg: float) -> tuple:
    more = []
    less = []
    for k in d.keys():
        if d[k] > avg:
            more.append(k)
        elif d[k] == avg:
            pass
        else:
            less.append(k)
    return more,less



if __name__ == "__main__":
    enterprises = getData()
    print(enterprises)
    annual_income = getAnnual(enterprises)
    print(annual_income)
    avg = sum(annual_income.values())/len(annual_income)
    print(avg)
    more,less = getMTA_LTA(annual_income,avg)
    print(f"More than average: {more}")
    print(f"Less than average: {less}")