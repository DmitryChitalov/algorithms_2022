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


class Huffman:
    def __init__(self, string_for_code):
        self.string_for_code = string_for_code
        self.code_table = dict()
        self.huffman_code(self.huffman_tree())
        self.result_code = ''

    def huffman_tree(self):
        count = Counter(self.string_for_code)
        sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                comb = {0: sorted_elements.popleft()[0], 1: sorted_elements.popleft()[0]}

                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (comb, weight))
                        break
                else:
                    sorted_elements.append((comb, weight))

        else:
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
        return sorted_elements[0][0]

    def huffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code(tree[0], path=f'{path}0')
            self.huffman_code(tree[1], path=f'{path}1')
        return self.code_table

    def encoding(self):
        for i in self.string_for_code:
            self.result_code += self.code_table[i]
        return self.result_code


str_code = input('Введите строку: ')
exam = Huffman(str_code)
print(f'Ваша строка: {str_code}')
print(f'Закодированная строка: {exam.encoding()}')
print(f'Таблица: {exam.code_table}')
