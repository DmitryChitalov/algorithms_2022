"""Профилировка"""

from cProfile import run


def get_count(items):
    return items.__len__()


def get_sum(items):

    new_sum = 0
    for i in items:
        new_sum += i
    return new_sum


def main():
    my_lst = [3, 5, 6, 7, 3]
    res_count = get_count(my_lst)
    res_sum = get_sum(my_lst)


run('main()')
