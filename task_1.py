from time import time

print('Задание a:')


def measure_time(func):
    def measure_time_wrapper(*args):
        start_val = time()
        func(*args)
        end_val = time()
        return end_val - start_val
    return measure_time_wrapper


@measure_time
def fill_in_list(num):
    for i in range(num):
        new_list.append(i)
    return new_list


@measure_time
def fill_in_dict(num):
    for i in range(num):
        new_dict[i] = i
    return new_dict

# Добавление элемента в конец списка: O(1); заполнение словаря: O(1), но словарь будет заполняться быстрее, так как это
# хэш-таблица.


new_list = []
new_dict = {}

test_1 = fill_in_list(150000)
test_2 = fill_in_dict(150000)

print(f'Время заполнения списка: {test_1}\nВремя заполнения словаря: {test_2}')
print('-' * 60)

print('Задание b:')


@measure_time
def modify_list(num):
    for i in range(num):
        new_list[i-1] = i
    return new_list


@measure_time
def modify_dict(num):
    for i in range(num):
        new_dict[i-1] = i
    return new_dict


test_3 = modify_list(50000)
test_4 = modify_dict(50000)

print(f'Время изменения элементов списка: {test_3}\nВремя изменения элементов словаря: {test_4}')
print('-' * 10)


@measure_time
def del_elem_list(num):
    for i in range(num):
        new_list.pop(i)
    return new_list


@measure_time
def del_elem_dict(num):
    for i in range(num):
        new_dict.pop(i)
    return new_dict


test_5 = del_elem_list(4500)
test_6 = del_elem_dict(4500)

print(f'Время удаления элементов списка: {test_5}\nВремя удаления элементов словаря: {test_6}')


# Изменение элемента списка: O(1); изменение элемента словаря: O(1); а удаление элементов из списка O(n) против
# O(1) у словаря, значит, вычислительная сложность функций изменения словаря меньше, поэтому в целом изменение словаря
# происходит быстрее.
