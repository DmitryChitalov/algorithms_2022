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


class HaffmanCode:

    def __init__(self, text):
        self.user_text = text
        self.code = {}
        self.generate_code(self.create_tree())

    def count_str(self):
        return Counter(self.user_text)

    def sort_str(self):
        return deque(sorted(self.count_str().items(), key=lambda item: item[1]))

    def generate_code(self, data, hm_code=''):
        if type(data[0]) == str:
            self.code[data[0]] = hm_code
        else:
            self.generate_code(data[0][0], f'{hm_code}0')
            self.generate_code(data[0][1], f'{hm_code}1')

    def create_tree(self):
        tree = ()
        sub_tree = self.sort_str()
        while len(sub_tree) > 1:
            left_node = sub_tree.popleft()
            right_node = sub_tree.popleft()
            weight = left_node[1] + right_node[1]
            tree = ((left_node, right_node), weight)
            for i, item in enumerate(sub_tree):
                if item[1] != weight:
                    continue
                else:
                    sub_tree.insert(i, tree)
                    break
            else:
                sub_tree.append(tree)

        return tree

    def generate_str(self):
        for i in self.user_text:
            print(a.code[i], end=' ')
        print()


if __name__ == "__main__":
    a = HaffmanCode('beep boop beer!')

    print(a.generate_str())

    """
    Пытался придумать что-то оригинальное, например, генерировать
    код на стадии формирования дерева через внесение дополнительного
    параметра, но из-за нехватки времени решил реализовать строго
    по шагам алгоритма. И при сравнении Вашего файла с моим нашел
    примерно ноль отличий.
    Была идея прибегнуть к namedtuple или defaultdict, но до
    конечно реализации так и не дошел. А вот как отказаться от
    дека и Countera хотябы из соображений удобства, скорости
    написания кода и повышения читабельности даже не представляю
    """