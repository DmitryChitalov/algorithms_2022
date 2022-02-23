"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class Stack_plate():
    def __init__(self):
        self.limit = 3
        self.stack = [[]]

    def append_val(self, val):
        if len(self.stack[-1]) > self.limit:
            new_inner = []
            new_inner.append(val)
            self.stack.append(new_inner)
        else:
            self.stack[-1].append(val)

    def __str__(self):
        return str(self.stack)

    def get_val(self):
        res = self.stack[-1][-1]
        del self.stack[-1][-1]
        if len(self.stack[-1]) < 1:
            del self.stack[-1]
        return res


st = Stack_plate()
st.append_val('st1')
st.append_val('st2')
st.append_val('smth')
st.append_val(123)
st.append_val(-1)




print(st)

















