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


s = "my name"
str_to_code(s)