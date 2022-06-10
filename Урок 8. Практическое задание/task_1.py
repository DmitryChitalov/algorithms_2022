"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import OrderedDict


class Leaf:
    """ Лист для создания дерева Хаффмана """

    __slots__ = ['key', 'value']

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'<Leaf[{self.key}={self.value}]>'


class Node:
    """ Класс Узел для построения """

    __slots__ = ['value', 'left', 'right']

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'<Node[{self.value}, {self.left}, {self.right}]>'


class Huffman:
    """ Класс сжатия и построения строки по алгоритму Хаффмана """

    __slots__ = ['data', 'code_table', 'real_str']

    def __init__(self):
        self.data = []
        self.code_table = {}
        self.real_str = ''

    def make_list(self, input_string: str):
        """ Упорядоченные массив обьектов класса Leaf """
        self.real_str = input_string
        symbols_arr = OrderedDict()

        # Подсчет символов
        for i in range(0, len(input_string)):
            symbol = input_string[i]
            if symbol not in symbols_arr:
                symbols_arr[symbol] = 1
            else:
                symbols_arr[symbol] += 1

        # Заполнение объектами
        for key, value in symbols_arr.items():
            self.data.append(Leaf(key, value))

    def create_huffman_tree(self):
        """ Построение бинарного дерева по алгоритму Хаффмана """
        while len(self.data) > 2:
            f_leaf = self.data.pop()
            s_leaf = self.data.pop()
            tmp_node = Node(f_leaf.value + s_leaf.value, s_leaf, f_leaf)
            tmp_node_value = tmp_node.value
            if tmp_node_value > self.data[0].value:
                self.data.insert(0, tmp_node)
            elif tmp_node_value < self.data[-1].value:
                self.data.append(tmp_node)
            else:
                for i in range(1, len(self.data)):
                    if self.data[i - 1].value >= tmp_node_value > self.data[i].value:
                        self.data = self.data[0:i] + [tmp_node] + self.data[i:]
                        break
        self.data = Node(self.data[0].value + self.data[1].value, self.data[0], self.data[1])

    def huffman_recursion(self, data, code: str = ''):
        """ Обход дерева и построение таблицы кодирования """
        if isinstance(data, Node):
            self.huffman_recursion(data.left, code + '0')
            self.huffman_recursion(data.right, code + '1')
        elif isinstance(data, Leaf):
            self.code_table[data.key] = code

    def get_encode_string(self) -> str:
        """ Преобразование в двоичный код """
        result = ''
        for i in range(0, len(self.real_str)):
            result = result + self.code_table[self.real_str[i]]
        return result

    def encode(self, input_string: str):
        """ Кодирование строки """
        self.make_list(input_string)
        self.create_huffman_tree()
        self.huffman_recursion(self.data)
        return self.get_encode_string()

    def decode(self, code_str, input_code_table=None):
        """ Декодирование строки """
        if input_code_table:
            self.code_table = input_code_table
        result = []
        i = 0
        j = 0
        while i < len(code_str):
            j += 1
            for key, val in input_code_table.items():
                if val == code_str[i:j:1]:
                    result.append(key)
                    i = j
        return ''.join(result)

    def get_table_code(self):
        """ Получить таблицу кодирования """
        return self.code_table

    def clear(self):
        self.data = []
        self.code_table = {}
        self.real_str = ''


huff = Huffman()
print(huff.encode('some string'))
# 0000110100010111000011110010100100011
code_table = huff.get_table_code()
# {'s': '000', 'n': '0010', 'g': '0011', 'm': '0100', 'e': '0101', 'o': '011',
# 'r': '100', 'i': '101', ' ': '110', 't': '111'}
print(code_table)
print(huff.decode('0000110100010111000011110010100100011', code_table))  # some string

# Проверка №2
huff.clear()
to_encode = 'Проверка еще одной строки проверка'
encoded = huff.encode(to_encode)
print(encoded)
decoded = huff.decode(encoded, huff.get_table_code())
print(decoded)
print(f"result - {decoded == to_encode}")
"""
101101001100000001010001000111100001111000011100111111101000111010111010010
10011010011001010000110100010100110000000101000100011
Проверка еще одной строки проверка
result - True
"""
