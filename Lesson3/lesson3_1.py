import time


def wrapper(n):
    def time_check(func):
        def timer():
            res = 0
            for el in range(n):
                start = time.time()
                func()
                end = time.time()
                result = end - start
                res += result
            print(f'Время выполнения: {res} секунд')

        return timer

    return time_check


@wrapper(1000)
def my_lst1():
    lst = [i for i in range(0, 1000)]  # O(n)


@wrapper(1000)
def my_lst2():
    lst = []
    for i in range(1000):  # O(n)
        lst.append(i)  # O(1)


@wrapper(1000)
def my_dict():
    for i in range(1000):  # O(n)
        my_dict = {}
        my_dict.setdefault(i, i)  # O(1)


@wrapper(1000)
def my_dict2():
    my_dict = {num: num for num in range(0, 1000)}  # O(n)


# my_lst1()
# my_lst2()
# my_dict()
# my_dict2()

# Список заполняется быстрее с помощью list comprehension.
# Заполнение словаря происходит медленее, возможно потому, что словарь это хеш таблица и создание хешей также требует времени.


@wrapper(200000)
def change_lst():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # O(1)
    lst.pop(3)  # O(1)


@wrapper(200000)
def change_dct():
    my_dict = {'1': 'addfs', '2': 'ewwfe', '3': 'w3ewf', '4': 'wwegr', '5': 'wqfrger', '6': 'wfrevd', '7': 'esgf',
               '8': 'efe'}  # O(1)
    my_dict.pop('2')  # O(1)


# change_lst()
# change_dct()

# Удаление из словаря происходит быстрее, поскольку удаление происходит по ключу, который в свою очередь хранится в хеше.
@wrapper(50000)
def insert_lst():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # O(1)
    lst.append(5)  # O(1)


@wrapper(50000)
def insert_dct():
    my_dict = {'1': 'addfs', '2': 'ewwfe', '3': 'w3ewf', '4': 'wwegr', '5': 'wqfrger', '6': 'wfrevd', '7': 'esgf',
               '8': 'efe'}  # O(1)
    my_dict.setdefault('9', 'wadff')  # O(1)


insert_lst()
insert_dct()

# Добавление элемента в список происходит быстрее.Возможно потому, что для ключа создается хеш, а это также требует времени.
