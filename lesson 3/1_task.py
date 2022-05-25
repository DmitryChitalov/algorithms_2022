from time import perf_counter


def perf_count(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'Execution time: {perf_counter() - start}')
        return result

    return wrapper


"""
    a) заполнение списка, оцените сложность в O-нотации
       заполнение словаря, оцените сложность в O-нотации
       сделайте аналитику, что заполняется быстрее и почему
       сделайте замеры времени
"""


@perf_count
def list_gen(n):  # O(n)
    return [i for i in range(0, n)]  # O(n)


@perf_count
def dict_gen(n):  # O(n)
    return {i: 'GB' for i in range(0, n)}  # O(n)


ex_lst = list_gen(50000)
ex_dct = dict_gen(50000)

# Словарь заполняется медленнее из-за хэширования ключей


"""
    b) получение элемента списка, оцените сложность в O-нотации
       получение элемента словаря, оцените сложность в O-нотации
       сделайте аналитику, что заполняется быстрее и почему
       сделайте замеры времени
"""


@perf_count
def get_list(lst: list, item):  # O(n)
    for el in lst:  # O(n)
        if el == item:  # O(1)
            return el  # O(1)


@perf_count
def get_dict(dct: dict, item):  # O(1)
    return dct[item]  # O(1)


get_list(ex_lst, 30000)
get_dict(ex_dct, 30000)

# Из словаря данные получить гораздо быстрее поскольку поиск происходит по хэшу ключа

"""
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
"""


@perf_count
def del_list(lst: list, item):  # O(n)
    lst.remove(item)  # O(n)
    return lst  # O(1)


@perf_count
def del_dict(dct: dict, item):  # O(1)
    dct.pop(item)  # O(1)
    return dct  # O(1)


del_list(ex_lst, 2500)
del_dict(ex_dct, 2500)

# Удаление происходит быстрее из словаря, т.к. удаление происходит по хэшу ключа, в то время как в списке нужно пройти
# почти через весь массив данных
