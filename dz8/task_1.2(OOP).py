from collections import Counter, deque


class HaffDec:
    def __init__(self, strc):
        self.strc = strc
        self.tbl_cod = dict()
        self.haff_cod(self.tree_my())

    def sort_count(self):
        count = Counter(self.strc)
        dec = deque(sorted(count.items(), key=lambda item: item[1]))
        return dec

    def tree_my(self):
        dec = self.sort_count().copy()
        if len(dec) != 1:
            while len(dec) > 1:
                sum_w = dec[0][1] + dec[1][1]
                res = {0: dec.popleft()[0],
                       1: dec.popleft()[0]}
                for i, w, in enumerate(dec):
                    if sum_w > w[1]:
                        continue
                    else:
                        dec.insert(i, (res, sum_w))
                        break
                else:
                    dec.append((res, sum_w))
        else:
            sum_w = dec[0][1]
            res = {0: dec.popleft()[0][1], 1: None}
            dec.append((res, sum_w))
        return dec[0][0]

    def haff_cod(self, tree, path=''):
        if not isinstance(tree, dict):
            self.tbl_cod[tree] = path
        else:
            self.haff_cod(tree[0], path=f'{path}0')
            self.haff_cod(tree[1], path=f'{path}1')

    def string_code(self):
        res = ''
        for el in self.strc:
            res += self.tbl_cod[el]
        return res

    def decoding(self, string_code):
        res = ''
        i = 0
        tbl_cod = self.tbl_cod
        while i < len(string_code):
            for cod in tbl_cod:
                if string_code[i:].find(tbl_cod[cod]) == 0:
                    res += cod
                    i += len(tbl_cod[cod])
        return res


a = HaffDec(input('Введите слово: '))
print(f"Список кортежей в деке: {a.sort_count()}")
print(f"Дерево: {a.tree_my()}")
print(f"Таблица закодированных символов: {a.tbl_cod}")
print(f"Закодированная строка: {a.string_code()}")
stroka = a.string_code()
print(f"Декадированная строка: {a.decoding(stroka)}")
