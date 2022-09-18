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


class MyTree:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(my_str):
    count_symbol = Counter(my_str)

    sorted_dict = deque(sorted(count_symbol.items(), key=lambda symbol: symbol[1]))

    while len(sorted_dict) > 1:

        weight = sorted_dict[0][1] + sorted_dict[1][1]
        node = MyTree(left=sorted_dict.popleft()[0], right=sorted_dict.popleft()[0])

        for i, item in enumerate(sorted_dict):
            if weight > item[1]:
                continue
            else:
                sorted_dict.insert(i, (node, weight))
                break
        else:
            sorted_dict.append((node, weight))

    return sorted_dict[0][0]


def haffman_code(tree, path=''):
    if not isinstance(tree, MyTree):
        code_dict[tree] = path

    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


if __name__ == "__main__":
    my_string = input('Введите строку дл кодирования: ')
    code_dict = {}
    haffman_code(haffman_tree(my_string))

    code_str = " ".join(code_dict[ch] for ch in my_string)
    print('Закодированная строка:', code_str)
