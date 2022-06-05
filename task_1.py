from collections import Counter, deque


class Huffman:

    def __init__(self, some_str):
        self.some_str = some_str
        self.code_table = dict()
        self.fill_in_code_table(self.make_tree())

    def make_tree(self):
        elements_amount = Counter(self.some_str)
        sorted_elements = deque(sorted(elements_amount.items(), key=lambda item: item[1]))
        if len(sorted_elements) != 1:
            while len(sorted_elements) > 1:
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                make_node = {0: sorted_elements.popleft()[0],
                             1: sorted_elements.popleft()[0]}
                for i, _count in enumerate(sorted_elements):
                    if weight > _count[1]:
                        continue
                    else:
                        sorted_elements.insert(i, (make_node, weight))
                        break
                else:
                    sorted_elements.append((make_node, weight))
        else:
            weight = sorted_elements[0][1]
            make_node = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((make_node, weight))
        return sorted_elements[0][0]

    def fill_in_code_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.fill_in_code_table(tree[0], path=f'{path}0')
            self.fill_in_code_table(tree[1], path=f'{path}1')

    def encode_str(self):
        encoded_str = ''
        for i in self.some_str:
            encoded_str += self.code_table[i]
        return encoded_str


if __name__ == '__main__':
    some_str = input('Input some string: ')
    test_1 = Huffman(some_str)
    print(f'Tree: {test_1.make_tree()}')
    print(f'Codes table:{test_1.code_table}')
    print(f'Encoded string: {test_1.encode_str()}')
