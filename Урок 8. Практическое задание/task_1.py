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


# Класс узлов дерева
class Node:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


# Функция возвращающая крайнюю правую букву в листе дерева и путь до нее
def search(Node, path=''):
    if Node.letter is not None:
        Node.value = 0
        return Node.letter, path
    if Node.right is not None and Node.right.value != 0:
        spam = search(Node.right, path=f'{path}1')
        if Node.right.value == 0 and Node.left.value == 0:
            Node.value = 0
        return spam
    if Node.left is not None and Node.left.value != 0:
        spam = search(Node.left, path=f'{path}0')
        if Node.right.value == 0 and Node.left.value == 0:
            Node.value = 0
        return spam


# Строка для перевода
s = input('Введите строку для кодирования:\n')

# Собираем словарь из встречающихся  букв и их количества
s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1

# Собираем очередь из узлов
node_list = deque([Node(s_dict[i], i) for i in s_dict])

# Собираем само дерево
for i in range(len(s_dict) - 1):
    node_list = deque(sorted(node_list, key=lambda node: node.value))

    first_el = node_list.popleft()
    second_el = node_list.popleft()

    new_node = Node(first_el.value + second_el.value, left=first_el, right=second_el)

    node_list.appendleft(new_node)

tree = node_list[0]

# Получаем таблицу перевода
table = {}
for _ in range(len(s_dict)):
    k = search(tree)
    table[k[0]] = k[1]
del tree

print(f'Оригинальная строка:\n{s}')

# Переводим
print('Кодированная строка:')
for char in s:
    print(table[char], end=' ')