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


class NodeValueError(Exception):
    """Исключение для ошибок валидации данных узла дерева."""


class Node:
    """
    Представление вершины (узла) бинарного дерева.
    Содержит данные узла, а также ссылки на левого и правого потомков.
    """

    def __init__(self, data, left=None, right=None):
        # Валидация данных через статический метод
        self.validate_data(data, left, right)

        self.data = data
        self.left_child = left
        self.right_child = right

    @staticmethod
    def validate_data(data, left, right):
        """Валидация входных данных узла."""
        # Проверка, что data - целое число
        if not isinstance(data, int):
            raise NodeValueError(f'Значение "{data}" должно быть целым числом.')

        # Проверка, что left и right либо None, либо экземпляры Node
        if left is not None and not isinstance(left, Node):
            raise NodeValueError("Левый потомок должен быть экземпляром Node или None.")
        if right is not None and not isinstance(right, Node):
            raise NodeValueError("Правый потомок должен быть экземпляром Node или None.")

    # метод доступа к правому потомку
    def get_right_child(self):
        """Возвращает правого потомка."""
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        """Возвращает левого потомка."""
        return self.left_child

    # метод доступа к корню
    def get_root_val(self):
        """Возвращает значение узла (корня)."""
        return self.data


class Tree:
    """
    Представление бинарного дерева и операции с ним.
    Включает добавление узлов, удаление, поиск и вывод дерева.
    """

    def __init__(self):
        self.root = None

    # Рекурсивный поиск вставляемого узла LNR
    def __find(self, node, parent, value):
        """
        Рекурсивный поиск узла в дереве.
        :param node: текущий узел для поиска.
        :param parent: родитель узла.
        :param value: значение узла, которое мы ищем.
        :return: найденный узел, его родитель и флаг нахождения.
        """
        if node is None:
            return None, parent, False

        # Если найден узел с таким значением, возвращаем его, родитель и флаг нашли ли вершину
        if value == node.data:
            return node, parent, True

        # Идем по левой ветви
        if value < node.data:
            if node.left_child:
                # Если есть левая ветвь, но нет правой - создаём её.
                return self.__find(node.left_child, node, value)

        # Идем по правой ветви
        if value > node.data:
            if node.right_child:
                # Если есть правая ветвь, но нет левой - создаём её.
                return self.__find(node.right_child, node, value)

        return node, parent, False

    # Добавление элементов
    def append(self, obj):
        """
        Добавляет новый узел в дерево.
        :param obj: узел для добавления.
        :return: добавленный узел.
        """
        if self.root is None:
            self.root = obj
            return obj

        # Ищем место для вставки
        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left_child = obj
            else:
                s.right_child = obj

        return obj

    # Вывод дерева в глубину
    def show_tree(self, node):
        """
        Вывод дерева в ширину (по уровням).
        :param node: корень дерева.
        """
        if node:
            self.show_tree(node.left_child)
            print(node.data)
            self.show_tree(node.right_child)

    # Удаление фрагмента
    def __del_leaf(self, s, p):
        """
        Удаляет лист (узел без детей).
        :param s: узел для удаления.
        :param p: родитель удаляемого узла.
        """
        if p.left_child == s:
            p.left_child = None
        elif p.right_child == s:
            p.right_child = None

    # Удаление узла с одним потомком
    def __del_one_child(self, s, p):
        """
        Удаляет узел с одним потомком.
        :param s: узел для удаления.
        :param p: родитель удаляемого узла.
        """
        if p.left_child == s:
            p.left_child = s.left_child if s.left_child else s.right_child
        elif p.right_child == s:
            p.right_child = s.left_child if s.left_child else s.right_child

    # Поиск минимальноё вершины узла
    def __find_min(self, node, parent):
        if node.left_child:
            return self.__find_min(node.left_child, node)
        return node, parent

    # Метод определения удаление узла
    def del_node(self, value):
        """
        Удаляет узел с заданным значением.
        :param value: значение узла для удаления.
        """
        s, p, fl_find = self.__find(self.root, None, value)

        if not fl_find:
            return None

        if s.left_child is None and s.right_child is None:
            self.__del_leaf(s, p)
        elif s.left_child is None or s.right_child is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right_child, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    # Вывод дерева обходом в ширину (по уровням).
    def show_wide_tree(self, node):
        """
        Вывод дерева в ширину (по уровням).
        :param node: корень дерева.
        """
        if node is None:
            print("Дерево пусто.")
            return

        # Очередь для обработки узлов по уровням
        queue = [node]

        while queue:
            # Временная очередь для текущего уровня
            next_queue = []
            level_values = []  # Список для значений текущего уровня

            # Проходим по текущему уровню
            for x in queue:
                level_values.append(x.data)  # Добавляем данные узла текущего уровня
                if x.left_child:
                    next_queue.append(x.left_child)  # Добавляем левого потомка в очередь
                if x.right_child:
                    next_queue.append(x.right_child)  # Добавляем правого потомка в очередь

            # Выводим все элементы на текущем уровне
            print(" ".join(map(str, level_values)))

            # Переходим к следующему уровню
            queue = next_queue


# Создаем дерево и добавляем в него элементы из массива "arr".
arr = [15, 9, 10, 8, 23, 21, 24]
t = Tree()
for element in arr:
    t.append(Node(element))

# Обходим получившиеся дерево.
t.show_wide_tree(t.root)
print('--------------------------------')
# Удаляем элемент выводим результат.
t.del_node(8)
t.show_wide_tree(t.root)
print('--------------------------------')
t.append(Node(8))
t.show_wide_tree(t.root)
print('--------------------------------')
# Проверяем, что меньшие корня дерева вставляются в левую ветку от корня дерева,
# правые соответственно.
arr = [11, 6, 22, 20]
for element in arr:
    t.append(Node(element))
t.show_wide_tree(t.root)
#
# t.append(Node(14))
# t.show_wide_tree(t.root)
