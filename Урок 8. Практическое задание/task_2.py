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


class ChildError(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def validate_left_node(self, new_node):
        if new_node >= self.root:
            raise ChildError('Левый ребенок должен меньше родителя')

    def validate_right_node(self, new_node):
        if new_node < self.root:
            raise ChildError('Правый ребенок должен быть больше или равен родителю')

    # добавить левого потомка
    def insert_left(self, new_node):

        try:
            self.validate_left_node(new_node)
        except ChildError as err:
            print(f'insert_left({new_node}): {err}')
            return self.insert_right(new_node)

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
            if self.left_child.root < new_node:
                tree_obj.left_child = self.left_child
            else:
                tree_obj.right_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):

        try:
            self.validate_right_node(new_node)
        except ChildError as err:
            print(f'insert_right({new_node}): {err}')
            return self.insert_left(new_node)

        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if self.right_child.root < new_node:
                tree_obj.left_child = self.right_child
            else:
                tree_obj.right_child = self.right_child
            self.right_child = tree_obj

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

    # жалкая попытка нарисовать дерево
    def show_tree(self, tree_string=''):
        # начинаем собирать строку. Если метод вызван с пустой строкой - записываем корень
        if tree_string == '':
            tree_string = f'{self.root}\n'

        lc = self.left_child  # левый ребенок
        rc = self.right_child  # правый ребенок
        children = [lc, rc]
        flag = True  # здесь будем отмечать найдены ли дети
        while flag is True:
            temp = []  # сюда будем собирать массив детей следующего уровня
            flag = False
            for child in children:
                if child:  # если ребенок есть, то есть не None
                    tree_string += f'{child.root} '  # записываем его в строку
                    lc = child.left_child
                    rc = child.right_child
                    # записываем детей в массив
                    temp.append(lc)
                    temp.append(rc)
                    # и если хоть один не None: меняем флаг
                    if lc or rc:
                        flag = True
                else:  # если ребенка нет, то и на следующем уровне детей не будет
                    temp.append(None)
                    temp.append(None)
                    tree_string += '. '  # тут могли бы быть дети ;(
            if flag:  # если хоть один ребёнок на следующем уровне есть:
                tree_string += '\n'  # преходим не следующую строку
                children = temp  # записываем массив в children

        # строчка готова. можно посмотреть в неотформатированном виде
        # print(tree_string)

        # попробуем вывести в более понятном виде
        # очень приблизительно. Если будут большие числа, то будет некрасиво
        # в children сейчас самый нижний ряд, соответственно самый длинный
        max_len = len(children) * 4
        for one_string in tree_string.split('\n'):  # разбиваем на строки и проходим по каждой
            temp_str = ''
            one_str_splt = one_string.strip().split(' ')  # разбиваем строку по пробелам
            el_len = max_len // len(one_str_splt)  # количество символов на один элемент
            for el in one_str_splt:
                # каждый элемент дополняем пробелами до нужной длины, центруем и добавляем в строку
                temp_str += el.center(el_len, ' ')
            print(temp_str)  # выводим


r = BinaryTree(8)
r.insert_left(40)
r.insert_right(77)
r.insert_left(7)
r.insert_left(4)
r.insert_right(5)
r.insert_left(80)
r.insert_left(55)

r.show_tree()
