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


def profile(func):
    import time

    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        stop_t = time.time()
        print(f'функция выполнялась: {stop_t - start_t}')
        return result
    return wrapper


@profile
# Сложность O(n)
def fill_list(n):
    return [n for n in range(n)]


@profile
# Сложность O(n)
def fill_dict(n):
    return {n: n for n in range(n)}


@profile
# Сложность O(n)
def del_from_list(list_d, start, count):
    [list_d.pop(n) for n in range(start, start + count)]


@profile
# Сложность O(n)
def del_from_dict(dict_d, start, count):
    [dict_d.pop(n) for n in range(start, start + count)]


@profile
# Сложность O(n)
def change_list(list_ch: list, start, count, new_val):
    for n in range(start, start + count):
        list_ch[n] = new_val


@profile
# Сложность O(n)
def change_dict(dict_ch, start, count, new_val):
    for n in range(start, start + count):
        dict_ch[n] = new_val


if __name__ == '__main__':
    print('Заполняем список')
    my_list = fill_list(1000000)

    print('Заполняем словарь')
    my_dict = fill_dict(1000000)

    print('Удаляем элементы из списка')
    del_from_list(my_list, 100000, 1000)

    print('Удаляем элементы из словаря')
    del_from_dict(my_dict, 100000, 1000)

    print('Изменяем элементы списка')
    change_list(my_list, 100, 10000, 1)

    print('Изменяем элементы словаря')
    change_dict(my_dict, 100, 10000, 1)

"""
Несмотря на то, что сложность операций одинаковая, выполнение функций занимает разное время

Заполнение списка происходит быстрее заполнения словаря
При заполнении словаря время затрачивается на создание хеша для ключей

Удаление элементов для списка происходит медленее удаления элементов из словаря
При удалении элемента из списка, время затрачивается на 'смещение элементов'.

Изменение элементов списка и словаря занимают примерно одинаковое время 
"""