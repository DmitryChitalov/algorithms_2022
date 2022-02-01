import time


def time_measure(func):
    def wrapper(my_obj, spec=0):
        start_point = time.time()
        func(my_obj, spec)
        end_point = time.time()
        return end_point - start_point
    return wrapper


@time_measure
def fill_the_dict(my_dict: dict, spectra):
    for i in range(spectra):
        my_dict[i] = i
    return my_dict


@time_measure
def fill_the_array(my_array: list, spectra):
    for i in range(spectra):
        my_array.append(i)
    return my_array


@time_measure
def take_a_symbol(my_obj, spec=0):
    return [my_obj[i] for i in range(len(my_obj))]


@time_measure
def delete(my_obj, spec=0):
    if type(my_obj) == dict:
        for i in range(len(my_obj)):
            del my_obj[i]
    else:
        for i in range(len(my_obj)):
            my_obj.pop()


# Ниже можно раскомментировать, чтобы посмотреть на маленьких и больших данных
"""
Часть А
dictionary = {}
test_array = []
time_dict = fill_the_dict(dictionary, 100)
time_arr = fill_the_array(test_array, 100)
print(f'Время на заполнение до 100. Словарь: {time_dict}, Список {time_arr}')
time_dict = fill_the_dict(dictionary, 1000000)
time_arr = fill_the_array(test_array, 1000000)
print(f'Время на заполнение до 1000000. Словарь: {time_dict}, Список {time_arr}')
"""

# Меньше на порядок для списка, т к не тратится время на генерацию хэша, при этом
# для списка сложность O(N), а для словаря по идее O(1), но тратится время на хэш,
# поэтому в худшем случае для словарей может быть достижима сложность O(N)
# ----------------------------------------------------------------------------------------

# ЧАСТЬ Б
# Получение элементов
dictionary = {}
time_dict = fill_the_dict(dictionary, 10000)
print('Вставка 10000 элементов в словарь: ', time_dict)
time_dict = take_a_symbol(dictionary)
print('Получаем 10000 элементов из словаря: ', time_dict)  # Сложность O(1)
test_array = []
time_array = fill_the_array(test_array, 10000)
print('Вставка 10000 элементов в список:', time_array)
time_array = take_a_symbol(test_array)
print('Получаем 10000 элементов из списка: ', time_array)  # Сложность O(1)
# Удаление
time_dict = delete(dictionary)
print('Удаление 10000 символов из словаря', time_dict)  # Сложность O(1)
time_array = delete(test_array)
print('Удаление 10000 символов из списка', time_array)  # Сложность O(N)

# Время на удаление из списка на порядок выше аналогичного из словаря, при этом
# время получения элементов примерно равно - одного порядка
