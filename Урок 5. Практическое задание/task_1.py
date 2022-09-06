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


def filling_data():
    structure = namedtuple('Enterprise', 'name values')
    enterprises_list = list()
    try:
        for _ in range(int(input('Введите количество организаций: '))):
            name = input('Введите название организации: ')
            while True:
                four_quarters_income = input(
                    'Через пробел введите прибыль каждого предприятия (всего 4 квартала): ').split(' ')
                if len(four_quarters_income) == 4:
                    four_quarters_income = list(map(float, four_quarters_income))
                    break
                else:
                    print('Вы ввели не 4 значения, попробуйте ещё раз!')
            enterprises_list.append(structure(name, four_quarters_income))
        return enterprises_list
    except ValueError:
        print('Вы ввели не число, попробуйте ещё раз!')


def calculation_average_total_income(ent_lst):
    val_lst = [sum(el.values) for el in ent_lst]
    return sum(val_lst) / len(val_lst)


def div_enterprises_by_av_income(ent_lst, avg_income):
    smaller_income_lst = list()
    bigger_income_lst = list()
    for el in ent_lst:
        if sum(el.values) < avg_income:
            smaller_income_lst.append(el.name)
        else:
            bigger_income_lst.append(el.name)
    return smaller_income_lst, bigger_income_lst


def printing_result(average_inc, smaller_income_list, bigger_income_list):
    print(f'Средняя годовая прибыль всех предприятий: {average_inc}')
    if not smaller_income_list:
        print(f'Оборот всех компаний равен')
    else:
        print(f'Название компаний с оборотом выше среднего значения: {" ".join(bigger_income_list)}')
        print(f'Название компаний с оборотом ниже среднего значения: {" ".join(smaller_income_list)}')


def main():
    enterprises_lst = filling_data()
    average_income = calculation_average_total_income(enterprises_lst)
    smaller_inc_lst, bigger_inc_lst = div_enterprises_by_av_income(enterprises_lst, average_income)
    printing_result(average_income, smaller_inc_lst, bigger_inc_lst)


if __name__ == '__main__':
    main()
