"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import random
from time import time


def timer(func):
    """
    Profiling of any function by this decorator
    :param function func:
    :return function:
    """

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Function: {func.__name__}, '
              f'Timing: {end - start}')
        return result

    return wrapper


# Ex. a
@timer
def fill_ls(n: int) -> list:
    """
    Function generated list of numbers from 0 to n
    :param int n: amount of elements
    :return list: list of integers
    """
    return [i for i in range(n + 1)]  # O(n) каждый раз в конец списка добавляется объект


@timer
def insert_fill_ls(n: int):
    result = []
    for i in range(n + 1):  # O(n)
        result.insert(0, i)  # O(n) сдвигается весь список, чтобы вставить новый элемент в начало
    return result


@timer
def fill_dict(n: int) -> dict:
    """
    Function generated dictionary, where key is index, value - random integer
    :param int n: amount of keys
    :return dict: dict of integers
    """
    return {k: v for k, v in enumerate([random.randint(0, n + 1) for _ in range(n + 1)])}
    # O(n) так как словарь формируется из в процессе создаваемого списка,
    # а добавление элемента в словарь имеет сложность O(1)


"""
Из-за того, что словарю необходимо создать хэш-таблицу, затрачивается больше времени на его создание.
В отличие от словаря:
Function: fill_ls, Timing: 0.5406186580657959
Function: fill_dict, Timing: 16.212496519088745
Но если элемент нужно вставить в начало списка, то время заполнения списка будет больше, 
так как сложность вставки составляет O(n).
Здесь словарь заполняется медленней, так как для его создания создаётся отдельный список
"""


# Ex. b
@timer
def change_ls(items: list):
    for i in range(len(items)):  # O(n)
        items[i] = random.randint(0, len(items))  # O(1) обращаемся по индексу 
    for j in range(len(items)):  # O(n)
        items.pop()  # O(1) с конца списка удаляется


@timer
def change_dict(items: dict):
    for k in items.keys():  # O(n)
        items[k] = random.randint(0, len(items.values()))  # O(1) обращение по ключу
    for _ in range(len(items)):  # O(n)
        items.pop(_)  # O(1) удаляем по ключу


"""
Скорость изменения и удаления элементов из списка выполняется быстрее, так как обход элементов происходит поочерёдно
У словаря изменение и удаление происходит медленнее, возможно из-за поиска ключа и значения.
"""
if __name__ == '__main__':
    ls = fill_ls(10_000_000)
    # insert_ls = insert_fill_ls(10_000_000)  # очень долго!!!
    dct = fill_dict(10_000_000)
    change_ls(ls)
    # change_ls(insert_ls)  # очень долго!!!
    change_dict(dct)
