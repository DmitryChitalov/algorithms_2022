"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from time import perf_counter


def read_file():
    """
    Функция для парсинга файла со словами через запятую.
    Добавлена, чтобы было чем заполнять список и словарь, и чтобы не загромождать код.
    """
    with open('cities.txt', 'r', encoding='utf-8') as f_str:
        f_list = f_str.read().split()
        for i in range(0, len(f_list)):
            f_list[i] = f_list[i].replace(',', '')
        return f_list


def time_profiler(func):
    def wrapper(arg1, arg2):
        start = perf_counter()
        user_func = func(arg1, arg2)
        print(f'Время выполнения составило: {perf_counter() - start: .7f} сек\n')
        return user_func
    return wrapper


@time_profiler
def fill_a_list(source_list: list, quantity: int):
    # Сложность линейная O(n). Примечание n = quantity.
    target_list = list()
    for i in range(0, quantity):
        target_list.append(source_list[i])
    return target_list


@time_profiler
def fill_a_dict(source_list: list, quantity: int):
    # Сложность линейная O(n). Примечание n = quantity.
    target_dict = {i + 1: source_list[i] for i in range(0, quantity)}
    return target_dict


@time_profiler
def get_from_list(source_list: list, number: int):
    # Сложность линейная O(len(source_list))
    return source_list[number]


@time_profiler
def get_from_dict(source_dict: dict, key: int):
    # Сложность константная O(1)
    return source_dict[key]


@time_profiler
def remove_from_list(source_list: list, quantity: int):
    # Сложность линейная O(n). Примечание n = quantity
    for _ in range(0, quantity):
        source_list.pop()
    return source_list


@time_profiler
def remove_from_dict(source_dict: dict, quantity: int):
    # Сложность линейная O(n). Примечание n = quantity
    key_max = max(source_dict.keys())
    for i in range(key_max, key_max - quantity, -1):
        source_dict.pop(i, '')
    return source_dict


if __name__ == '__main__':
    """
    Вывод. Операции со списками работают быстрее при n = 10 и n = 1000.
    Теоретически, операция получения элемента из словаря должна быть быстрее, чем получение
    элемента из списка. На практике получается, что операции или равны по времени, или операция
    со списком быстрее.
    Вероятно, работа со словарем медленнее потому, что при обращении к словарю компьютер
    работает с вдвое большим количеством элементов (ключ, значение)
    """
    user_string = read_file()
    n = 1000

    print(f'Добавление {n} элементов в список')
    user_list = fill_a_list(user_string, n)
    # print(user_list)
    print(f'Добавление {n} пар ключ-значение в словарь')
    user_dict = fill_a_dict(user_string, n)
    # print(user_dict)
    print(f'Получение {int(n / 2)}-го элемента из списка')
    user_item = get_from_list(user_list, int(n / 2) - 1)
    # print(user_item)
    print(f'Получение {int(n / 2)}-го элемента из cловаря')
    user_key_value = get_from_dict(user_dict, int(n / 2))
    # print(user_key_value)
    print(f'Удаление {n} элементов из списка')
    user_list_2 = remove_from_list(user_list, n)
    # print(user_list_2)
    print(f'Удаление {n} элементов из словаря')
    user_dict_2 = remove_from_dict(user_dict, n)
    # print(user_dict_2)
    n = 10
    print(f'Добавление {n} элементов в список')
    user_list = fill_a_list(user_string, n)
    # print(user_list)
    print(f'Добавление {n} пар ключ-значение в словарь')
    user_dict = fill_a_dict(user_string, n)
    # print(user_dict)
    print(f'Получение {int(n / 2)}-го элемента из списка')
    user_item_2 = get_from_list(user_list, int(n / 2) - 1)
    # print(user_item)
    print(f'Получение {int(n / 2)}-го элемента из cловаря')
    user_key_value_2 = get_from_dict(user_dict, int(n / 2))
    # print(user_key_value)
    print(f'Удаление {n} элементов из списка')
    user_list_3 = remove_from_list(user_list, n)
    # print(user_list_2)
    print(f'Удаление {n} элементов из словаря')
    user_dict_3 = remove_from_dict(user_dict, n)
    # print(user_dict_2)


