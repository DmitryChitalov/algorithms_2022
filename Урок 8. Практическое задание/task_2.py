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
from collections import Counter, deque


class BinaryTree:
    def __init__(self, user_str):
        self.user_str = user_str
        self.code_table = dict()
        self.huffman_code(self.get_tree())

    def sort_counter(self):
        counter = Counter(self.user_str)
        return deque(sorted(counter.items(),
                            key=lambda item: item[1]))

    def get_tree(self):
        sort_value = self.sort_counter().copy()
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

    def get_str_code(self):
        res = ''
        for i in self.user_str:
            res += self.code_table[i]
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


str_1 = input("Введите строку: ")
tr_obj = BinaryTree(str_1)
print(f"Исходная строка:\n'{str_1}'")

tree_1 = tr_obj.get_tree()
print(f"Дерево:\n{tree_1}")

print(f"Таблица c кодами:\n{tr_obj.code_table}")

print(f"Строка кода после кодирования:\n{tr_obj.get_str_code()}")
print(f"Декодированная строка:\n'{tr_obj.decoding(tr_obj.get_str_code())}'")


