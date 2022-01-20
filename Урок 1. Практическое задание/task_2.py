"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
from copy import deepcopy
from random import randint, shuffle, randrange

my_arr = list(range(randint(-20,-10), randint(0, 20)))
shuffle(my_arr)

def get_min_from_array_heavy(arr: list) -> int:
    """
    Сложность O(n^2)
    """
    print(f"Array :{arr}")
    num = 0                         # O(1)
    copy_arr = deepcopy(arr)        # O(n)
    counter = 0                     # O(1)
    while len(copy_arr) > 1:        # O(n)
        if copy_arr[counter] > num: # O(1)
            del copy_arr[counter]   # O(n)
            counter = 0             # O(1)
            continue                # O(1)
        else:                       # O(1)
            num = copy_arr[counter] # O(1)
        counter += 1                # O(1)
    return num                      # O(1)



def get_min_from_array_light(arr: list) -> int:
    """
    Сложность O(n)
    """
    print(f"Array :{arr}")
    num = 0
    for el in arr:          # O(n)
        if el < num:        # O(1)
            num = el        # O(1)
    return num              # O(1)


print(get_min_from_array_heavy(my_arr))

print(get_min_from_array_light(my_arr))