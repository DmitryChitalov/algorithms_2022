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


from collections import deque


class MyNode:
    # Класс узлов дерева
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


def search(node, path='',):
    # Функция возвращающая крайнюю правую букву в листе дерева и путь до нее
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


our_string = input('Введите строку для кодирования: ')

our_string_dict = {}
for i in our_string:
    if i not in our_string_dict:
        our_string_dict[i] = 1
    else:
        our_string_dict[i] += 1

node_list = deque([MyNode(our_string_dict[i], i) for i in our_string_dict])

for i in range(len(our_string_dict)-1):

    node_list = deque(sorted(node_list, key=lambda node: node.value))

    first_el = node_list.popleft()
    second_el = node_list.popleft()

    new_node = MyNode(first_el.value + second_el.value, left=first_el, right=second_el)

    node_list.appendleft(new_node)

tree = node_list[0]

table = {}
for _ in range(len(our_string_dict)):
    k = search(tree)
    table[k[0]] = k[1]
del tree

print(f'Оригинальная строка:\n{our_string}')

print('Кодированная строка:')
for char in our_string:
    print(table[char], end=' ')
