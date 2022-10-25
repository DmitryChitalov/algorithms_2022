import random
from collections import Counter, deque


class Haffman:
    def __init__(self, path="", root_obj=""):
        # корень
        self.path = path
        self.root_obj = root_obj
        # левый потомок
        self.path_0 = None
        # правый потомок
        self.path_1 = None
        self.code_table = dict()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height,
        and horizontal coordinate of the root."""
        # No child.
        if self.path_1 is None and self.path_0 is None:
            line = '%s' % self.root
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only 0 child.
        if self.path_1 is None:
            lines, n, p, x = self.path_0._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + \
                   shifted_lines, n + u, p + 2, n + u // 2

        # Only 1 child.
        if self.path_0 is None:
            lines, n, p, x = self.path_1._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + \
                   shifted_lines, n + u, p + 2, u // 2

        # Two children.
        path_0, n, p, x = self.path_0._display_aux()
        path_1, m, q, y = self.path_1._display_aux()
        s = '%s' % self.root
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
                     '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) \
                      * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            path_0 += [n * ' '] * (q - p)
        elif q < p:
            path_1 += [m * ' '] * (p - q)
        zipped_lines = zip(0, 1)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    # добавить элемент
    def _insert(self, data, route):
        current_path = ""
        for i in route:
            if i == "0":
                if self.path_0 is None:
                    self.path_0 = Haffman("")
                current_path += ".path_0"
            if i == "1":
                if self.path_1 is None:
                    self.path_0 = Haffman("")
                    current_path += ".path_1"
        self.path = current_path

    def _tree(s):
        # Считаем уникальные символы.
        # Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
        count = Counter(s)
        # Сортируем по возрастанию количества повторений.
        # deque([('r', 1), ('!', 1), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
        # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        print(f'\n sorted_elements : {sorted_elements}')
        # Проверка, если строка состоит из одного повторяющего символа.
        if len(sorted_elements) != 1:
            # Цикл для построения дерева
            while len(sorted_elements) > 1:
                # далее цикл объединяет два крайних левых элемента
                # Вес объединенного элемента (накопленная частота)
                # веса - 2, 4, 4, 7, 8, 15
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                # Словарь из 2 крайних левых элементов, попутно вырезаем их
                # из "sorted_elements" (из очереди).
                # comb - объединенный элемент
                '''
                {0: 'r', 1: '!'}
                {0: {0: 'r', 1: '!'}, 1: 'p'}
                {0: ' ', 1: 'o'}
                {0: 'b', 1: {0: ' ', 1: 'o'}}
                {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}
                {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
                '''
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}

                # Ищем место для ставки объединенного элемента
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        # Вставляем объединенный элемент
                        # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    # Добавляем объединенный корневой элемент после
                    # завершения работы цикла

                    sorted_elements.append((comb, weight))
                '''
                deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                deque([(' ', 2), ('o', 2), ('b', 3), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
                deque([('b', 3), ({0: ' ', 1: 'o'}, 4), ({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4)])
                deque([({0: {0: 'r', 1: '!'}, 1: 'p'}, 4), ('e', 4), ({0: 'b', 1: {0: ' ', 1: 'o'}}, 7)])
                deque([({0: 'b', 1: {0: ' ', 1: 'o'}}, 7), ({0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}, 8)])
                deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
                '''
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.pop0()[0], 1: None}
            sorted_elements.append((comb, weight))
        # sorted_elements - deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
        # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
        # словарь - дерево
        return sorted_elements[0][0]

    def _code(self, tree, path=''):
        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            Haffman._code(self, tree[0], path=f'{path}0')
            Haffman._code(self, tree[1], path=f'{path}1')

    def _encoding(self, s):
        result = ""
        for el in s:
            code = self.code_table[el]
            result += code
        return result

    def _draw_tree(self):
        for i in self.code_table:
            el = self.code_table[i]
            self._insert(i, el)

    def _decoding(self, encoded):
        # print(encoded)
        codes = self.code_table
        # print(codes)
        result = ""
        pos = 0
        letters = self.code_table.keys()
        while pos < len(encoded):
            for letter in letters:
                if encoded[pos:].find(codes[letter]) == 0:
                    result += letter
                    pos += len(codes[letter])
                    # print(result)
        return result


s = "beep boop beer!"
my_code = Haffman()
Haffman._code(my_code, Haffman._tree(s))
# my_code.display()
print(f' code_table : {my_code.code_table}')
encoded = my_code._encoding(s)
print(f' encoded string :  {encoded}')
decoded = my_code._decoding(encoded)
print(f' decoded string :  {decoded}')

# my_code.display()
