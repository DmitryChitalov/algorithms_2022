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
# import random


class TreeLeftChildError(BaseException):
    pass


class TreeRightChildError(BaseException):
    pass


class TreeGetLeftChildError(BaseException):
    pass


class TreeGetRightChildError(BaseException):
    pass


class BinaryTree:
    __slots__ = ['root', 'left_child', 'right_child']

    def __init__(self, root_obj):
        # print(f"Root {root_obj}")
        # корень
        if isinstance(root_obj, int):
            self.root = root_obj
        else:
            raise ValueError
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def dictify(self):
        return {
            'root': self.root,
            'left_child': self.left_child.dictify() if self.left_child else None,
            'right_child': self.right_child.dictify() if self.right_child else None,
        }

    # добавить левого потомка
    def insert_left(self, new_node):
        # проверяем условия бинарного дерева
        if new_node >= self.root:
            raise TreeLeftChildError

        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            # tree_obj.left_child = self.left_child

            # используем уже имеющуюся функцию в классе включающую валидацию
            tree_obj.insert_left(self.get_left_child())

            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # проверяем условия бинарного дерева
        if new_node <= self.root:
            raise TreeRightChildError

        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            # tree_obj.right_child = self.right_child

            # используем уже имеющуюся функцию в классе включающую валидацию
            tree_obj.insert_right(self.get_right_child())
    #
    #         self.right_child = tree_obj
    def __insert_right(self, new_node):
        self.right_child = BinaryTree(new_node)

    def __insert_left(self, new_node):
        self.left_child = BinaryTree(new_node)

    # def insert(self, root_tree, new_node):
    #     debug_root = root_tree.dictify()
    #     is_right_child = new_node >= root_tree.root
    #     tree_obj = root_tree.right_child if is_right_child else root_tree.left_child
    #     if tree_obj is None:
    #         if is_right_child:
    #             root_tree.__insert_right(new_node)
    #         else:
    #             root_tree.__insert_left(new_node)
    #     else:
    #         is_right_child = new_node >= tree_obj.root
    #         new_obj = BinaryTree(new_node)
    #         if is_right_child:
    #             new_obj.__insert_right(new_node)
    #             tree_obj.left_child = new_obj
    #         else:
    #             new_obj.__insert_left(new_node)
    #             tree_obj.right_child = new_obj

    #        # self.insert(tree_obj, new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        # if not self.right_child:
        #     raise TreeGetRightChildError
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        # if not self.left_child:
        #     raise TreeGetLeftChildError
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # @staticmethod
    # def draw_childs(tree):
    #     while (tree.get_left_child() if tree else None is not None):
    #         print(f"{tree.root}")
    #         print(f"{tree.left_child.root if tree.left_child else None}-"
    #               f"{tree.right_child.root if tree.right_child else None}")
    #         tree = tree.get_left_child()
    #
    # def draw(self):
    #     left_child = self.left_child.root if self.left_child else None
    #     right_child = self.right_child.root if self.right_child else None
    #     print(f"{self.root} - {left_child}-{right_child}")
    #     print("Child Left")
    #     self.draw_childs(self.get_left_child())
    #     print("Child Right")
    #     self.draw_childs(self.get_right_child())


r = BinaryTree(8)
# r.set_root_val(100)
print(r.get_root_val())
print(r.get_left_child())

# r.insert_left(40)
# print(r.insert(40))
print(r.get_left_child())
print(r.get_left_child().get_root_val())
# r.insert_right(12)
# print(r.insert(12))
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
# r.draw()

# test_arr = [random.randint(0, 100) for x in range(0, 10)]
# test_arr = [20, 16, 2, 45, 36, 62, 61, 24, 80, 39]
# print(test_arr)
# tree_dom = BinaryTree(test_arr[0])
# # for x in range(1, len(test_arr)):
# # tree_dom.insert(tree_dom, 20)
# tree_dom.insert(tree_dom, 16)
# tree_dom.insert(tree_dom, 45)
# tree_dom.insert(tree_dom, 2)
# print(tree_dom.dictify())

"""
    Добавлены исключения, валидация для проверки условий бинарного дерева.
    Значение добавляемое будет отклонено, и будет выброшено исключение.
    Также добавлен __slots__ в класс.
"""
