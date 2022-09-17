# """
# Задание 1.
#
# Реализуйте кодирование строки по алгоритму Хаффмана.
# У вас два пути:
# 1) тема идет тяжело? тогда вы можете,
# опираясь на примеры с урока, сделать свою версию алгоритма
# Разрешается и приветствуется изменение имен переменных,
# выбор других коллекций, различные изменения
# и оптимизации.
#
# 2) тема понятна? постарайтесь сделать свою реализацию.
# Вы можете реализовать задачу, например,
# через ООП или предложить иной подход к решению.
# """
#
from collections import Counter, deque


class Node:  # узел дерева. Имя (символ), значение- (0/1),
    def __init__(self, name=None, val=None):
        self.name = name
        self.val = val
        self.l_child = None
        self.r_child = None

    def __str__(self):
        return f'{self.val}'

    def has_left_child(self):
        if self.l_child:
            return True
        return False

    def has_right_child(self):
        if self.r_child:
            return True
        return False

    def add_left_child(self, child):
        if not self.has_left_child():
            self.l_child = child
        else:
            print('Ошибка вставки элемента')

    def add_right_child(self, child):
        if not self.has_right_child():
            self.r_child = child
        else:
            print('Ошибка вставки элемента')


class HuffmanTree:
    def __init__(self, input_str):
        self.input_str = input_str  # храним строку
        self.root = self.make_tree(input_str)  # корень дерева (состоит из экземпляров Node), где имя - буква,
        # а Node.val - 0/1
        self.letters_way = self.make_way(self.root)
        self.encoded_str = None

    def make_tree(self, inpt_str):  # создаем дерево и возвращаем корень
        counter = Counter(inpt_str)
        nodes_deque = deque(Node(el[0], el[1]) for el in sorted((counter.items()), key=lambda x: x[1]))
        while len(nodes_deque) >= 2:
            new_node = Node(val=nodes_deque[0].val + nodes_deque[1].val)  # создаём ноду на основе двух первых элементов
            nodes_deque[0].val = 0  # значениям присваиваем 0 и 1 соответственно (в зависимости от расположения)
            nodes_deque[1].val = 1
            new_node.add_left_child(nodes_deque[0])
            new_node.add_right_child(nodes_deque[1])
            if len(nodes_deque) == 2:  # так как на последнем этапе у нас останется 2 элемента - возвращаем new_node
                # она и будет являться корнем
                return new_node
            nodes_deque.popleft()  # удаляем оба элемента
            nodes_deque.popleft()
            nodes_deque.insert(self.index_searcher(nodes_deque, new_node), new_node)  # вставляет ноду в список обратно

    @staticmethod
    def index_searcher(deq, target):  # бинарный поиск индекса по node.val в последовательности
        low = 0
        high = len(deq) - 1
        while low != high:
            mid = (low + high) // 2
            if deq[mid].val == target.val:
                return mid
            elif deq[mid].val < target.val:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1

    @staticmethod
    def make_way(root_):  # Обходим дерево и "собираем" путь до каждого символа, записываем в словарь и возвращаем
        letters_way = {}

        def filling_letters_ways(root: Node, string=''):  # рекурсивная функция обхода дерева
            if isinstance(root.name, str):
                letters_way[root.name] = string
            else:
                if root.has_left_child():
                    filling_letters_ways(root.l_child, string + str(root.l_child.val))
                if root.has_right_child():
                    filling_letters_ways(root.r_child, string + str(root.r_child.val))

        filling_letters_ways(root_)
        return letters_way

    def do_encode(self):
        result = ''
        for el in self.input_str:
            result += self.letters_way[el]
        self.encoded_str = result


if __name__ == '__main__':
    user_string = input('Введите строку для кодирования по методу Хаффмана: ')
    huff_tree = HuffmanTree(user_string)
    huff_tree.do_encode()
    print(f'Закодированная строка: {huff_tree.encoded_str}')
    print(f'Длина введённой строки {len(user_string)}')
    print(f'Длинна закодированной строки: {len(huff_tree.encoded_str)}')
