import random
import time


def time_decorator(function):
    def timer(*args):
        start_val = time.time()
        function(*args)
        end_val = time.time()
        time_funk = end_val - start_val
        print(f'Время выполенения функции {function.__name__} составило {time_funk}')
        return time_funk
    return timer


my_list = []
my_dict = {}

# o(1). Вставка в конец списка
@time_decorator
def list_fill(i):
    for el in range(i):
        my_list.append(i)
    return my_list


list_fill(1000000)

# o(1) быстрее словарь заполняется, т.к. это хэш-таблица
@time_decorator
def dict_fill(i):
    for el in range(i):
        my_dict[i] = i
    return my_dict


dict_fill(1000000)


@time_decorator
def change_list(i):
    for el in range(i):
        my_list.pop(i)     # 0(n)
    for el in range(i):
        my_list[el] = my_list[el + 20]    # 0(1)

    return my_list


change_list(1000)


@time_decorator
def change_dict(i):
    for v in range(i):
        my_dict.popitem()   # 0(1)
    for j in range(1, 100000):
        my_dict[j] = 'Hi'   #0(1)
    return my_dict


change_dict(1)


