# i
def check_1(lst_obj):

    lst_to_set = set(lst_obj)  # n()
    return lst_to_set  # n()

def check_2(lst_obj):

    for j in range(len(lst_obj)):          # O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # O(1+n)
            return False                   # O(1)
    return True                            # O(1)

def check_3(lst_obj):

    lst_copy = list(lst_obj)                 # O(len(lst_obj))
    lst_copy.sort()                          # O(n log n)
    for i in range(len(lst_obj) - 1):        # O(n)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)

for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))


# ii


"""
Задание 2.
Реализуйте два алгоритма.
Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.
Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.
Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Постарайтесь не использовать ф-ции min() и sort() и другие ф-ции!
Подход должен быть максимально алгоритмическим.
"""


# сложность O(n)
def get_min_number(lst):
    min_number = lst[0]                                     # O(1)
    for i in lst:                                           # O(n)
        if i < min_number:                                  # O(len(i)
            min_number = i                                  # O(1)
    return min_number                                       # O(1)


# Сложность O(n**2)
def get_min_number_2(lst):
    min_number_2 = lst[0]                                   # O(1)
    for i in lst:                                           # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_number_2 > lst[j]:                       # O(len(lst[j])
                min_number_2 = lst[j]                       # O(1)
    return min_number_2                                     # O(1)


first_list = [100, 50, 3, 4, 23, 10]

print(get_min_number(first_list))

print(get_min_number_2(first_list))

# iii

"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


company = {'Tander': 50000, 'Rosprom': 45000, 'Gazprom': 27000, 'Lenta': 55600, 'Ashan': 39000}
print(len(company))

# Первый способ:
# сложность O(n log n)


def by_value(item):
    return item[1]                                                          # O(1)


max_profit = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(company.items(), key=by_value, reverse=True):     # O(n + n log n)
    if i < 3:                                                               # O(len(i)
        max_profit.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)
print(max_profit)                                                           # O(1)


# Второй способ:
# Сложность O (n**2)

global max_value                                                            # O(1)
global key_max_value                                                        # O(1)

max_profit_2 = {}                                                           # O(1)
while len(max_profit_2) < 3:                                                # O(n)
    max_value = 0                                                           # O(1)
    for key, value in company.items():                               # O(n)
        if max_value < value:                                               # O(len(max_value))
            max_value = value                                               # O(1)
            key_max_value = key                                             # O(1)
    max_value = company.pop(key_max_value)                           # O(1)
    max_profit_2.setdefault(key_max_value, max_value)                       # O(1)

print(max_profit_2)

# Вывод: Первый способ выполняется быстрее так как самым "тяжелым" алгоритмом,
# является функция SORT() = O (n log n)
