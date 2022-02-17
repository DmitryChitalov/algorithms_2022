"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class HuffmanCode:

    def __init__(self, input_string):
        self.input_string = input_string
        self.code_table = dict()
        self.huffman_code(self.get_tree())

    def get_counter_symbol(self):
        return Counter(self.input_string)

    def sort_counter_value(self):
        return deque(sorted(self.get_counter_symbol().items(),
                            key=lambda item: item[1]))

    def get_tree(self):
        sort_value = self.sort_counter_value().copy()
        if len(sort_value) != 1:
            while len(sort_value) > 1:
                weight = sort_value[0][1] + sort_value[1][1]
                new_elem = {0: sort_value.popleft()[0],
                            1: sort_value.popleft()[0]}
                for i, _count in enumerate(sort_value):
                    if weight > _count[1]:
                        continue
                    else:
                        sort_value.insert(i, (new_elem, weight))
                        break
                else:
                    sort_value.append((new_elem, weight))
        else:
            weight = sort_value[0][1]
            new_elem = {0: sort_value.popleft()[0], 1: None}
            sort_value.append((new_elem, weight))
        return sort_value[0][0]

    def huffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code(tree[0], path=f'{path}0')
            self.huffman_code(tree[1], path=f'{path}1')

    def get_string_code(self):
        res = ''
        for symbol in self.input_string:
            res += self.code_table[symbol]
        return res

    def decoding(self, code_string):
        res = ''
        i = 0
        codes_dict = self.code_table
        while i < len(code_string):
            for code in codes_dict:
                if code_string[i:].find(codes_dict[code]) == 0:
                    res += code
                    i += len(codes_dict[code])
        return res

    def draw_tree(self, tree, prefix=''):
        if isinstance(tree, str):
            descr = f'N{prefix} [label="{tree}:{prefix}", fontcolor=blue, fontsize=16, width=2, shape=box];\n'
        else:
            descr = f'N{prefix} [label="{prefix}"];\n'
            for child in tree.keys():
                descr += self.draw_tree(tree[child], prefix=f'{prefix}{child}')
                descr += f'N{prefix} -> N{prefix}{child};\n'
        return descr

    def save_tree(self):
        with open('graph.dot', 'w') as f:
            f.write('digraph G {\n')
            f.write(self.draw_tree(self.get_tree()))
            f.write('}')


if __name__ == '__main__':
    string = input("Введите строку: ")
    a_1 = HuffmanCode(string)
    print(f"Исходная строка:\n'{string}'")

    tree_1 = a_1.get_tree()
    print(f"Дерево:\n{tree_1}")

    print(f"Таблица c кодами:\n{a_1.code_table}")

    code_str = a_1.get_string_code()
    print(f"Строка кода после кодирования:\n{code_str}")
    print(f"Декодированная строка:\n'{a_1.decoding(code_str)}'")
    a_1.save_tree()

# please don't stop the music

"""
Переменная users_string изменена на input_string.

Добавлены два метода в класс:
draw_tree - создаёт строки для файла типа .dot
save_tree - сохраняет файл dot

Дерево сохраняется в файле graph.dot, который потом можно открыть и посмотреть, 
пример исполнения взят со stackoverflow и модифицирован под f-строки.

Была мысль про замену degue на namedtuple, 
но хотелось добавить функционала, а не просто сделать изменения ради изменений.
"""
