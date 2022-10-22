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

from task_1_2 import HaffmanElement, HaffmanTree

class HaffmanCoding():
    def __init__(self, str_src : str):
        self.__str_src = str_src
        self.__simbols_list = list()
        self.root_element = HaffmanElement('root', 0)
        self.__dict_haffman = dict()

        self.__create_list_simbols()
        self.__create_binary_tree()

    def print_simbols_list(self):
        st_list_simbols = str()
        for i in self.__simbols_list:
            st_list_simbols += f'{str(i)}, '
        st_list_simbols = st_list_simbols[:-2]
        print(st_list_simbols)

    def view_tree(self, node):
        # print('Haffman element:', node)
        left_child = node.left_child
        right_child = node.right_child
        if not left_child is None:
            node.left_child.bit += node.bit + '0'
            print(f'left {node}:', node.left_child)
            if node.left_child.simbol[:4] != 'zero':
                self.__dict_haffman[node.left_child.simbol] = node.left_child.bit
                # print(node.left_child.simbol)
            self.view_tree(left_child)
        if not right_child is None:
            node.right_child.bit += node.bit + '1'
            print(f'right {node}:', node.right_child)
            if node.right_child.simbol[:4] != 'zero':
                self.__dict_haffman[node.right_child.simbol] = node.right_child.bit
                # print(node.right_child.simbol)
            self.view_tree(right_child)

    # Формирование словаря с уникальными символами
    def __create_list_simbols(self):
        simbols_set = set(self.__str_src)
        for simbol in simbols_set:
            self.__simbols_list.append(HaffmanElement(simbol, self.__str_src.count(simbol)))
        self.__simbols_list.sort(key=lambda el: el.count)
        self.print_simbols_list()
        print('-----end __create_list_simbols-----\n')

    def __create_binary_tree(self):
        n = 1
        while len(self.__simbols_list) > 2:
            el_a = self.__simbols_list.pop(0)
            el_b = self.__simbols_list.pop(0)
            zero = HaffmanElement('zero' + str(n), el_a.count + el_b.count)
            n += 1
            zero.insert_left(el_a)
            zero.insert_right(el_b)
            # if el_a.count >= el_b.count:
            #     zero.insert_right(el_a)
            #     zero.insert_left(el_b)
            # else:
            #     zero.insert_left(el_a)
            #     zero.insert_right(el_b)
            for i, el in enumerate(self.__simbols_list):
                if zero.count > el.count:
                    continue
                else:
                    self.__simbols_list.insert(i, zero)
                    break
            else:
                self.__simbols_list.append(zero)

        el_a = self.__simbols_list[0]
        el_b = self.__simbols_list[1]
        if el_a.count >= el_b.count:
            self.root_element.insert_right(el_a)
            self.root_element.insert_left(el_b)
        else:
            self.root_element.insert_left(el_a)
            self.root_element.insert_right(el_b)
        self.view_tree(self.root_element)
        print('-----end __create_binary_tree-----\n')

    def encoding_text(self):
        print('Словарь кодирования Хаффмана:')
        print(self.__dict_haffman)
        st_coding = ''
        for el in self.__str_src:
            st_coding += self.__dict_haffman[el]
        print(st_coding)

        st_coding_space = ''
        for i, el in enumerate(list(st_coding)):
            st_coding_space += el
            if ((i+1) > 3) and (((i+1) % 4) == 0):
                st_coding_space += ' '
        print(st_coding_space)


h = HaffmanCoding('beep boop beer!')
h.encoding_text()
print()