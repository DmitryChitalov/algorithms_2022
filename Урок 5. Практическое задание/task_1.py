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


from collections import defaultdict


def number_of_firms():
    n = input('Введите количество предприятий для расчета прибыли: ')
    if n.isdigit():
        return int(n)
    else:
        print('Количество предприятий должно быть цифрой. Попробуйте снова.')
        number_of_firms()


def revenue_input():
    n = input(f'Через пробел введите прибыль данного '
              f'предприятия за каждый квартал'
              f'(Всего 4 квартала):').split()

    check = 0
    for i, el in enumerate(n):
        if el.isdigit():
            check += 1
            n[i] = int(n[i])
    if check == 4:
        return n
    else:
        print('Прибыль следует указать в цифрах через пробел. '
              'Должно быть 4 квартала. Попробуйте снова.')
        revenue_input()


def find_average(l: list):
    return sum(l) / len(l)


def show_upper_ave(comp, ave_sum):
    res = {}
    for k, v in comp.items():
        if find_average(v) > ave_sum:
            res[k] = find_average(v)
    return res


def show_lower_ave(comp, ave_sum):
    res = {}
    for k, v in comp.items():
        if find_average(v) < ave_sum:
            res[k] = find_average(v)
    return res


if __name__ == '__main__':
    companies = defaultdict(list)
    average_rev = 0

    for i in range(0, number_of_firms()):
        c = input(f'Введите название {i + 1}-й компании: ')
        companies[c] = revenue_input()
        average_rev += find_average(companies[c])

    average_rev = average_rev / len(companies)

    print('-' * 100)
    print(f'Средняя прибыль предприятий: {average_rev}')
    print(f'Предприятия с прибылью выше среднего значения: '
          f'{show_upper_ave(companies, average_rev)}')
    print(f'Предприятия с прибылью ниже среднего значения: '
          f'{show_lower_ave(companies, average_rev)}')