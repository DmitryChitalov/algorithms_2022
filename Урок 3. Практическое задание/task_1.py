import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Время выполнения функции {function.__name__} =  {time.perf_counter() - start_time} ')
        return res

    return wrapped


@time_of_function
def fill_list(li, n):
    """Зполнение списка вставкой в конец"""
    for i in range(n):
        li.append(i)  # Сложность O(1)


@time_of_function
def fill_list_ins(li, n):
    """Заполнение списка вставкой в начало"""
    for i in range(n):
        li.insert(0, i)  # Сложность O(n)


@time_of_function
def fill_dict(di, n):
    for i in range(n):
        di[i] = i  # Сложность O(1)


some_list = []
some_list2 = []
some_dict = {}
some_dict2 = {}
fill_list(some_list, 100)
fill_list_ins(some_list2, 100)
fill_dict(some_dict, 100)

"""
    Время выполнения функции fill_list =  1.5199999999999936e-05 наносек. Заполнение через append идет быстрее, так как значение вставляется в конец, сложность O(1)
    Время выполнения функции fill_list_ins =  2.110000000000306e-05 наносек. Заполнение через insert медленнее, так как каждый раз идет пересчет индексов элементов. Сложность O(n)
    Время выполнения функции fill_dict =  1.1400000000001687e-05 наносек. Зполнение словаря быстрее заполнения списка. Сложность также О(1)

    """
print('*' * 100)


@time_of_function
def get_from_list(li, n):
    for i in li:
        if n == i:
            return i  # Сложность O(n)


@time_of_function
def get_from_dict(di, n):
    return di.get(n)  # Сложность O(1)


get_from_list(some_list, 45)
get_from_dict(some_dict, 45)

"""
    Время выполнения функции get_from_list =  1.9000000000060635e-06 Сложность O(n), медленно, так как идет перебор всех элементов
    Время выполнения функции get_from_dict =  1.1000000000038757e-06 Сложность O(1) быстрее списка, так как в словаре можно получить значение по ключу

  """

print('*' * 100)


@time_of_function
def del_from_list(li, n):
    for i in range(n):
        li.pop()  # Сложность O(1)


@time_of_function
def del_from_dict(di, n):
    for i in range(n):
        di.popitem()  # Сложность O(1)


del_from_list(some_list, 50)
del_from_dict(some_dict, 50)

"""
    Время выполнения функции del_from_list =  3.7999999999982492e-06 Сложность O(1)
    Время выполнения функции del_from_dict =  6.499999999999562e-06 Сложность O(1) работает медленее, так ак удаляется пара ключ: значение
"""