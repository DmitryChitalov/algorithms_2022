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
"""
В качестве самой главной оптимизации для данного класса, на мой взгляд, нужно работать не с быстродействием и 
оптимизацией памяти,  а с удобством использования данного класса. У нас есть жестко описанные правиласоставления 
бинарного дерева, так зачем же нам выбирать, куда вставлять новое значение: в право или лево? Метод add_new_node сделает
это автоматически!
Для проверки работоспособности нового метода исплользуем бинарное дерева из презентации урока:
              8
      4               12
  2       6       10      14
1   3   5   7   9   11  13  15
Что бы такое дерево получилось,  скармливаем методу add_new_node список  -> 
 ->  [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
для вывода дерева в консоль использую метод tree_list_create. Метод откровенно сырой и недоделанный, 
правдоподобную картину дерева он сможет выдать только для идеально - симметричного бинарного дерева. Так что за этот 
метод меня можно смело ругать, но доделать его до совершенства у меня сил пока нехватило.
P.S.
На мой скромный взгляд, insert_left и insert_right - работают в принципе некорректно, и пользуясь ими невозможно 
построить бинарное дерево из примера приведенного выше.
оригинальный кусок кода:
   def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
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
Согласно этому коду, если у корня есть потомок, то он всегда будет подменяться новым потомком, что протеворечит самой 
сути бинарного дерева. Новый кандидат должен сравниваться с корнем, а потом не подменять потомка, а сравниваться с ним,
что бы понять, куда ему ниже уйти в право или лево. А если пользоваться этими функциями, то будет не бинарное дерево,
а бинарный клин, с острием - корнем)) 
"""
from random import randint


class BinaryTreeError(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    tree_list = []

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
            if new_node < self.root:
                # если у узла нет левого потомка
                if self.left_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    self.left_child.add_new_node(new_node)

            else:
                raise BinaryTreeError(f'Неправильно выбран тип вставки нового узла!\n'
                                      f'Новый узел {new_node} больше или равен корню {self.root} нашего дерева!\n')
        except BinaryTreeError as tree_error:
            print(tree_error)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node >= self.root:
                # если у узла нет правого потомка
                if self.right_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                # если у узла есть правый потомок
                else:
                    self.right_child.add_new_node(new_node)
            else:
                raise BinaryTreeError(f'Неправильно выбран тип вставки нового узла!\n'
                                      f'Новый узел {new_node} меньше корня {self.root} нашего дерева!\n')
        except BinaryTreeError as tree_error:
            print(tree_error)

    def add_new_node(self, new_node):
        try:
            if isinstance(new_node, int) or isinstance(new_node, float):
                if new_node >= self.root:
                    self.insert_right(new_node)
                else:
                    self.insert_left(new_node)
            else:
                raise BinaryTreeError('Ошибка! Тип данных нового узла должен быть "int" или "float"!')
        except BinaryTreeError as tree_error:
            print(tree_error)

    # метод доступа к правому потомку
    @property
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    @property
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    @property
    def get_root_val(self):
        return self.root

    def show_tree(self):
        self.tree_list_create()
        for el in self.tree_list:
            print(el)

    def tree_list_create(self, step=0):
        self.tree_list.append([])
        self.tree_list[step].append(self.root)
        if self.left_child == None:
            self.tree_list.append([])
            self.tree_list[(step + 1)].append(' ')
        else:
            self.left_child.tree_list_create(step + 1)
        if self.right_child == None:
            self.tree_list.append([])
            self.tree_list[(step + 1)].append(' ')
        else:
            self.right_child.tree_list_create(step + 1)


r = BinaryTree(8)

num_list = [4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
r.add_new_node('sd')  # Генерируем появление ощибки и нашего класса - исключения
print(num_list)
for el in num_list:
    r.add_new_node(el)
r.show_tree()
