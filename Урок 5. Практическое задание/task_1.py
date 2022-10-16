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

from collections import OrderedDict

order_dct = OrderedDict()
# ввод данных
# for j in range(2):
#     name = input('Введите название предприятия: ')
#     values = input('Через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ')
#     lst = list(map(int, values.split(" ")))
#     order_dct[name] = lst

order_dct['Рога'] = [235, 345634, 55, 235]
order_dct['Копыта'] = [345, 34, 543, 34]

average_p = sum(map(sum, order_dct.values())) / len(order_dct)
print(f'Средняя годовая прибыль всех предприятий: {average_p}')
comps = [x for x in order_dct.keys() if (sum(order_dct[x])>average_p)]  # не сообразил как сделать
print('Больше ', comps)
for j in order_dct.items():
    if sum(j[1])> average_p:
        print(f'Предприятия, с прибылью выше среднего значения: {j[0]}')
    elif sum(j[1])<average_p:
        print(f'Предприятия, с прибылью ниже среднего значения: {j[0]}')


