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


def haffman_tree(my_string):
    count = Counter(my_string)
    sorted_deque = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_deque) != 1:
        while len(sorted_deque) > 1:
            weight = sorted_deque[0][1] + sorted_deque[1][1]
            united = {0: sorted_deque.popleft()[0],
                      1: sorted_deque.popleft()[0]}
            for i, _count in enumerate(sorted_deque):
                if weight > _count[1]:
                    continue
                else:
                    sorted_deque.insert(i, (united, weight))
                    break
            else:
                sorted_deque.append((united, weight))
    else:
        weight = sorted_deque[0][1]
        united = {0: sorted_deque.popleft()[0], 1: None}
        sorted_deque.append((united, weight))
    return sorted_deque[0][0]


code_dict = dict()


def haffman_code(tree, path=''):
    if type(tree) is not dict:
        code_dict[tree] = path
    else:
        haffman_code(tree[1], path=f'{path}1')
        haffman_code(tree[0], path=f'{path}0')


my_string = "beep boop beer!"

haffman_code(haffman_tree(my_string))

for i in my_string:
    print(code_dict[i], end=' ')
print()
