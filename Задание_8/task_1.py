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
from recordclass import recordclass

node_class = recordclass('node_class', ('parent', 'value', 'left', 'right'))

def value_insert(value, parent, side):
# создать узел с заданным значением, вставить в дерево на указанное место, вернуть узел
    node = node_class(parent=parent, value=value, left=None, right=None)
    if parent != None:
        if side == 0:
            if parent.left != None:
                node.left = parent.left
            parent.left = node
        elif side == 1:
            if parent.right != None:
                node.right = parent.right
            parent.right = node
    return node

def haffman_tree(s):
    node_list = [] # список узлов дерева
# создать список элементов из кортежей (символ, количество) в порядке убывания количества
    count = Counter(s)
    item_list = sorted(count.items(), key=lambda item: item[1], reverse=True)
# обработать крайние случаи строки    
    if len(item_list) == 0:
        return node_list
    elif len(item_list) == 1:
        item0 = item_list.pop()
        node = value_insert(parent=None, value=(item0[0], item0[1]), side=0)
        node_list.append(node)
        child = value_insert(parent=node, value=item0, side=0)
        node_list.append(child)
        return node_list
        
    while len(item_list) > 1:
# обработать пару последних элементов в списке:
# создать узел-родитель по обрабатываемым элементам и добавить его в список узлов дерева
        item0 = item_list.pop()
        item1 = item_list.pop()
        value = item0[0] + item1[0] 
        weight = item0[1] + item1[1]
        node = value_insert(parent=None, value=(value, weight), side=0)
        node_list.append(node)
    
# если обрабатываемый элемент - кортеж (символ, количество),
# то создать по нему узел под узлом-родителем и добавить его в список узлов дерева,
# иначе - элемент связан с ранее созданным узлом, установить узел элемента под узел-родитель
        if len(item0) == 2:
            child = value_insert(parent=node, value=item0, side=0)
            node_list.append(child)
        else:
            item0[2].parent = node
            node.left = item0[2]

        if len(item1) == 2:
            child = value_insert(parent=node, value=item1, side=1)
            node_list.append(child)
        else:
            item1[2].parent = node
            node.right = item1[2]
            
# определить позицию в списке элементов для вставки в него нового элемента, связанного с узлом-родителем
# поместить в список элементов кортеж (строка, количество, узел-родитель)
        for index, item in enumerate(item_list):
            if item[1] < weight:
                item_list.insert(index, (value, weight, node))
                break
        else:
            item_list.append((value, weight, node))
            
    return node_list

def tree_to_dict(node_list):
# по дереву построить словарь: ключ - символ, значение - код
    char_dict = dict()
# отобрать узлы - символы, они не имеют детей
    for node in [node for node in node_list if node.left == None and node.right == None]:
        char = node.value[0]
        code = ''
# подниматься вверх до корня, на каждом уровне добавлять в начало кода 0, если пришёл на уровень слева и 1 - если справа
        parent = node.parent
        while parent != None:
            if parent.left == node:
                code = '0' + code
            else:
                code = '1' + code
            node = parent
            parent = node.parent
# добавить сформированный код в словарь            
        char_dict[char] = code
    return char_dict

s = 'beep boop beer!'
#s = 'fa'
#s = 'f'
#s = ''
node_list = haffman_tree(s)
char_dict = tree_to_dict(node_list)
print(char_dict)

for char in s:
    print(char_dict[char], end=' ')
print()

# Замечание
# Искомый словарь (ключ - символ, значение - код) быстрее и проще получать другим алгоритмом, без построения дерева.
