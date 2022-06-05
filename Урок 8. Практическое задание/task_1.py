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
from heapq import heappop, heapify, heappush
from collections import Counter


# Для реализации кодирования строки по алгоритму Хаффмана воспользовался кучей (heapq) для построения двоичного дерева,
# которая с помощью heappop всегда выбрасывает элемент с наименьшим приоритетом.
# В классе, возможно, избыточное количество атрибутов. Это сделано для удобства отладки.
class HuffmanCoding:
    def __init__(self, line):
        self.line = line
        self.key_kod = {}
        self.binary_tree = []
        self.encoded = ''
        self.huffman_tree()

    def huffman_tree(self):  # создаем двоичное дерево, получаем таблицу кодов и кодируем заданную строку
        def huffman_code(tree, path=''):  # собираем двоичные коды для символов
            if isinstance(tree, str):
                self.key_kod[tree] = path
            else:
                huffman_code(tree[0], path=f'{path}0')
                huffman_code(tree[1], path=f'{path}1')

        heapify(h := [[cnt[1], -i, cnt[0]] for i, cnt in enumerate(Counter(self.line).items())])
        while len(h) > 1:
            (freq1, _, left), (freq2, _, right) = heappop(h), heappop(h)
            heappush(h, [freq1 + freq2, len(h) + 1, [left, right]])
        huffman_code(h[0][2])  # h[0][2] двоичное дерево без приоритетов
        self.encoded = ''.join(self.key_kod[ch] for ch in self.line)  # шифруем строку с пом. таблицы символов

    def huffman_decode(self):  # делаем раскодировку шифрованной строки
        s, b = '', 0
        while b < len(self.encoded):
            for k, v in self.key_kod.items():
                if v == self.encoded[b:b + len(v)]:
                    s += k
                    b += len(v)
        return s

    def __str__(self):
        return f"{self.line}\nkey_code:{self.key_kod} \nencoded line:{self.encoded}"


# проверяем работу алгоритма
def test(n_iter=100):
    import random
    import string
    for i in range(n_iter):
        length = random.randint(10, 50)
        s = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        h_ex = HuffmanCoding(s)
        assert h_ex.huffman_decode() == s
    print("Tests - OK!")


sss = 'beep boop beer!'
h_c = HuffmanCoding(sss)
print(h_c)
print(f'Дешифруем: {h_c.huffman_decode()}')
test()
