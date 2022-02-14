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

from collections import Counter
from collections import deque

"""
класс Tree состоит из узлов и потомков

"""


class Tree:

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None


class HoffmanCode:

    def __init__(self, string):  # текстовая строка, которая будем кодироваться
        self.string = string

        self.order = deque(sorted(Counter(string).items(), key=lambda x: x[1]))  # создание отсортированной по частоте
        # символов очереди из кортежей (символ, частота)
        self.tree = self.fill_tree()  # сборка дерева
        self.code_table = dict()  # создание и заполнение таблицы соответствия символов и кодов
        self.fill_code_table(self.tree)  # получение экземпляра класса
        # print(type(self.tree))

    def fill_tree(self):

        while len(self.order) > 1:  # Вместо словаря, как в примере, используем
            # объекты класса Tree, которые соберём один объект этого класса
            left = self.order.popleft()  # изьятие  двух крайних левых элементов из очереди
            right = self.order.popleft()
            node = Tree(left[1] + right[1])  # формируем из них дерево
            node.left_child = left[0]
            node.right_child = right[0]

            for idx, element in enumerate(self.order):  # выбираем, куда вставить дерево
                if element[1] < node.root:
                    continue
                else:
                    self.order.insert(idx, (node, node.root))
                    break
            else:
                self.order.append((node, node.root))  # добавляем итоговый элемент

        return self.order[0][0]  # Получает само дерево

    """
    рекурсивно заполняем таблицу кодов по принципу:
    если аргумент tree - символ (строка), добавляем в словарь кодов эту строку и получившееся кодовое значение,
    если аргумент tree не символ (то есть дерево), берём его потомков и передаём их в функцию,
    а к передаваемому вместе с потомками кодовому значению добавляем 0 или 1
    """

    def fill_code_table(self, tree, value=''):

        if isinstance(tree, str):
            self.code_table[tree] = value
            return
        self.fill_code_table(tree.left_child, f'{value}0')
        self.fill_code_table(tree.right_child, f'{value}1')

    def encode(self):
        result = (self.code_table[letter] for letter in self.string)  # формируем строку из кодов символов
        # с помощью генератора
        return ' '.join(result)


if __name__ == '__main__':

    str_1 = HoffmanCode('beep boop beer!')

    str_2 = HoffmanCode('New line cinema')

    for key, val in str_1.code_table.items():
        print(key, val, )
    print('\n', 'beep boop beer!', '\n', str_1.encode(), '\n')

    for key, val in str_2.code_table.items():
        print(key, val)
    print('\n', 'New line cinema', '\n', str_2.encode(), '\n')
