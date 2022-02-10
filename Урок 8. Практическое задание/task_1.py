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


# from lesson
def do_tree(obj):
    count_obj = Counter(obj)
    sort_obj = deque(sorted(count_obj.items(), key=lambda item: item[1]))
    if len(sort_obj) != 1:
        while len(sort_obj) > 1:
            weight = sort_obj[0][1]+sort_obj[1][1]
            comb = {0: sort_obj.popleft()[0], 1: sort_obj.popleft()[0]}
            for i, cnt in enumerate(sort_obj):
                if weight > cnt[1]:
                    continue
                else:
                    sort_obj.insert(i, (comb, weight))
                    break
            else:
                sort_obj.append((comb, weight))
    else:
        weight = sort_obj[0][1]
        comb = {0: sort_obj.popleft()[0], 1: None}
        sort_obj.append((comb, weight))
    return sort_obj[0][0]


dict_for_path = dict()


def pathfinder(tr, path=''):
    if not isinstance(tr, dict):
        dict_for_path[tr] = path
    else:
        pathfinder(tr[0], path=f'{path}0'),
        pathfinder(tr[1], path=f'{path}1')


# my
def count(txt):
    cnt = Counter(txt)
    return cnt


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    my_dict = {}

    def __init__(self, weights):
        self.Leaf = [Node(k, v) for k, v in weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def do_tree(self, tr, length):
        node = tr
        if not node:
            return
        elif node.name:
            res = ''
            for i in range(length):
                res += str(self.Buffer[i])
            self.my_dict[node.name] = res
            return
        self.Buffer[length] = 0
        self.do_tree(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.do_tree(node.rchild, length + 1)

    def get_code(self):
        self.do_tree(self.root, 0)
        print(self.my_dict)


if __name__ == '__main__':
    text = 'алгоритм Хаффмана!'
    print("from lesson")
    pathfinder(do_tree(text))
    print(dict_for_path)
    print('from me')
    tree = HuffmanTree(count(text))
    tree.get_code()
