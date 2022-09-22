class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def insert_val(self, new_node):
        root = self.get_root_val()
        if new_node > root:
            self.insert_right(new_node)
        if new_node < root:
            self.insert_left(new_node)

    # добавить левого потомка
    def insert_left(self, new_node):
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
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок


@ @-77

, 6 + 84, 26 @ @
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
r.insert_val(40)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.get_left_child())

r.insert_val(10)
print(r.get_right_child())
print(r.get_right_child().get_root_val())  # 10 вместо 40
print(r.get_right_child().get_right_child())
print(r.get_right_child().get_right_child().get_root_val())  # 40 образовало новый вложенный корень
print(r.get_right_child().get_left_child())
print(r.get_left_child())
r.insert_val(1)
print(r.get_right_child())
print(r.get_left_child())
r.insert_val(15)
print(r.get_right_child().get_root_val())  # "15 вместо 10"
print(r.get_right_child().get_right_child())
print(r.get_right_child().get_right_child().get_root_val())  # 10
print(r.get_right_child().get_left_child())
print(r.get_left_child())