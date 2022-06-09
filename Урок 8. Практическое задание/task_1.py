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


def h_tree(n):
    symbols_count = Counter(n)
    symbols_count_sort = deque(sorted(symbols_count.items(), key=lambda item: item[1]))
    if len(symbols_count_sort) != 1:
        while len(symbols_count_sort) > 1:
            new_weight = symbols_count_sort[0][1] + symbols_count_sort[1][1]
            new_element = {0: symbols_count_sort.popleft()[0],
                           1: symbols_count_sort.popleft()[0]}
            for i, _count in enumerate(symbols_count_sort):
                if new_weight > _count[1]:
                    continue
                else:
                    symbols_count_sort.insert(i, (new_element, new_weight))
                    break
            else:
                symbols_count_sort.append((new_element, new_weight))
    else:
        new_weight = symbols_count_sort[0][1]
        new_element = {0: symbols_count_sort.popleft()[0], 1: None}
        symbols_count_sort.append((new_element, new_weight))
    return symbols_count_sort[0][0]


code_table = dict()


def h_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        h_code(tree[0], path=f'{path}0')
        h_code(tree[1], path=f'{path}1')


n = "we are the champions!"
h_code(h_tree(n))
for i in n:
    print(code_table[i], end=' ')
print()
