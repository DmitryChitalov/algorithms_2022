"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""

from timeit import timeit
from collections import deque

"""Операции выполняются примерно одинакого """
just_list = [i for i in range(1, 1000)]
just_deque = deque([i for i in range(1, 1000)])


count = 300


# получения элемента списка
# receive_el_list ---- 0.007059000000000003
def receive_el_list(my_list):
    for i in range(1, count, 3):
        a = my_list[i]


receive_el_list(just_list.copy())


# получения элемента дека
# receive_el_deque ---- 0.007914499999999991
def receive_el_deque(my_deque):
    for i in range(1, count, 3):
        a = my_deque[i]


receive_el_deque(just_deque.copy())


print(f'receive_el_list ---- {timeit("receive_el_list(just_list.copy())", globals=globals(), number=1000)}')
print(f'receive_el_deque ---- {timeit("receive_el_deque(just_deque.copy())", globals=globals(), number=1000)}')

"""Там где функционал встроенный под задачу скорость одинакова. Там где нет функционала у списка под конкретную задачу, 
там список работает дольше"""