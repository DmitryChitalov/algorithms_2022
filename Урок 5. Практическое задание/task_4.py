"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from time import time
from collections import OrderedDict


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} - {end - start}')
        return result

    return timer


@time_decorator
def entry_dict(num):
    """
    Создания обычного словаря
    :param num: количество элементов словаря
    :return: словарь
    """
    normal_dict = {}
    for i in range(num):
        normal_dict[i] = i + 2
    return normal_dict


@time_decorator
def entry_ordered_dict(num):
    """
    Создания словаря с помощью OrderedDict()
    :param num: количество элементов словаря
    :return: словарь
    """
    ordered_dict = OrderedDict()
    for i in range(num):
        ordered_dict[i] = i + 2
    return ordered_dict


@time_decorator
def dict_output(dict_work):
    """
    Изменение элементов словаря
    :param dict_test: словарь
    :return: измененный словарь
    """
    for key in dict_work.keys():
        dict_work[key] += 1


@time_decorator
def clear_dict(dict_work):
    """
    Удаление 20 000 элементов словаря через pop
    :param dict_test: словарь
    :return: словарь уменьшенный на 20000 элементов
    """
    if len(dict_work) > 20000:
        for key in range(20000):
            dict_work.pop(key)


@time_decorator
def clear_dict_ordered(dict_work):
    """
    Удаление 20 000 элементов словаря через popitem
    :param dict_test: словарь
    :return: словарь уменьшенный на 20000 элементов
    """
    if len(dict_work) > 20000:
        for i in range(20000):
            dict_work.popitem(last=True)


if __name__ == '__main__':
    number = 10 ** 6
    print('Замер времени заполнения словаря без OrderedDict()')
    my_dict_normal = entry_dict(number)
    print('Замер времени заполнения словаря с OrderedDict()')
    my_dict_ordered = entry_ordered_dict(number)
    print('Замер времени изменения словаря созданого без OrderedDict()')
    dict_output(my_dict_normal)
    print('Замер времени изменения словаря созданого с OrderedDict()')
    dict_output(my_dict_ordered)
    print('Замер времени удаления записей словаря созданого без OrderedDict()')
    clear_dict(my_dict_normal)
    print('Замер времени удаления записей словаря созданого с OrderedDict() через pop')
    clear_dict(my_dict_ordered)
    print('Замер времени удаления записей словаря созданого с OrderedDict() через popitem')
    clear_dict_ordered(my_dict_ordered)

    """
    результаты замеров при number = 10 ** 6
    Замер времени заполнения словаря без OrderedDict()
    Время выполенения функции entry_dict - 0.12865424156188965
    Замер времени заполнения словаря с OrderedDict()
    Время выполенения функции entry_ordered_dict - 0.18650150299072266
    Замер времени изменения словаря созданого без OrderedDict()
    Время выполенения функции dict_output - 0.17852210998535156
    Замер времени изменения словаря созданого с OrderedDict()
    Время выполенения функции dict_output - 0.2099905014038086
    Замер времени удаления записей словаря созданого без OrderedDict()
    Время выполенения функции clear_dict - 0.003988981246948242
    Замер времени удаления записей словаря созданого с OrderedDict() через pop
    Время выполенения функции clear_dict - 0.004155158996582031
    Замер времени удаления записей словаря созданого с OrderedDict() через popitem
    Время выполенения функции clear_dict_ordered - 0.006815671920776367
    
    Замеры показали, что все операции с обычным словарям происходит быстрее, 
    даже с использованием popitem(last=True) в упорядочном словаре происходят медленее.
    Начиная с версии Python 3.6 обычный словарь поддерживает запоминание порядка добавления 
    элементов словаря. Таким образом использование OrderedDict в версиях Python 3.6 и выше 
    не оправдано, только если есть необходимость использования особых функции:
    move_to_end(key, last=True), move_to_end(key, last=False), popitem(last=True),
    popitem(last=False), которых нет у обычного словаря
    """
