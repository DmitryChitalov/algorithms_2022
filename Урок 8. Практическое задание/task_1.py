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

from collections import Counter, deque

class HaffmanTreeClass:
    def __init__(self, obj_l=None, obj_r=None):
        self.left_branch = obj_l
        self.right_branch = obj_r

    def huffman_tree(self, mystring):
        string_counter = Counter(mystring)
        string_deque = deque(sorted(string_counter.items(), key=lambda item: item[1]))
        while len(string_deque) > 1:
            new_node = HaffmanTreeClass(string_deque[0][0], string_deque[1][0])
            new_node_val = string_deque[0][1] + string_deque[1][1]
            string_deque.popleft()
            string_deque.popleft()
            for i in range(0, len(string_deque)):
                if string_deque[i][1] >= new_node_val:
                    string_deque.insert(i, (new_node, new_node_val))
                    break
            else:
                if len(string_deque) > 0 and string_deque[0][1] >= new_node_val:
                    string_deque.appendleft((new_node, new_node_val))
                else:
                    string_deque.append((new_node, new_node_val))
        self.left_branch = string_deque[0][0].left_branch
        self.right_branch = string_deque[0][0].right_branch
        return self

    def code(self, code_dict, code=''):
        if isinstance(self.left_branch, HaffmanTreeClass):
            self.left_branch.code(code_dict, code + '0')
        else:
            code_dict[self.left_branch] = code + '0'
        if isinstance(self.right_branch, HaffmanTreeClass):
            self.right_branch.code(code_dict, code + '1')
        else:
            code_dict[self.right_branch] = code + '1'
        return code_dict


if __name__ == '__main__':
    code_table = dict()
    user_string = input('Введите строку: ')
    c = HaffmanTreeClass()
    c.huffman_tree(user_string)
    print(f'Таблица с кодами\n {c.code(code_table)}')
    print('Закодированная строка: ')
    for i in user_string:
        print(code_table[i], end=' ')
    print()

"""
Собственно, за основу взят алгоритм с урока


Введите строку: beep boop beer!
Таблица с кодами
 {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
Закодированная строка: 
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001 
"""
