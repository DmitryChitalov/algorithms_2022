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
from collections import defaultdict, Counter

"""
Вариант без модуля collections и безз ввода данных
"""


def get_avg(obj_dict):
    total = 0
    total_sum = {}
    n = len(obj_dict)
    more_avg = []
    less_avg = []
    for k, v in obj_dict.items():
        total_sum[k] = sum(v)
        total += sum(v)
    for k, v in total_sum.items():
        if v > total/n:
            more_avg.append(k)
        else:
            less_avg.append(k)

    return f'Средняя годовая прибыль всех предприятий: {round(total/n, 2)}, \n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(str(x) for x in more_avg)} \n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(str(x) for x in less_avg)}'


obj_dict = {'рога': [345, 34, 543, 34], 'копыта': [
    235, 345634, 55, 235], 'хвост': [123, 321, 4567, 89076]}

print(get_avg(obj_dict))


"""
Второй вариант с использованием defaultdict, Counter
"""


def get_sum_values(values):
    sum_values = 0
    for value in values:
        sum_values += int(value)
    return sum_values


def get_avg_2(obj_dict_2):
    total_sum = sum(Counter(obj_dict_2).values())
    total_avg = total_sum/len(obj_dict_2)
    more_avg = [i for i in obj_dict_2 if obj_dict_2.get(i) > total_avg]
    less_avg = [i for i in obj_dict_2 if obj_dict_2.get(i) < total_avg]
    return f'Средняя годовая прибыль всех предприятий: {total_avg}, \n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(str(x) for x in more_avg)} \n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(str(x) for x in less_avg)}'


def main():
    obj_dict_2 = defaultdict(int)
    qty = int(input('Введите количество предприятий для расчета прибыли: '))
    for _ in range(qty):
        name = input('Введите название предприятия: ')
        values = input(
            'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        total = get_sum_values(values)
        obj_dict_2[name] = total
    return get_avg_2(obj_dict_2)


print(main())
