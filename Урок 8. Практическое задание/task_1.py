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
from collections import Counter, deque


def treehaf(s):
    count = Counter(s)
    sort_elem = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sort_elem) != 1:
        while len(sort_elem) > 1:
            volume = sort_elem[0][1] + sort_elem[1][1]
            combo = {0: sort_elem.popleft()[0],
                    1: sort_elem.popleft()[0]}
            for i, cnt in enumerate(sort_elem):
                if volume > cnt[1]:
                    continue
                else:
                    sort_elem.insert(i, (combo, volume))
                    break
            else:
                sort_elem.append((combo, volume))
    else:
        weight = sort_elem[0][1]
        comb = {0: sort_elem.popleft()[0], 1: None}
        sort_elem.append((comb, weight))
    return sort_elem[0][0]


code_table = dict()


def haffinal_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffinal_code(tree[0], path=f'{path}0')
        haffinal_code(tree[1], path=f'{path}1')


st = "beep boop beer!"

haffinal_code(treehaf(st))


print(treehaf(st))
print('\n', '-' * 100)
print(code_table)
for i in st:
    print(code_table[i], end=' ')

print('\n', '-' * 100)
