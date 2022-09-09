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


class InvalidLeftInsertion(Exception):
    def __init__(self, new_node, root):
        self.message = f'Вставляемый влево объект "{new_node}" больше или равен корневому ("{root}")'

    def __str__(self):
        return self.message


class InvalidRightInsertion(Exception):
    def __init__(self, new_node, root):
        self.message = f'Вставляемый вправо объект "{new_node}" меньше корневого ("{root}")'

    def __str__(self):
        return self.message


class InvalidRootChange(Exception):
    def __init__(self, new_node):
        self.message = f'Невозможно заменить корень на объект "{new_node}"'

    def __str__(self):
        return self.message


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def _check_insert_left(self, new_node):
        """Проверка вставки влево"""
        root = self.get_root_val()
        if new_node >= root:
            raise InvalidLeftInsertion(new_node, root)

    def _check_insert_right(self, new_node):
        """Проверка вставки вправо"""
        root = self.get_root_val()
        if new_node < root:
            raise InvalidRightInsertion(new_node, root)

    def _check_change_root(self, new_root):
        """Проверка изменения корня"""
        left_child = self.get_left_child()
        right_child = self.get_right_child()
        if left_child and right_child is None:
            if new_root < left_child:
                raise InvalidRootChange(new_root)
        elif right_child and left_child is None:
            if new_root > right_child:
                raise InvalidRootChange(new_root)
        elif left_child and right_child:
            if left_child > new_root > right_child:
                raise InvalidRootChange(new_root)

    # добавить левого потомка
    def insert_left(self, new_node):
        self._check_insert_left(new_node)
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево,
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
        self._check_insert_right(new_node)
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево,
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
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
        self._check_change_root(obj)
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':

    try:
        r = BinaryTree(8)
        print(r.get_root_val())
        print(r.get_left_child())
        r.insert_right(12)
        print(r.get_right_child())
        print(r.get_right_child().get_root_val())
        r.get_right_child().set_root_val(16)
        print(r.get_right_child().get_root_val())
        print(r)
        r.insert_left(40)
        print(r.get_left_child())
        print(r.get_left_child().get_root_val())
    except InvalidLeftInsertion as e:
        print(e)
    except InvalidRightInsertion as e:
        print(e)
    except InvalidRootChange as e:
        print(e)
