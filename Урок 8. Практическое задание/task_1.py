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
from collections import Counter

s = "dfghjkliuytyujnbghvfrtgfcdxserfdxswedfgvghjhjkjhyujhgyujgtyhgfrtgftyhukjuikjhgftyhgyujhgyujhujhgtgfdrtgft"


class HoffmanEncoding:
    def __init__(self, string):
        self.string = string
        self.dct = {}

    def Hoffman_lst(self):
        frequency_dict = Counter(self.string)
        lst = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(lst) - 1):
            b = lst.pop()
            a = lst.pop()
            c = [a[0], b[0]]
            num = a[1] + b[1]
            lst.append((0, 0))
            for j in range(len(lst) - 1, -1, -1):
                if num < lst[j][1]:
                    lst.insert(j + 1, (c, num))
                    break
                elif j == 0:
                    lst.insert(0, (c, num))
            lst.pop()
        return lst[0][0]

    def Hoffman_dict(self, lst, cod=''):
        if isinstance(lst[0], str):
            self.dct.update({lst[0]: cod + '0'})
        else:
            self.dct.update(self.Hoffman_dict(lst[0], cod + '0'))
        if isinstance(lst[1], str):
            self.dct.update({lst[1]: cod + '1'})
        else:
            self.dct.update(self.Hoffman_dict(lst[1], cod + '1'))
        return self.dct

    def Hoffman_code(self):
        for i in self.string:
            self.string = self.string.replace(i, self.dct[i], 1)
        return self.string

    def get_code(self):
        self.Hoffman_dict(self.Hoffman_lst())
        return self.Hoffman_code()


h = HoffmanEncoding(s)
print(h.get_code())
print(h.dct)
