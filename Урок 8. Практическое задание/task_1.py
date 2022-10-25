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
class MyNode:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


# Функция возвращающая крайнюю правую букву в листе дерева и путь до нее
def search(node, path=''):
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


# Строка для перевода
s = 'ехал грека через реку'
# s = input('Введите строку для кодирования:\n')

# Собираем словарь из встречающихся  букв и их количества
s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1

# Собираем очередь из узлов
node_list = deque([MyNode(s_dict[i], i) for i in s_dict])

# Собираем само дерево
for i in range(len(s_dict) - 1):
    node_list = deque(sorted(node_list, key=lambda node: node.value))

    first_el = node_list.popleft()
    second_el = node_list.popleft()

    new_node = MyNode(first_el.value + second_el.value, left=first_el, right=second_el)

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
