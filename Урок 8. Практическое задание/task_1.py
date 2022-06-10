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


def haffman_tree(string: str):
    count = Counter(string)
    sort_elems = deque(sorted(count.items(), key=lambda x: x[1]))
    if len(sort_elems) == 1:
        weight = sort_elems[0][1]
        merge_elems = {0: sort_elems.popleft()[0], 1: None}
        sort_elems.append((merge_elems, weight))
        del weight, merge_elems
    else:
        while len(sort_elems) > 1:
            weight = sort_elems[0][1] + sort_elems[1][1]
            merge_elems = {0: sort_elems.popleft()[0],
                           1: sort_elems.popleft()[0]}
            for i, elem in enumerate(sort_elems):
                if weight > elem[1]:
                    continue
                else:
                    sort_elems.insert(i, (merge_elems, weight))
                    break
            else:
                sort_elems.append((merge_elems, weight))
        del weight, merge_elems

    return sort_elems[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


haffman_code(haffman_tree('молоко делили ледоколом'))

print(code_table)
