"""
Задание 1.

Для каждой из трех функций выполнить следующее:

1) для каждого выражения вместо символов !!! укажите сложность.
2) определите сложность алгоритма в целом (Сложность: !!!).

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- Сложность нужно указать только там, где есть !!!
-- Сложности встроенных функций и операций нужно искать
    в таблицах (см. материалы к уроку).
"""

from random import sample


##############################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 1:
    Создать множество из списка

    Сложность: O(N) - Линейная.
    """
    lst_to_set = set(lst_obj)  # O(N) Линейная
    return lst_to_set  # O(1) Константная


##############################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: O(N^2).
    """
    for j in range(len(lst_obj)):          # O(N)
        if lst_obj[j] in lst_obj[j+1:]:    # O(N) + O(N) = O(N)
            return False                   # O(1)
    return True                            # O(1)


##############################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: O(Nlog N)
    """
    lst_copy = list(lst_obj)                 # O(N)
    lst_copy.sort()                          # O(Nlog N)
    for i in range(len(lst_obj) - 1):        # O(N)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
