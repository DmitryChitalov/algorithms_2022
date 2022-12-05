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


# Будем делать на основе кода примера с урока с добавлением ООП
class HuffmanCode:
    # У класса будут атрибуты: строка, словарь с кодировками, код Хаффмана, счетчик:
    def __init__(self, input_str):
        self.input_str = input_str
        self.code_dict = dict()
        self.haffman_code(self.get_tree())

    # Счетчик как в примере отдельным методом:
    def get_counter(self):
        return Counter(self.input_str)

    # Сортировка как в примере отдельным методом:
    def get_sorted_deque(self):
        return deque(sorted(self.get_counter().items(), key=lambda item: item[1]))

    # Основной функционал кодирования, как в примере:
    def get_tree(self):
        sorted_elements = self.get_sorted_deque().copy()
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                new_elem = {0: sorted_elements.popleft()[0],
                            1: sorted_elements.popleft()[0]}
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (new_elem, weight))
                        break
                else:
                    sorted_elements.append((new_elem, weight))
        else:
            weight = sorted_elements[0][1]
            new_elem = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((new_elem, weight))
        return sorted_elements[0][0]

    # Метод получения кода как в примере:
    def haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_dict[tree] = path
        else:
            self.haffman_code(tree[0], path=f'{path}0')
            self.haffman_code(tree[1], path=f'{path}1')

    # Метод для декодирования:
    def get_decoded_str(self, code_string):
        out_decoded_str = ''
        # Будем итерироваться по коду Хаффмана:
        i = 0
        while i < len(code_string):
            # Ищем совпадение в созданном ранее словаре:
            for code in self.code_dict.keys():
                # Поиск происходит в остатке строки с кодом:
                if code_string[i:].find(self.code_dict[code]) == 0:
                    # Если нашли, добавляем к выходной строке символ из словаря:
                    out_decoded_str += code
                    # К итератору добавляем длину найденного в словаре кода (во избежание дубликатов):
                    i += len(self.code_dict[code])
        return out_decoded_str

    # Переопределим метод для вывода в консоль:
    def __str__(self):
        out_code = ''
        for char in self.input_str:
            out_code += self.code_dict[char]
        return out_code


coded_str = HuffmanCode(input('Строка для кодировки: '))
print(f'Дерево:\n{coded_str.get_tree()}')
print(f'Словарь кодировки:\n{coded_str.code_dict}')
print(f'Код Хаффмана:\n{coded_str}')
print(f'Декодированная строка:\n{coded_str.get_decoded_str(str(coded_str))}')
