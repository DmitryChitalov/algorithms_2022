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
    :param int n:
    :return list: list of integers
    """
    return [i for i in range(n + 1)]  # O(n) каждый раз в конец списка добавляется объект
    

@timer
def insert_fill_ls(n: int):
    result = []
    for i in range(n + 1):  #  O(n)
        result.insert(0, i)  # O(n) в начало списка, то есть сдвигается весь список, чтобы вставить новый элемент в начало
    return result


@timer
def fill_dict(n: int) -> dict:
    """
    Function generated dictionary, where key is index, value - random integer
    :param int n: amount of keys
    :return dict: dict of integers
    """
    return {k: v for k, v in enumerate([random.randint(0, n + 1) for _ in range(n + 1)])}  # O(n) так как словарь формируется из в процессе создаваемого списка, 
    # а добавление элемента в словарь имеет сложность O(1), так как словарь - это хэш таблица


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
        items.pop(_)  # O(1) удаляем с конца


if __name__ == '__main__':
    ls = fill_ls(100000)
    insert_ls = insert_fill_ls(100000)  # медленнее, чем append, так как insert здесь вставляет в начало списка 
    dct = fill_dict(100000)  # быстрее, так как словарь - это хэш-таблица 
    change_ls(ls)
    change_ls(insert_ls)
    change_dict(dct)
