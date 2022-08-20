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


class Stack:
    def __init__(self, max_size):
        self.stack = [[]]
        self.max_size = max_size

    def push(self, el):
        if len(self.stack[len(self.stack)-1]) < self.max_size:
            self.stack[len(self.stack)-1].append(el)
        else:
            self.stack.append([])
            self.stack[len(self.stack)-1].append(el)

    def pop(self):
        result = self.stack[len(self.stack)-1].pop()
        if len(self.stack[len(self.stack)-1]) == 0:
            self.stack.pop()
        return result


if __name__ == '__main__':
    stack1 = Stack(3)
    stack1.push('dish')
    stack1.push('dish')
    stack1.push('dish')
    print('Добавили три тарелки', stack1.stack)
    stack1.push('dish')
    print('Добавили еще одну', stack1.stack)
    stack1.push('dish')
    stack1.push('dish')
    stack1.push('dish')
    print('Добавили еще три', stack1.stack)
    stack1.pop()
    print('Убрали одну',stack1.stack)
    stack1.pop()
    print('Убрали еще одну', stack1.stack)