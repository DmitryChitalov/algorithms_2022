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


class TreeBuilder:
    def __init__(self, some_text):
        self.some_text = some_text
        self.array = self.huff_count()
        self.root = self.build_tree()

    def huff_count(self):
        return Counter(self.some_text).most_common()

    def build_tree(self):
        while self.array:
            value_1 = self.array.pop()
            value_2 = self.array.pop()
            if not isinstance(value_1[0], HuffmanNode):
                node_1 = HuffmanNode(value_1, route='0')
            else:
                node_1 = value_1[0]
            if not isinstance(value_2[0], HuffmanNode):
                node_2 = HuffmanNode(value_2, route='1')
            else:
                node_2 = value_2[0]
            parent_weight = node_1.get_weight() + node_2.get_weight()
            parent = HuffmanNode(((node_1, node_2), parent_weight), node_1, node_2)
            if len(self.array) == 0:
                return parent
            for i in range(len(self.array) - 1, -1, -1):
                if self.array[i][1] >= parent_weight:
                    self.array.insert(i + 1, (parent, parent_weight))
                    break
                if i == 0:
                    self.array.insert(0, (parent, parent_weight))
                    break

    # метод для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left_child)
            right_height = self.height(node.right_child)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    # метод для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            rv = root.value
            if not isinstance(rv, tuple):
                print(f'({rv}, {root.route})', end='')
            else:
                print('Node  ', end='')
        elif level > 1:
            self.print_given_level(root.left_child, level - 1)
            self.print_given_level(root.right_child, level - 1)

    # метод для распечатки дерева
    def print_tree(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            print('-' * 30)
            i += 1

    # метод для построения словаря
    def find_routes(self, node=None, route=''):
        values_dict = {}
        if not node:
            node = self.root
        if isinstance(node.value, str):
            return {node.value: route}

        lc = node.left_child
        lc_route = f'{route}0'
        rc = node.right_child
        rc_route = f'{route}1'

        left_result = self.find_routes(lc, lc_route)
        values_dict.update(left_result)
        right_result = self.find_routes(rc, rc_route)
        values_dict.update(right_result)

        return values_dict


class HuffmanNode:
    def __init__(self, node, left_child=None, right_child=None, route=''):
        self.value = node[0]
        self.weight = node[1]
        self.route = route
        self.left_child = left_child
        self.right_child = right_child

    def get_weight(self):
        return self.weight


if __name__ == '__main__':
    text = 'beep boop beer!'

    h_b = TreeBuilder(text)

    h_b.print_tree(h_b.root)
    # Node
    # ------------------------------
    # Node
    # Node
    # ------------------------------
    # (b, 0)
    # Node
    # Node(e, 1)
    # ------------------------------
    # (, 0)(p, 1)
    # Node(o, 1)
    # ------------------------------
    # (!, 0)(r, 1)
    # ------------------------------
    print()

    print(h_b.find_routes())
    # {'b': '00', ' ': '010', 'p': '011', '!': '1000', 'r': '1001', 'o': '101', 'e': '11'}
