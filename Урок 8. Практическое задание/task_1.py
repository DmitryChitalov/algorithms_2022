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

"""
1) Максим Салтыков
2) Алгоритмы и структуры данных на Python. Базовый курс
3) дату старта курса(именно курса, а не обучения) 
4) номер урока 260931
5) номер профиля 4389736
"""


import collections

def get_freq(txt):
    counter = collections.Counter()
    for letter in txt:
        counter[letter] += 1
    return counter

def same_tree(a, b):
    if a is None and b is None:
        return 1
    elif a and b:
        return (
        a.value == b.value and
        same_tree(a.left, b.left) and
        same_tree(a.right, b.right)
        )
    return 0


class Tree:
    def __init__(self):
        self.root = None

    def new_node(self, value, left = None, right = None):
        return Node(value, left, right)

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1
        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) +\
                   self.get_width(root.right, level - 1)

    def print_given_level(self, root, level):
        if root is None:
            return

        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    def print_level_order(self, root):
        h = self.height(root)

        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __repr__(self):
        return f'Node[{self.value}]'


def countAllLetters(text):
    counter = collections.Counter()
    for letter in ''.join(chr(i) for i in range(128)):
        n = text.count(letter)
        if n!=0:
            counter[letter] = text.count(letter)
    return counter


def appendDicts(a,b):
    for el in b.keys():
        a[el] = b[el]
    return a


def recScan(node,n=''):
    codes = dict()
    res = []
    if type(node) is Node:
        letter,cods = recScan(node.left.value,n+'0')
        codes = appendDicts(codes,cods)
    """else:
        codes[node.left.value] = n + '0'
        pass"""
    if type(node) is Node:
        letter,cods = recScan(node.right.value,n+'1')
        codes = appendDicts(codes,cods)
    """else:
        codes[node.right.value] = n + '1'
        pass"""
    if type(node) is not Node:
        codes[node] = n
        return node,codes
    return node,codes

def haffman(text):
    counter = countAllLetters(text).items()
    counter = sorted(counter, key=lambda counter: counter[1])
    tree = Tree()
    nodes = []
    for i in range(len(counter)-1):
        nodes.append(Node(None))
        nodes[len(nodes)-1].left = Node(counter[0][0])
        nodes[len(nodes)-1].right = Node(counter[1][0])
        counter.append((nodes[len(nodes)-1],counter[0][1]+counter[1][1]))
        counter.pop(0)
        counter.pop(0)
        counter.sort(key=lambda counter: counter[1])
    encoding = recScan(nodes[len(nodes)-1])[1]
    #print(encoding)
    codedTxt = ''
    for i in range(len(text)):
        codedTxt = codedTxt + encoding[text[i]]
    return encoding, codedTxt

if __name__ == "__main__":
    #message = "122333444455555"
    #counter = get_freq(message)
    #print(counter)
    #q = queue
    #print(counter.most_common(len(counter))[len(counter)-1][1])

    #for i in range(len(counter)):
    #    weight = counter.most_common(len(counter))[len(counter)-1][1] + counter.most_common(len(counter))[len(counter)-2][1]
    #    left = counter.most_common(len(counter))[len(counter)-1][1]
    #    right = counter.most_common(len(counter))[len(counter)-2][1]
    #    tnode = Node(weight,left,right)
    #
    #    print(tnode)


    """t = Tree()
    t.root = t.new_node(8)
    t.root.left = t.new_node(4)
    t.root.right = t.new_node(12)
    t.root.left.left = t.new_node(2)
    t.root.left.right = t.new_node(6)
    t.root.right.left = t.new_node(10)
    t.root.right.right = t.new_node(14)
    t.root.left.left.left = t.new_node(0)
    t.root.left.left.right = t.new_node(3)
    t.root.left.right.left = t.new_node(5)
    t.root.left.right.right = t.new_node(7)
    t.root.right.left.left = t.new_node(9)
    t.root.right.left.right = t.new_node(11)
    t.root.right.right.left = t.new_node(13)
    t.root.right.right.right = t.new_node(15)
    t.print_level_order(t.root)
    print(f'высота: {t.height(t.root)}')
    print(f'ширина: {t.get_max_width(t.root)}')
    print(f'ширина: {t.print_given_level(t.root,2)}')"""
    ctr = countAllLetters("texttext2233kekeke1111111111111t8").items()
    print(sorted(ctr, key=lambda ctr: ctr[1]))
    ctr = sorted(ctr, key=lambda ctr: ctr[1])
    l = lambda i: ctr[i][1]
    #print(l())
    h = haffman("texttext2233kekeke1111111111111t8")
    print(h[0])
    print(h[1])









