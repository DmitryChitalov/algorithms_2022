"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


# Класс, описывающий узел дерева
class Node:
    def __init__(self, data=None, left=None, right=None):
        # корень
        self.data = data
        # левый потомок
        self.left = left
        # правый потомок
        self.right = right

    def __repr__(self):
        return f'Node[{self.data:^5}]'

    def __str__(self):
        return 'Node [' + str(self.data) + ']'


# Класс, описывающий дерево
class BinaryTree:
    def __init__(self, root_obj=None):
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # корень
        if root_obj is None:
            self.root = root_obj
        else:
            self.root = self.new_node(root_obj)

    # функция для добавления узла в дерево
    @staticmethod
    def new_node(data):
        temp = Node(0, None, None)
        temp.data = data
        return temp

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)

            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1

    # функция для распечатки элементов на определённом уровне дерева
    def print_given_level(self, root, level, ltr):
        if root is None:
            return
        if level == 1:
            print("%d " % root.data)
        elif level > 1:
            if ltr:
                self.print_given_level(root.left, level - 1, ltr)
                self.print_given_level(root.right, level - 1, ltr)
            else:
                self.print_given_level(root.right, level - 1, ltr)
                self.print_given_level(root.left, level - 1, ltr)

    # функция для распечатки дерева
    def print_level_order(self):
        h = self.height(self.root)
        i = 1
        ltr = 1
        while i <= h:
            self.print_given_level(self.root, i, ltr)
            i += 1

    # функция для вычисления ширины дерева
    def get_max_width(self, root):
        max_width = 0
        i = 1
        # width = 0
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_width:
                max_width = width
            i += 1

        return max_width

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(
                root.right, level - 1)

    def contains(self, node, value):
        """метод проверки наличия узла в дереве"""
        if node is None:
            return None
        elif node.data == value:
            return True
        elif node.data > value:
            return self.contains(node.left, value)
        else:
            return self.contains(node.right, value)

    def get_node(self, node, value):
        """метод получение узла"""
        if node.data == value:
            return node
        elif node.data > value:
            return self.get_node(node.left, value)
        else:
            return self.get_node(node.right, value)
    # *************************************************************************

    def get_root_val(self):
        """метод доступа к корню"""
        return self.root

    def set_root_val(self, obj):
        """метод установки коря"""
        self.root.data = obj

    def get_left_child(self):
        """метод доступа к левому потомку"""
        return self.left_child

    def get_right_child(self):
        """метод доступа к правому потомку"""
        return self.right_child

    def insert_left(self, data):
        """добавить левого потомка"""
        try:
            if data > self.root.data:
                raise InsertLeftError(f"Потомок слева (Node [{data}]) не может "
                                      f"быть больше корня ({self.root}) !\n"
                                      f"Операция не выполнена!")
        except InsertLeftError as ex:
            print(ex)
            return

        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево и
            # формируется новое поддерево
            self.root.left = self.new_node(data)
        else:  # если у узла есть левый потомок
            # тогда вставляем новый узел
            tree_obj = self.new_node(data)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, data):
        try:
            if data < self.root.data:
                raise InsertRightError(f"Потомок справа (Node [{data}]) не может "
                                       f"быть меньше корня ({self.root}) !\n"
                                       f"Операция не выполнена!")
        except InsertRightError as ex:
            print(ex)
            return

        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево и
            # формируется новое поддерево
            self.root.right = self.new_node(data)
        else:  # если у узла есть правый потомок
            # тогда вставляем новый узел
            tree_obj = self.new_node(data)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj


class InsertLeftError(Exception):
    """Класс исключения при вставке левого потомка"""

    def __init__(self, *args):
        super().__init__(*args)
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        """Вывод сообщения об ошибке в консоли"""
        return f"Ошибка: {self.msg}"


class InsertRightError(Exception):
    """Класс исключения при вставке правого потомка"""

    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        """Вывод сообщения об ошибке в консоли"""
        return f"Ошибка: {self.msg}"


def first_test():
    # создание дерева
    t = BinaryTree()
    # добавление коря
    t.root = t.new_node(8)
    # добавление узлов в дерево
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

    print('-' * 60)
    t.print_level_order()
    print(f'корень: {t.root}')
    print(f'высота: {t.height(t.root)}')
    print(f'ширина: {t.get_max_width(t.root)}')
    if t.contains(t.root, 4):
        print(f"left_child для Node(4): {t.get_node(t.root, 4).left}")
        print(f"rigth_child для Node(4): {t.get_node(t.root, 4).right}")


def second_test():
    print('-' * 60)
    r = BinaryTree(7)
    assert id(r.root) == id(r.get_root_val())
    print(f'корень: {r.get_root_val()}')
    print(f'адрес left_child корня: {r.get_left_child()}')
    r.insert_left(40)  # попытка неверного размещения потомка
    print(f'адрес left_child корня: {r.get_left_child()}')
    r.insert_left(5)
    r.insert_right(9)
    print(f'корень: {r.root}')
    print(f'высота: {r.height(r.root)}')
    print(f'ширина: {r.get_max_width(r.root)}')
    r.print_level_order()


def main():
    first_test()
    second_test()


if __name__ == "__main__":
    main()
