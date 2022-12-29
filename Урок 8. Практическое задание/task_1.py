"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque

"""
Функция вставки в кортеж нового элемента- узла  со значениями: (словарь , вес узла)
"""


def tuple_insert(dict, val, weight):
    for i, _count in enumerate(dict):
        if weight > _count[1]:
            continue
        else:
            dict.insert(i, (val, weight))
            return dict
    else:
        dict.append((val, weight))


"""
Функция  составления таблицы для метода сжатия Хаффмана. После сортировки берутся крайние левые кортежи  и объединяются
в кортеж ,состоящий из словаря с ключами - символавми  и их значенями-переходами ввиде 0 или 1 (при последующих проходах
0 или 1 добавляются к текущим значеням слева). В функции  в цикле идет проверка на тип первых элементлов кортежа
объедияемых узлов, в зависимости от которого по разному изменяются значения  символов после прохода в словаре 
"""


def haffman_table(test_string):
    sorted_elm = deque(sorted(Counter(test_string).items(), key=lambda item: item[1]))
    sorted_elm_tmp = sorted_elm
    for i in range(len(sorted_elm) - 1):
        dict_tmp = {}
        dict_tmp1 = {}
        if isinstance(sorted_elm_tmp[1][0], dict) and isinstance(sorted_elm_tmp[0][0], dict):
            dict_tmp = {key: '0' + val for key, val in sorted_elm_tmp[0][0].items()}
            dict_tmp1 = {key: '1' + val for key, val in sorted_elm_tmp[1][0].items()}
            dict_tmp.update(dict_tmp1)
            tuple_insert(sorted_elm_tmp, dict_tmp, sorted_elm_tmp[0][1] + sorted_elm_tmp[1][1])
        elif isinstance(sorted_elm_tmp[0][0], dict):
            dict_tmp = {key: '0' + val for key, val in sorted_elm_tmp[0][0].items()}
            dict_tmp[sorted_elm_tmp[1][0]] = '1'
            tuple_insert(sorted_elm_tmp, dict_tmp, sorted_elm_tmp[0][1] + sorted_elm_tmp[1][1])
        elif isinstance(sorted_elm_tmp[1][0], dict):
            dict_tmp = {key: '1' + val for key, val in sorted_elm_tmp[1][0].items()}
            dict_tmp[sorted_elm_tmp[0][0]] = '0'
            tuple_insert(sorted_elm_tmp, dict_tmp, sorted_elm_tmp[0][1] + sorted_elm_tmp[1][1])
        else:
            tuple_insert(sorted_elm_tmp, {sorted_elm_tmp[0][0]: '0', sorted_elm_tmp[1][0]: '1'},
                         sorted_elm_tmp[0][1] + sorted_elm_tmp[1][1])
        sorted_elm_tmp.popleft()
        sorted_elm_tmp.popleft()
    return sorted_elm_tmp[0][0]


print(haffman_table('beep boop beer!'))
