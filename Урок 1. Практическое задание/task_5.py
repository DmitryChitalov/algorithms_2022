"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""


class MyStack:

    def __init__(self, limit):
        self.stack = [[]]
        self.limit = limit

    def is_empty(self):
        return self.stack[0] == []

    def add_item(self, item):
        if len(self.stack[-1]) < self.limit:
            self.stack[-1].append(item)
        else:
            self.stack.append([item])

    def get_item(self):
        if not self.is_empty():
            item = self.stack[-1].pop()
            if len(self.stack[-1]) == 0:
                self.stack.__delitem__(-1)
            return item
        else:
            return []


st = MyStack(5)
for i in range(28):
    st.add_item(i)
print(st.stack)
lst = []
for _ in range(7):
    lst.append(st.get_item())
print(lst)
print(st.stack)