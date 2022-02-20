"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(string):

    el_cnt = Counter(string)
    #print(el_cnt)

    sorted_string = deque(sorted(el_cnt.items(), key=lambda item: item[1]))
    #print(sorted_string)
    while len(sorted_string) > 1:

        weight = sorted_string[0][1] + sorted_string[1][1]

        node = MyNode(left=sorted_string.popleft()[0], right=sorted_string.popleft()[0])

        for pos, pair in enumerate(sorted_string):
            if weight > pair[1]:
                continue
            else:
                sorted_string.insert(pos, (node, weight))
                break
        else:
            sorted_string.append((node, weight))

    return sorted_string[0][0]


letters_code = dict()


def haffman_code(tree, path=''):

    if not isinstance(tree, MyNode):
        letters_code[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


s = "beep boop beer!"

haffman_code(haffman_tree(s))

print(f'\nСтрока кода после кодирования строки "{s}": ')
for el in s:
    print(letters_code[el], end=' ')
print()

