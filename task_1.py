from time import time


def time_speed(fun):
    def deco(*args):
        start = time()
        p = fun(*args)
        print('Время выполнения: ', time()-start)
        return p
    return deco


"""--------------a-------------- """

@time_speed
def append_list(lst_1):            # 0(n)
    for i in range(100000):        # O(n)
        lst_1.append(i)            # O(1)


@time_speed
def append_dict(dic_1):            # O(n)
    for i in range(100000):        # O(n)
        a = str(i)                 # O(1)
        dic_1[a] = i

print('a: ')
lst = []
dic = {}
append_list(lst)
append_dict(dic)

'''
Время выполнения:  0.010093450546264648
Время выполнения:  0.0749812126159668
Формирование словаря происходит медленнее, так как 
вычисление хеша замедляет его заполнение
'''

"""--------------b--------------"""


@time_speed
def get_list(list_2):               # O(n)
    for i in range(len(list_2)):    # O(n)
        list_2[i]                   # O(1)


@time_speed
def get_dict(dict_2):             # O(n)
    for i in dict_2.keys():       # O(n)
        dict_2[i]                 # O(1)

print('b: ')
get_list(lst)
get_dict(dic)

'''
Время выполнения:  0.004552364349365234
Время выполнения:  0.005011796951293945
Получение элемента из списка и из словаря происходит почти с одинаковой скоростью, хотя вроде бы
получение элемента по ключу должно на мой взгляд отрабатываться быстрее, так как ключи хранятся в хеше!
'''

"""--------------c--------------"""

@time_speed
def del_list(list_3):               # O(n)
    for i in range(len(list_3)):    # O(n)
        list_3.pop(0)               # O(1)


@time_speed
def del_dict(dict_3):             # O(n)
    for i in range(len(dict_3)):  # O(n)
        dict_3.pop(str(i))        # O(1)

print('c: ')
del_list(lst)
del_dict(dic)

'''
Время выполнения:  1.360121726989746
Время выполнения:  0.039845943450927734
Удаление элемента из списка как мы видим намного медленнее,
так как происходит перебор всех элементов.
'''
