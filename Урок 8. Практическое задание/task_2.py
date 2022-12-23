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


# ошибка для неправильной вставки в бинароное дерево
class BinaryTreePlacementError(Exception):
    'That is not where this node should go'
    pass

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            # если левый элемент больше корня, то возвращаем ошибку
            if new_node > self.root:
                raise BinaryTreePlacementError
            # если у узла нет левого потомка
            elif self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                try:
                    # если новый узел меньше его будущего левого ребенка, то возвращаем ошибку
                    if tree_obj.root < self.left_child.get_root_val():
                        raise BinaryTreePlacementError
                    else:
                        # и спускаем имеющегося потомка на один уровень ниже
                        tree_obj.left_child = self.left_child
                        self.left_child = tree_obj
                except BinaryTreePlacementError:
                    print('Exception occured - wrong placement in binary tree')
        except BinaryTreePlacementError:
            print('Exception occured - wrong placement in binary tree')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            # если правый элемент меньше корня возвращаем ошибку
            if new_node < self.root:
                raise BinaryTreePlacementError
            # если у узла нет правого потомка
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                try:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # если новый узел больше его будущего правого ребенка, то возвращаем ошибку
                    if tree_obj.root > self.right_child.get_root_val():
                        raise BinaryTreePlacementError
                    else:
                        # и спускаем имеющегося потомка на один уровень ниже
                        tree_obj.right_child = self.right_child
                        self.right_child = tree_obj
                except BinaryTreePlacementError:
                    print('Exception occured - wrong placement in binary tree')
        except BinaryTreePlacementError:
            print('Exception occured - wrong placement in binary tree')

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


    # метод самого простого отображения дерева
    def get_full_tree(self):
        if self.left_child == None and self.right_child == None:
            return ''
        else:
            description = f'For root {self.root}\n'
            if self.left_child != None:
                description += f'\tleft child is {self.left_child.get_root_val()}\n'
            if self.right_child != None:
                description += f'\tright child is {self.right_child.get_root_val()}\n'
            left_tree = self.left_child.get_full_tree() if self.left_child != None else ''
            right_tree = self.right_child.get_full_tree() if self.right_child != None else ''
            return f'{description} {left_tree} {right_tree}'



r = BinaryTree(9)
print(f'Root of binary tree - {r.get_root_val()}')
print(f'Right child of root - {r.get_left_child()}')
r.insert_left(40)
r.insert_left(3)
print(f'Left child of root - {r.get_left_child()}')
print(f'Left child value of root - {r.get_left_child().get_root_val()}')
r.insert_left(5)
r.insert_left(2)
r.insert_left(7)
r.insert_right(12)
r.get_left_child().insert_right(8)
print(r.get_left_child().get_left_child().get_root_val())
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert_right(14)
print(r.get_full_tree())

'''
Добавила ошибку BinaryTreePlacementError, ее вызываю в insert_right и insert_right. Не придумала, как реализовать аналогичную проверку для set_root_val, сейчас можно там поменять узел так, чтобы не соблюдались правила бинарного дерева

Результат для кода

Root of binary tree - 9
Right child of root - None
Exception occured - wrong placement in binary tree
Left child of root - <__main__.BinaryTree object at 0x7fe0a4b3c8b0>
Left child value of root - 3
Exception occured - wrong placement in binary tree
5
<__main__.BinaryTree object at 0x7fe0a4a816d0>
12
16
For root 9
	left child is 7
	right child is 14
 For root 7
	left child is 5
	right child is 8
 For root 5
	left child is 3
    For root 14
	right child is 16

Возвращаются две ошибки для строк:
- r.insert_left(40)
- r.insert_left(2)
'''
