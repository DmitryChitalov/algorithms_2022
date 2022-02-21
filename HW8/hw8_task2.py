"""
Из сделанного - обработка базовых исключений и перестановка элементов при неправильном заполнении
на первом этапе.
Не успел обработать ряд случаев на самом деле, много еще надо добаратывать
К примеру, проверку вставки в правую ветку узла левой ветки
"""


class WrongValues(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def check_left_value(self):
        """
        работает лишь для первого узла, не успел реализовать для остальных узлов
        """
        try:
            if self.left_child.root > self.root:
                raise WrongValues('Корень оказался меньше левого потомка')
            elif self.left_child.root == self.root:
                raise WrongValues('Корень оказался равен левому потомку. Ошибка')
        except WrongValues as err:
            print(err)
            self.root, self.left_child = self.left_child.root, BinaryTree(self.root)
        else:
            print('Значения корректны')

    def check_right_value(self):
        try:
            if self.right_child.root < self.root:
                raise WrongValues('Корень оказался больше правого потомка')
            elif self.right_child.root == self.root:
                raise WrongValues('Корень оказался равен правому потомку. Ошибка')
        except WrongValues as err:
            print(err)
            self.root, self.right_child = self.right_child.root, BinaryTree(self.root)
            # print('Произошла смена местами', self.root, self.right_child.root)
        else:
            print('Значения корректны')


    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            self.check_left_value()  # проверка значений а также их смена
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            try:
                if tree_obj.root < self.left_child.root:  # вставки не будет, останется нулл
                    raise WrongValues('Ошибка: вводимое число окажется  меньше левого потомка')
                else:
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            except WrongValues as err:
                print(err)


    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            self.check_right_value()
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            try:
                if tree_obj.root > self.right_child.root:
                    # вставки не будет, останется нулл
                    raise WrongValues('Ошибка: вводимое число окажется больше правого потомка '
                                      'либо должно находиться в другой ветке')
                else:
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            except WrongValues as err:
                print(err)


    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
r.insert_left(20)
r.insert_right(12)
# print(r.get_root_val()) # т к я их переставил на первом этапе то корень теперь 12
# print(r.left_child.get_root_val())  # 8
# print(r.right_child.get_root_val())  # 20
r.insert_left(1)
print(r.left_child.left_child)  # NONE т к неправильный ввод
r.insert_left(10)
print(r.left_child.root)  # стал 10, 8 - теперь левый потомок
r.insert_right(25)
r.insert_right(15)
print(r.right_child.root)
r.insert_right(1)  # должно находиться в другой ветке
