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


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def __insert_left(self, new_node):
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
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def __insert_right(self, new_node):
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
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def insert_child(self, new_child):
        if new_child == self.root:
            return
        elif new_child > self.root:
            self.__insert_right(new_child)
        else:
            self.__insert_left(new_child)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj
        # Надо проверить, есть ли chold'ы и возможно их надо пересортировать
        right_child = self.get_right_child()
        left_child = self.get_left_child()
        if right_child:
            if self.get_root_val() > right_child.get_root_val():
                self.left_child = right_child
                self.right_child = None
        if left_child:
            if self.get_root_val() < left_child.get_root_val():
                self.right_child = left_child
                self.left_child = None

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # показать всех childs
    def view_childs(self):
        right_child = self.get_right_child()
        left_child = self.get_left_child()
        if right_child:
            print(f'Правый потомок у {self.get_root_val()}: {right_child.get_root_val()}')
            right_child.view_childs()
        if left_child:
            print(f'Левый потомок у {self.get_root_val()}: {left_child.get_root_val()}')
            left_child.view_childs()

if __name__ == "__main__":
    r = BinaryTree(8)
    # print(f'Значение root: {r.get_root_val()}')
    # print(f'Левый потомок: {r.get_left_child()}')
    # print(f'Правый потомок у {r.get_root_val()}: {r.get_right_child()}')
    # print()
    #
    # r.insert_child(40)
    # print(f'Левый потомок: {r.get_left_child()}')
    # print(f'Правый потомок у {r.get_root_val()}: {r.get_right_child().get_root_val()}')
    # print()
    #
    # r.insert_child(12)
    # print(f'Левый потомок: {r.get_left_child()}')
    # print(f'Правый потомок у {r.get_root_val()}: {r.get_right_child().get_root_val()}')
    # print(f'Правый потомок у {r.get_right_child().get_root_val()}: {r.get_right_child().get_right_child().get_root_val()}')
    # print()
    #
    # r.get_right_child().set_root_val(16)
    # print(f'Правый потомок у {r.get_root_val()}: {r.get_right_child().get_root_val()}')
    # print(f'Правый потомок у {r.get_right_child().get_root_val()}: {r.get_right_child().get_right_child().get_root_val()}')
    # print()
    # print()

    r.view_childs()
    r.insert_child(40)
    r.view_childs()
    print()

    r.insert_child(12)
    r.view_childs()
    print()

    r.get_right_child().set_root_val(16)
    r.view_childs()
    print('----------------------------------------------')
    print()

    r.set_root_val(17)
    r.view_childs()
    print()