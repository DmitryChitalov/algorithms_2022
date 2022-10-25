"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде


Написал 2 функции :
add_data_1 : вставляет данные в дерево :
 в конец справа - если значение больше максимального существующего;
  в конец слева - если значение меньше минимального существующего;
  внутрь дерева в нужном месте

find_val - ищет есть ли заданное значение в дереве,
обходит все ветви бинарного дерева

"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None




    def add_data_1(self, data):
        # если у узла нет правого потомка
        root_value = self.get_root_val()
        # print(f'root_value = {root_value}')

        if data < root_value:
            if self.left_child:                                     # left branch exist
                left_value = self.left_child.get_root_val()
                # print(f'left_value = {left_value}')
                if left_value < data < root_value:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(data)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                    return
                else:
                    BinaryTree.add_data_1(self.left_child, data)              # go down the tree to left
            else:                                                       # create left branch
                tree_obj = BinaryTree(data)
                self.left_child = tree_obj
                return

        if root_value < data:
            if self.right_child:                # right branch exist
                right_value = self.right_child.get_root_val()
                # print(f'right_value = {right_value}')
                if root_value < data < right_value:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(data)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                    return
                else:
                    BinaryTree.add_data_1(self.right_child, data)  # go down the tree to right
            else:                                       # create left branch
                tree_obj = BinaryTree(data)
                self.right_child = tree_obj
                return


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

    # def get_root_path(self):
        return root

    # Поиск узла
    def find_val(self, val, res=False):
        # print(f'get_root_val() = {self.get_root_val()}')
        if res:
            # print('a')
            return True
        elif self.get_root_val() == val:
            # print('b')
            return True
        if self.get_right_child():
            # print(f' get_right_child = {self.right_child.get_root_val()}')
            # root = self.get_right_child()
            # print(f'right root = {self.right_child}')
            # print(f'right value= {self.right_child.get_root_val()}')
            if BinaryTree.find_val(self.right_child, val, False):
                # print('c')
                return True
        if self.get_left_child():
            # print(f' get_left_child = {self.left_child.get_root_val()}')
            # print(f'left root = {self.left_child}')
            # print(f'left value= {self.left_child.get_root_val()}')
            if BinaryTree.find_val(self.left_child, val, False):
                # print('d')
                return True
        return False


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height,
        and horizontal coordinate of the root."""
        # No child.
        if self.right_child is None and self.left_child is None:
            line = '%s' % self.root
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + \
                   shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + \
                   shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = '%s' % self.root
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
                     '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) \
                      * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



# r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left(40)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(12)
# # print(r.get_right_child())
# # print(r.get_right_child().get_root_val())
# # r.get_right_child().set_root_val(16)
# # print(r.get_right_child().get_root_val())
# r.display()
# print(r.find_val(50))


int_lst = [20, 30, 10, 15, 45, 15, 60, 8, 7, 20, 95, 50, 80]

for i , el in enumerate(int_lst):
    if i == 0:
        r = BinaryTree(el)
    else:
        if r.find_val(el):
            print(f'Value {el} is already in tree')
            continue
        r.add_data_1(el)
        r.display()