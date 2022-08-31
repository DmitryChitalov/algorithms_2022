"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: получения и удаления элемента.
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
import functools
import time

MY_LIST = []
MY_DICT = {}


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        finish = time.perf_counter()
        delta_time = finish - start
        print(f"Execution time: {delta_time:0.10f} seconds")
        return value

    return wrapper_timer


@timer
def in_my_list(value):  # O(N)
    for i in (range(value)):  # O(N)
        MY_LIST.append(i)  # O(1)
    return f'Заполнили спизок из {value} элементов.'


@timer
def in_my_dict(value):  # O(N)
    for i in (range(value)):  # O(N)
        MY_DICT[i] = i  # O(1)
    return f'Заполнили словарь из {value} элементов.'


@timer
def from_my_list(value):  # O(N)
    for i in (range(value)):  # O(N)
        my_el = MY_LIST[i]  # O(1)
    return f' Получили из списка {value} элементов.'


@timer
def from_my_dict(value):  # O(N)
    for i in (range(value)):  # O(N)
        my_el = MY_LIST[i]  # O(1)
    return f' Получили из словаря {value} элементов.'


@timer
def del_my_list():  # O(n ** 2)
    while MY_LIST:  # O(N)
        # MY_LIST.pop(0)  # O(N) на 1000000 зависает.
        del MY_LIST[0]  # O(N) на 1000000 зависает.
        # MY_LIST.pop()  # O(1) - время становится сопоставимо с удалением из словаря.
    return f'  Удалили из списка все элементы.'


@timer
def del_my_dict():  # O(N)
    while MY_DICT:  # O(N)
        # MY_DICT.pop(len(MY_DICT) - 1)  # O(1)
        del MY_DICT[len(MY_DICT) - 1]  # O(1)
    return f'  Удалили из словаря все элементы.'


@timer
def el_append_in_my_list(value):
    MY_LIST.append(value)  # O(1)
    return ' Добавили элемент в конец списка O(1).'


@timer
def el_insert_in_my_list(i, value):
    MY_LIST.insert(i, value)  # O(N)
    return f' Вставили элемент по индексу - {i} O(N).'


@timer
def el_in_my_dict(value):
    MY_DICT[value] = value  # O(1)
    return ' Добавили 1 лемент в словарь. O(1)'


@timer
def el_from_my_list(value):
    my_el = MY_LIST[value]  # O(1)
    return f'  Получили элемент {my_el} из списка. O(1)'


@timer
def el_from_my_dict(value):
    my_el = MY_LIST[value]  # O(1)
    return f'  Получили элемент {my_el} из словаря. O(1)'


@timer
def del_el_my_list(i):
    del MY_LIST[i]  # O(N)
    return f'   Удалили из списка элемент с индексом {i}. O(N)'


@timer
def del_el_my_dict(i):
    del MY_DICT[i]  # O(N)
    return f'   Удалили из словаря элемент по ключу {i}. O(1)'


if __name__ == '__main__':
    print(in_my_list(1000))
    print(in_my_dict(1000))
    print(in_my_list(10000))
    print(in_my_dict(10000))
    print(in_my_list(100000))
    print(in_my_dict(100000))
    # print(in_my_list(1000000))
    # print(in_my_dict(1000000))

    #  Запись у словаря будет медленнее (почти) всегда, потому что надо посчитать хэш и в память по индексам положить,
    #  а в list() (чтоб добавить элемент в конец) достаточно несколько байт записать в заранее выделенную память,
    #  если заранее выделенной памяти недостаточно,
    #  то может увеличиться время на изменения размера ранее выделенной памяти.

    print('__________________________________________')
    print(from_my_list(1000))
    print(from_my_dict(1000))
    print(from_my_list(10000))
    print(from_my_dict(10000))
    print(from_my_list(100000))
    print(from_my_dict(100000))
    # print(from_my_list(1000000))
    # print(from_my_dict(1000000))

    # Примерно одинаковое время - сложность в обоих случаях линейная.
    # Конкретное время зависит от состояния ОС, памяти, выполняемых процессов.
    # Время извлечения из словаря может оказаться чуть больше,
    # так как извлечение элемента в словаре включает в себя 2 шага: сначала хеширование ключа,
    # а затем извлечение значения (второе), в то время как в списке мы просто извлекаем значение из адреса памяти
    # этого конкретного местоположения списка

    print('__________________________________________')

    print(del_my_list())
    print(del_my_dict())
    print(in_my_list(1000))
    print(del_my_list())
    print(in_my_dict(1000))
    print(del_my_dict())
    print(in_my_list(10000))
    print(del_my_list())
    print(in_my_dict(10000))
    print(del_my_dict())
    print(in_my_list(100000))
    print(del_my_list())
    print(in_my_dict(100000))
    print(del_my_dict())

    # Удаление из списка медленнее - линейная сложность удаления повторяется N раз, общая - квадратичная, .
    # Удаление из словаря быстрее - константная сложность удаления повторяется N раз, общая - линейная,

    print('__________________________________________')
    print(in_my_list(1000000))
    print(in_my_dict(1000000))
    print('Одиночные всавки элементов.')
    print(el_append_in_my_list(1000001))  # O(1)
    print(el_insert_in_my_list(1000002, 1000002))  # O(1)
    # практически равнозначные по времени команды O(1)
    print(el_insert_in_my_list(0, 1000001))  # O(N)
    # модленно, так как элемент вставляется в позицию i (здесь -0), а все остальные сдвигаются.
    print(el_in_my_dict(1000001))  # O(1)

    print(el_from_my_list(1000002))  # O(1)
    print(el_from_my_dict(1000001))  # O(1)

    print(del_el_my_list(0))  # O(N)
    # Удаляется первый элемент и все остальные сдвигаются.
    print(del_el_my_list(1000001))  # O(1) - удаление последнего элемента по времени сравнимо с удалением из словаря.
    print(del_el_my_dict(1000001))  # O(1) - время удаления из словаря может быть чуть больше, так как хешируется ключ.
