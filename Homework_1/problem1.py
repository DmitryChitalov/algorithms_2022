import random


##############################################################################
def check_1(lst_obj):
    """
    Сложность: O(len(lst)).
    """
    lst_to_set = set(lst_obj)  # O(len(lst)) зависит от длины аргумента
    return lst_to_set  # O(1)


##############################################################################
def check_2(lst_obj):
    """
    Сложность: O(n^2).
    """
    for j in range(len(lst_obj)):          # O(n)
        if lst_obj[j] in lst_obj[j+1:]:    # O(n)
            return False                   # O(1)
    return True                            # O(1)


##############################################################################
def check_3(lst_obj):
    """
    Сложность: O(nlog(n))
    """
    lst_copy = list(lst_obj)                            # O(len(lst)) зависит от длины аргумента
    lst_copy.sort()                                     # O(nlog(n))
    for i in range(len(lst_obj) - 1):                   # O(n)
        if lst_copy[i] == lst_copy[i+1]:                # O(1)
            return False                                # O(1)
    return True                                         # O(1)


for j in (50, 500, 1000, 5000, 10000):                  # O(1)
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)      # O(n)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))