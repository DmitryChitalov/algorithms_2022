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


class StackPlates:
    def __init__(self, vol_stack):
        self.vol_stack = vol_stack
        self.stack = []

    def add_stack(self, vol, varibl):
        if len(self.stack) == 0:
            self.stack.append([str(varibl)])
            vol = vol-1
        for i in range(1, vol+1):
            stack = self.stack.pop()
            if len(list(stack)) == self.vol_stack:
                self.stack.append(stack)
                self.stack.append([str(varibl)])
            if len(list(stack)) < self.vol_stack:
                stack.append(str(varibl))
                self.stack.append(stack)


if __name__ == '__main__':
    # Создаем стек с размером стопки
    a = StackPlates(5)
    # добавляем количество тарелок - vol и тип тарелки - varibl
    a.add_stack(6, "p5656")
    a.add_stack(6, "222")
    a.add_stack(3, "6676")
    a.add_stack(5, "ttghfgh6666")

    print(a.stack)
