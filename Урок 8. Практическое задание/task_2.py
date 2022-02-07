"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""
# Добавлен вывод дерева на печать
# Например:
#   _10__ 
#  /     \
#  8     12
# / \   /
# 7 9  11
# Добавлена проверка для релазации бинарного дерева поиска, 
# таким образом если встявляется неподходящее значение в ветку, 
# то будет пользовательское исключение.

class OrderError(ValueError):
    pass

ValueError
class BinaryTreeSearch:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if new_node >= self.root:
            raise OrderError(f'New node({new_node}) bigger or equal then parent({self.root})')

        new_tree_obj = self.__class__(new_node)
        if self.left_child == None:
            self.left_child = new_tree_obj
        else:
            if new_node > self.left_child.root:
                new_tree_obj.left_child = self.left_child
            else:
                new_tree_obj.right_child = self.left_child
            self.left_child = new_tree_obj

    def insert_right(self, new_node):
        if new_node < self.root:
            raise OrderError(f'New node({new_node = }) less then parent({self.root})')

        new_tree_obj = self.__class__(new_node)
        if self.right_child == None:
            self.right_child = new_tree_obj
        else:
            if new_node <= self.right_child.root:
                new_tree_obj.right_child = self.right_child
            else:
                new_tree_obj.left_child = self.right_child
            self.right_child = new_tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

    def __str__(self):
        def recursive_print(node=self):
            sub_line = str(node.root)
            sub_width = len(sub_line)

            if node.right_child is None and node.left_child is None:
                height = 1
                middle = sub_width // 2 
                return [sub_line], sub_width, height, middle

            if node.right_child is None:
                _ = recursive_print(node.left_child)
                lines, width_left_branch, height_left_branch, middle_left_branch = _

                first_line = ((middle_left_branch + 1) * ' ' + 
                              (width_left_branch - middle_left_branch - 1) * '_' + 
                               sub_line)

                second_line = (middle_left_branch * ' ' + '/' + 
                              (width_left_branch - middle_left_branch - 1 + sub_width) * ' ')

                shifted_lines = [line + sub_width * ' ' for line in lines]

                return ([first_line, second_line] + shifted_lines, 
                        middle_left_branch + sub_width, 
                        height_left_branch + 2, 
                        middle_left_branch + sub_width // 2)
            
            if node.left_child is None:
                _ = recursive_print(node.right_child)
                lines, width_right_branch, height_right_branch, middle_right_branch = _

                first_line = (sub_line + middle_right_branch * '_' + 
                             (width_right_branch - middle_right_branch) * ' ')

                second_line = ((sub_width + middle_right_branch) * ' ' + '\\' + 
                               (width_right_branch - middle_right_branch - 1) * ' ')

                shifted_lines = [sub_width * ' ' + line for line in lines]

                return ([first_line, second_line] + shifted_lines, 
                        width_right_branch + sub_width, 
                        height_right_branch + 2, 
                        sub_width // 2)

            _ = recursive_print(node.left_child)
            left, width_left_branch, height_left_branch, middle_left_branch = _

            _ = recursive_print(node.right_child)
            right, width_right_branch, height_right_branch, middle_right_branch= _

            first_line = ((middle_left_branch + 1) * ' ' + 
                          (width_left_branch - middle_left_branch - 1) * '_' + 
                          sub_line + middle_right_branch * '_' + 
                          (width_right_branch - middle_right_branch) * ' ')

            second_line = (middle_left_branch * ' ' + '/' + 
                          (width_left_branch - middle_left_branch - 1 + 
                            sub_width + middle_right_branch) * ' ' + 
                          '\\' + (width_right_branch - middle_right_branch - 1) * ' ')

            if height_left_branch < height_right_branch:
                left += [width_left_branch * ' '] * (height_right_branch - height_left_branch)
            elif height_right_branch < height_left_branch:
                right += [width_right_branch * ' '] * (height_left_branch - height_right_branch)

            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + sub_width * ' ' + b for a, b in zipped_lines]

            return (lines, width_left_branch + width_right_branch + sub_width, 
                    max(height_left_branch, height_right_branch) + 2, 
                    width_left_branch + sub_width // 2)
       
        lines, *_ = recursive_print(self)
    
        return '\n'.join(lines)
    


r = BinaryTreeSearch(10)
r.insert_left(9)
r.insert_left(8)
r.get_left_child().insert_left(7)

r.insert_right(12)
r.get_right_child().insert_left(11)
print(r)

