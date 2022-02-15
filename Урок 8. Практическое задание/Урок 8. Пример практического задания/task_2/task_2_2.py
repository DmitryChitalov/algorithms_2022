import random


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

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

    # добавить потомков
    def insert(self, data):
        if data == self.root:
            self.root = data
        else:
            if data < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(data)
                else:
                    self.left_child.insert(data)
            elif data > self.root:

                if self.right_child is None:
                    self.right_child = BinaryTree(data)
                else:
                    self.right_child.insert(data)

    # метод доступа к правому потомку
    def get_right_child(self, root):

        if root == self.root:
            if self.right_child is None:
                print('Потомка нет')
            else:
                print(f'Узел {self.root}, правый потомок '
                      f'{self.right_child._get_root_val()}')
        else:
            try:
                if root > self.root:
                    self.right_child.get_right_child(root)
                else:
                    self.left_child.get_right_child(root)
            except AttributeError:
                print('Узел отсутствует')

    # метод доступа к левому потомку
    def get_left_child(self, root):
        if root == self.root:
            if self.left_child is None:
                print('Потомка нет')
            else:
                print(f'Узел {self.root}, левый потомок'
                      f' {self.left_child._get_root_val()}')
        else:
            try:
                if root > self.root:
                    self.right_child.get_left_child(root)
                else:
                    self.left_child.get_left_child(root)
            except AttributeError:
                print('Узел отсутствует')

    # метод доступа к корню
    def _get_root_val(self):
        return self.root


r = BinaryTree(50)

for _ in range(20):
    r.insert(random.randint(10, 60))
r.display()
for i in range(10):
    a = random.randint(10, 60)
    print(f'Поиск потомков узла {a}', end=': ')
    if i % 2 == 0:
        r.get_left_child(a)
    else:
        r.get_right_child(a)

'''
Изменен основной алгоритм. Убрано ручное добавление элементов, 
заменено на автоматическое с проверкой. 
Также изменен подход к взятью левого (правого)
 потомка - нужно указать родителя.
Добавлена проверка на наличия узла в дереве.

Применен специальный алгоритм для вывода графа в консолью.

        __________________50___     
       /                       \    
      18_____                 57___ 
     /       \               /     \
  __16    __32_________     55    60
 /       /             \         /  
10_     27_       ____44_       58  
   \       \     /       \          
  12      29    37_     46          
               /   \                
              33  39_               
                     \              
                    41  
                                
Поиск потомков узла 37: Узел 37, левый потомок 33
Поиск потомков узла 36: Узел отсутствует
Поиск потомков узла 44: Узел 44, левый потомок 37
Поиск потомков узла 58: Потомка нет
Поиск потомков узла 44: Узел 44, левый потомок 37
Поиск потомков узла 11: Узел отсутствует
Поиск потомков узла 47: Узел отсутствует
Поиск потомков узла 12: Потомка нет
Поиск потомков узла 24: Узел отсутствует
Поиск потомков узла 55: Потомка нет
'''
