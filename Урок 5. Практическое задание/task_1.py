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
from collections import OrderedDict

amaunt = int(input('введите кол-во предприятий '))
enterprise = namedtuple('enterprise', ['Name', 'q1', 'q2', 'q3', 'q4'])
full_dict = OrderedDict()
middle = 0


def one_enterprise():
    name = input('введите название предприятия ')
    p_li = []
    for i in range(4):
        pr = input(f'введите прибыль за {i+1} квартал ')
        p_li.append(float(pr))
    ent = enterprise(name, q1=p_li[0], q2=p_li[1], q3=p_li[2], q4=p_li[3])
    full_dict[name] = ent


def calculate_middle_profit():
    for _ in range(amaunt):
        one_enterprise()
    sum_one = []
    for k, v in full_dict.items():
        sum_one.append(v.q1+v.q2+v.q3+v.q4)
    global middle
    middle = sum(sum_one)/len(sum_one)
    print(f'Средняя годовая прибыль всех предприятий: {middle}')


def main_downstream_or_upstream():
    calculate_middle_profit()
    up = 'Cумма прибыли больше среднего у: '
    down = 'Cумма прибыли меньше среднего у: '
    global middle
    for k, v in full_dict.items():
        sum_one = v.q1+v.q2+v.q3+v.q4
        if sum_one > middle:
            up += k + ' '
        else:
            down += k + ' '
    print(up)
    print(down)


main_downstream_or_upstream()
