"""
Комментарий после проверки:
O(2^N)
у текущей рекурсии другая сложность
см. урок 1, 2
"""

# создадим словарь: ключ - название компании, значение - годовая прибыль
from random import randint, choice

names = []
dict_companies = {}
for i in range(1, 10):
    names.append('Company_' + str(i))
for name in names:
    dict_companies[name] = randint(10000, 10000000)
print(dict_companies)


# рекурсия, сложность линейная
def three_max_1(**dict_comp):  # O(N)
    """
    :param dict_comp: dict
        словарь из ключей - названий компаний со значениями - годовой прибыли
    :return: tuple(название компании, прибыль)
        кортеж из названия компании и прибыли
    """
    if len(dict_companies) - len(dict_comp) < 3:  # O(N)
        # берём кортежи из названия и прибыли и ищеем максимум по прибыли
        max_val = max(dict_comp.items(), key=lambda x: x[1])  # O(N)
        del dict_comp[max_val[0]]  # O(1)
        print(max_val)  # O(1)
        return three_max_1(**dict_comp)  # O(N)


three_max_1(**dict_companies)
