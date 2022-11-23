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


class Huffman_Code:

    def __init__(self, my_string):
        self.my_string = my_string
        self.code_dict = dict()
        self.get_huffman_code(self.get_huffman_tree())

    def get_sort_counter_symbol_in_string(self):
        return deque(sorted(Counter(self.my_string).items(), key=lambda item: item[1]))

    def get_huffman_tree(self):
        my_string = self.get_sort_counter_symbol_in_string()
        if len(my_string) != 1:
            while len(my_string) > 1:
                weight = my_string[0][1] + my_string[1][1]
                comb = {0: my_string.popleft()[0],
                        1: my_string.popleft()[0]}
                for i, _count in enumerate(my_string):
                    if weight > _count[1]:
                        continue
                    else:
                        my_string.insert(i, (comb, weight))
                        break
                else:
                    my_string.append((comb, weight))
        else:
            weight = my_string[0][1]
            comb = {0: my_string.popleft()[0], 1: None}
            my_string.append((comb, weight))
        return my_string[0][0]

    def get_huffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_dict[tree] = path
        else:
            self.get_huffman_code(tree[0], path=f'{path}0')
            self.get_huffman_code(tree[1], path=f'{path}1')
            return self.code_dict

    def get_huffman_code_in_string(self):
        return ''.join([self.code_dict[i] for i in self.my_string])

    def get_normal_string(self):
        res = ''
        i = 0
        code_string = self.get_huffman_code_in_string()
        code_dict = self.code_dict
        while i < len(code_string):
            for code in code_dict:
                if code_string[i:].find(code_dict[code]) == 0:
                    res += code
                    i += len(code_dict[code])
        return res


h_c = Huffman_Code('dfsfsddfsfsgsg fwfs fsdf')
print(h_c.get_sort_counter_symbol_in_string())
print(h_c.get_huffman_tree())
print(h_c.get_huffman_code(h_c.get_huffman_tree()))
print(h_c.get_huffman_code_in_string())
print(h_c.get_normal_string())
