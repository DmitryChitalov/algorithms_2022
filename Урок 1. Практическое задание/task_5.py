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
#НЕ СПРАВИЛСЯ

class Stack:
    def __init__(self):
        self.stack = [[]]

    def push(self, item):
        # print(len(self.stack))
        for spam in range(len(self.stack)):
            if len(self.stack[spam]) < 5:
                self.stack[spam].append(item)
            else:
                self.stack.append([item])
        # if len(self.stack) == 0:
        #     self.stack.append([item])
        # elif len(self.stack[0]) < 5 and len(self.stack) != 0:
        #     self.stack[0].append(item)
        # else:
        #     self.stack.append([item])

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


if __name__ == '__main__':
    stack = Stack()
    i = 1
    # count = 0
    # for sum in range(i):
    #     stack.push(count)
    #     count+=1
    while i < 10:
        stack.push(1 + i)
        i += 1
    print(stack.stack)

