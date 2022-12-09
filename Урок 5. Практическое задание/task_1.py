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


def income_calculation():
    print('Введите количество компаний: ', end='')
    count = int(input())
    companies = dict()
    total_avg = 0
    for i in range(1, count + 1):
        print(f'Пожалуйста, введите название {i}-го предприятия: ', end='')
        name = input()
        print(f'Пожалуйста, введите (через пробел) поквартальную прибыль предприятия {name}: ', end='')
        qrt_income = input().split(' ')
        avg_income = 0
        info = namedtuple('info', 'name qrt_income avg_income')
        try:
            avg_income = sum([avg_income + int(val)/len(qrt_income) for val in qrt_income])
        except ValueError:
            print('Будьте внимательней при вводе поквартальной прибыли. Попробуйте еще раз.')
            income_calculation()
        total_avg = total_avg + avg_income / count
        companies[i] = info(name=name,
                            qrt_income=qrt_income,
                            avg_income=avg_income)
    print(f'Средняя годовая прибыль предприятий составила {total_avg:.1f}')
    is_less = ''
    is_more = ''
    for i in companies.keys():
        if companies[i].avg_income < total_avg:
            if is_less == '':
                is_less = companies[i].name
            else:
                is_less = is_less + ', ' + companies[i].name
        else:
            if is_more == '':
                is_more = companies[i].name
            else:
                is_more = is_more + ', ' + companies[i].name
    if is_more:
        print(f'Предприятия, с прибылью выше среднего значения: {is_more}')
    if is_less:
        print(f'Предприятия, с прибылью ниже среднего значения: {is_less}')


if __name__ == '__main__':
    income_calculation()


