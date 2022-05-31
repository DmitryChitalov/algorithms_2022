def lin_complexity(array):
    var = array[0]
    for i in range(1, len(array)):  # O(N)
        if array[i] < var:
            var = array[i]
    return var


def sq_complexity(array):
    """по сути сортировка с возвратом первого элемента"""
    for i in range(len(my_list) - 2):
        for j in range(len(my_list) - i - 1):  # O(N^2)
            if array[j] > array[j+1]:
                t = array[j]
                array[j] = array[j+1]
                array[j+1] = t
    return array[0]


my_list = [1, 4, 7, -4, 6, -36, -96, -87, -90, 95, 5, 1]
min_lin_el = lin_complexity(my_list)
min_sq_el = sq_complexity(my_list)
print(f'Минимальный элемент: {min_sq_el}')
print(f'Минимальный элемент: {min_lin_el}')
