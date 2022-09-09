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



"""Хаффман через коллекции"""

from collections import Counter

code_table = dict()


def convert_to_dict(data):
    count = Counter(data)
    # print(count)
    sort_lst = [(k, v) for k, v in count.items()]
    # sort_lst=sorted(count.items(), key=lambda x: x[1])
    #print(sort_lst)
    if len(sort_lst) != 1:
        while len(sort_lst) > 1:
            m = sort_lst[-1][1]+sort_lst[-2][1]
            #print(m)
            union = {0: sort_lst.pop()[0],
                     1: sort_lst.pop()[0]}
            for i, _count in enumerate(sort_lst):
                if m > _count[1]:
                    continue
                else:
                    sort_lst.insert(i, (union, m))
                    break
            else:
                sort_lst.append((union, m))
                # print(sort_lst)
    else:
        m = sort_lst[0][1]
        union = {0: sort_lst[0][0], 1: None}
        sort_lst.append((union, m))
    return sort_lst[0][0]


def dict_to_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        dict_to_code(tree[0], path=f'{path}0')
        dict_to_code(tree[1], path=f'{path}1')


def str_to_code(string):
    dict_to_code(convert_to_dict(string))
    res = ''
    for i in s:
        res = f'{res} {code_table[i]}'
    return print(f'Строка {string} имеет код:\n{res}')


s = "next door"
str_to_code(s)


"""
Как-то так)
"""
#
# from collections import Counter, deque
#
#
# def haffman_tree(s):
#     # Считаем уникальные символы.
#     # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
#     count = Counter(s)
#     # Сортируем по возрастанию количества повторений.
#     # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
#     # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
#     sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
#     # Проверка, если строка состоит из одного повторяющего символа.
#     if len(sorted_elements) != 1:
#         # Цикл для построения дерева
#         while len(sorted_elements) > 1:
#             # далее цикл объединяет два крайних левых элемента
#             # Вес объединенного элемента (накопленная частота)
#             # веса - 2, 4, 4, 7, 8, 15
#             weight = sorted_elements[0][1] + sorted_elements[1][1]
#             # Словарь из 2 крайних левых элементов, попутно вырезаем их
#             # из "sorted_elements" (из очереди).
#             # comb - объединенный элемент
#             '''
#             {0: 'r', 1: '!'}
#             {0: {0: 'r', 1: '!'}, 1: 'p'}
#             {0: ' ', 1: 'o'}
#             {0: 'b', 1: {0: ' ', 1: 'o'}}
#             {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
#             {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
#             '''
#             comb = {0: sorted_elements.popleft()[0],
#                     1: sorted_elements.popleft()[0]}
#
#             # Ищем место для ставки объединенного элемента
#             for i, _count in enumerate(sorted_elements):
#                 if weight > _count[1]:
#                     continue
#                 else:
#                     # Вставляем объединенный элемент
#                     # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
#                     sorted_elements.insert(i, (comb, weight))
#                     break
#             else:
#                 # Добавляем объединенный корневой элемент после
#                 # завершения работы цикла
#
#                 sorted_elements.append((comb, weight))
#             '''
#             deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
#             deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
#             deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
#             deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
#             deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
#             deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
#             '''
#     else:
#         # приравниваемыем значение 0 к одному повторяющемуся символу
#         weight = sorted_elements[0][1]
#         comb = {0: sorted_elements.popleft()[0], 1: None}
#         sorted_elements.append((comb, weight))
#     # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
#     # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
#     # словарь - дерево
#     return sorted_elements[0][0]
#
#
# code_table = dict()
#
# """
# tree - {
# 0: {0: 'b', 1: {0: ' ', 1: 'o'}},
# 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
# }
# """
#
#
# def haffman_code(tree, path=''):
#     # Если элемент не словарь, значит мы достигли самого символа
#     # и заносим его, а так же его код в словарь (кодовую таблицу).
#     if not isinstance(tree, dict):
#         code_table[tree] = path
#     # Если элемент словарь, рекурсивно спускаемся вниз
#     # по первому и второму значению (левая и правая ветви).
#     else:
#         haffman_code(tree[0], path=f'{path}0')
#         haffman_code(tree[1], path=f'{path}1')
#
#
# # строка для кодирования
# s = "next door"
#
# # функция заполняет кодовую таблицу (символ-его код)
# # {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
# haffman_code(haffman_tree(s))
#
# # code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
#
# # выводим коды для каждого символа
# for i in s:
#     print(code_table[i], end=' ')
# print()