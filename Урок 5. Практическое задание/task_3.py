"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""
from timeit import timeit
from collections import deque
import random

simple_lst = []
my_deque = deque()

""" 1 append, pop, extend списка и дека """
def append_measure(lst: list, num: int) -> list:
    for _ in range(num):
        lst.append(random.randint(0, 10000))
    return lst


def pop_measure(lst: list) -> list:
    lst.pop()
    return lst


def extend_measure(lst: list) -> list:
    lst.extend(random.sample(range(0, 10000), 10))
    return lst


""" 2 appendleft, popleft, extendleft дека и соответствующих им операций списка"""
def deque_appendleft(_deque: deque, new_el) -> deque:
    _deque.appendleft(new_el)
    return _deque


def list_appendleft(lst: list, new_el) -> list:
    lst.insert(0, new_el)
    return lst

def deque_popleft(_deque: deque) -> deque:
    item = _deque.popleft()
    return _deque


def list_popleft(lst: list) -> list:
    item = lst.pop(0)
    return lst


def deque_extendleft(_deque: deque, new_list: list):
    _deque.extendleft(new_list)


def list_extendleft(lst: list, new_list: list):
    for number in new_list:
        lst.insert(0, number)


""" 3 операции получения элемента списка и дека """

def getelement_list_deque(lst: list, el: any) -> any:
    index = lst.index(el)
    return lst[index]


if __name__ == "__main__":
    separator = 50
    print("*" * separator + " замеры 1 " + "*" * separator)
    iterations = 100
    number = 100000
    for variable in (simple_lst, my_deque):
        print(f"'APPEND method' measure for type: %s takes "
              f"{timeit('append_measure(variable, iterations)', globals=globals(), number=number)} s"
              % (type(variable)))
        print(f"'POP method' measure for type: %s takes "
              f"{timeit('pop_measure(variable)', globals=globals())} s"
              % (type(variable)))
        print(f"'EXTEND method' measure for type: %s takes "
              f"{timeit('extend_measure(variable)', globals=globals())} s"
              % (type(variable)))
    simple_lst.clear()
    my_deque.clear()
    print("*"*separator + " замеры 2 " + "*"*separator)
    """
    1. Результаты (number=1000000): 
        'APPEND method' measure for type: <class 'list'> takes 10.5886514 s
        'APPEND method' measure for type: <class 'collections.deque'> takes 10.612354500000002 s
        'POP method' measure for type: <class 'list'> takes 0.1345660000000013 s
        'POP method' measure for type: <class 'collections.deque'> takes 0.11896229999999974 s
        'EXTEND method' measure for type: <class 'list'> takes 10.1739426 s
        'EXTEND method' measure for type: <class 'collections.deque'> takes 10.232057899999997 s
    Вывод: 
        в deque методы APPEND,EXTEND происходят медленнее но я бы сказал незначительно, особой разницы со списком 
        не заметил прогнав функции несколько раз. Однако метод POP быстрее в deque примерно на 10%
        
    """

    new_el = 102
    number = 100000
    print(f'deque_appendleft takes {timeit("deque_appendleft(my_deque, new_el)", globals=globals(), number=number)} s')
    print(f'list_appendleft takes {timeit("list_appendleft(simple_lst, new_el)", globals=globals(), number=number)} s')
    print(f'deque_popleft takes {timeit("deque_popleft(my_deque)", globals=globals(), number=number)} s')
    print(f'list_popleft takes {timeit("list_popleft(simple_lst)", globals=globals(), number=number)} s')
    new_list = random.sample(range(0, 10000), 10)
    number = 10000
    print(f'deque_extendleft takes {timeit("deque_extendleft(my_deque, new_list)", globals=globals(), number=number)} s')
    print(f'list_extendleft takes {timeit("list_extendleft(simple_lst, new_list)", globals=globals(), number=number)} s')
    simple_lst.clear()
    my_deque.clear()
    """
    2. Результаты на параметре number=100000: 
        deque_appendleft takes 0.012617999999999997 s
        list_appendleft takes 2.7037382 s
        deque_popleft takes 0.010751399999999744 s
        list_popleft takes 0.9621523000000001 s
        
        Результаты на параметре number=10000:
        deque_extendleft takes 0.0022676000000000016 s
        list_extendleft takes 2.6538306 s
    Вывод:
        В сравнении с списком методы deque (appendleft, popleft, extend) работают очень быстро что дает существенный   
        прирост к производительности.
    """
    print("*" * separator + " замеры 3 " + "*" * separator)
    test_value = "testvalue"
    test = [*random.sample(range(0, 10000), 180), test_value, *random.sample(range(0, 10000), 100)]
    my_deque.extend(test)
    simple_lst.extend(test)
    for variable in (simple_lst, my_deque):
        print(f"'getelement_list_deque' measure for type: %s takes "
                  f"{timeit('getelement_list_deque(variable, test_value)', globals=globals())} s"
                  % (type(variable)))
    """
    3. Результаты (number=1000000):
        'getelement_list_deque' measure for type: <class 'list'> takes 3.290357 s
        'getelement_list_deque' measure for type: <class 'collections.deque'> takes 3.3617274999999998 s
    Вывод: Получение елемента из списка быстрее чем в deque примерно на 2% судя по замерам
    """