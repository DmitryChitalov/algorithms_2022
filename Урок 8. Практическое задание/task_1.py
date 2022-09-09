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


# Подготовить таблицу вероятностей каждого символа
def findfrequency(chars):
    count = Counter(chars)
    sorted_elements = dict(sorted(count.items(), key=lambda item: item[1]))
    return sorted_elements


# Создать класс узла
class BinaryTree(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None


# Создать дерево Хаффмана
class HuffmanTree(object):
    def __init__(self, elements: dict):
        # Из словарей отсортированных по значению создаем самостоятельные объекты
        self.Leaf = [BinaryTree(key, value) for key, value in elements.items()]
        # Перебираем объекты пока не дойдем до корня
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda x: x.value, reverse=True)
            n = BinaryTree(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def code_generate(self, tree_data, length):
        if not tree:
            return
        elif tree_data.name:
            print(f'"{tree_data.name}" :', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print()
            return
        self.Buffer[length] = 0
        self.code_generate(tree_data.lchild, length + 1)
        self.Buffer[length] = 1
        self.code_generate(tree_data.rchild, length + 1)

    #  Вывод кодировки Хаффмана
    def get_code(self):
        self.code_generate(self.root, 0)


if __name__ == '__main__':
    text = r'He threw three free throws.'
    counted_elements = findfrequency(text)  # Сначала посчитали и отсортировали число вхождений
    tree = HuffmanTree(counted_elements)  # Сформировали из отсортированных значений, данные кодировки
    tree.get_code()  # Вывод данных
