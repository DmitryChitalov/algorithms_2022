from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haffman_tree(s):
    con = Counter(s)
    sor = deque(sorted(con.items(), key=lambda item: item[1]))
    while len(sor) > 1:
        weight = sor[0][1] + sor[1][1]
        node = MyNode(left=sor.popleft()[0], right=sor.popleft()[0])
        for i, item in enumerate(sor):
            if weight > item[1]:
                continue
            else:
                sor.insert(i, (node, weight))
                break
        else:
            sor.append((node, weight))
    return sor[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_table[tree] = path
    else:
        haffman_code(tree.left, path=f'{path}0')
        haffman_code(tree.right, path=f'{path}1')


s = "Hello Dmitry!"
haffman_code(haffman_tree(s))
for j in code_table.items():
    print(f"'{j[0]}' -> {j[1]}", end=' ;  ')
print()
for i in s:
    print(code_table[i], end=' ')
