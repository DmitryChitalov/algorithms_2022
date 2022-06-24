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

from collections import deque, Counter


def haffman_tree(string):
    count = Counter(string)
    sort_el = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sort_el) != 1:
        while len(sort_el) > 1:
            weight = sort_el[0][1] + sort_el[1][1]
            comb = {0: sort_el.popleft()[0], 1: sort_el.popleft()[0]}
            for i, count in enumerate(sort_el):
                if weight > count[1]:
                    continue
                else:
                    sort_el.insert(i, (comb, weight))
                    break
            else:
                sort_el.append((comb, weight))
    else:
        weight = sort_el[0][1]
        comb = {0: sort_el.popleft()[0], 1: None}
        sort_el.append((weight, comb))
    return sort_el[0][0]


code_table = {}


def haffman_code(tree, path=' '):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = 'hello world!'
haffman_code(haffman_tree(s))


print(code_table)
for i in s:
    print(code_table[i], end=' ')
print()
