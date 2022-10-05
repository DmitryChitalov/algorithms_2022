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
class StackClass:
    def __init__(self):
        self.elems = [[]]

    def push_in(self, el, col):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        j = 1
        for i in range(0, len(self.elems)):
            while len(self.elems[i]) < col:
                if j > el:
                    break
                self.elems[i].append(j)

                if j == col * (i + 1) and el != col:
                    self.elems.append([])
                    i += 1
                j += 1


if __name__ == '__main__':
    SC_OBJ = StackClass()
    SC_OBJ.push_in(7, 4)

    print(SC_OBJ.elems)
