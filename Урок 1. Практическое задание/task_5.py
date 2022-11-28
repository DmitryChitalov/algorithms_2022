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


class StackStopok:
    def __init__(self):
        self.box_stopok = []
        self.stopka = []
        self.count = 1
        self.main()

    def tarelka_add(self):
        self.stopka.append(self.count)
        self.count += 1
        return self.stopka

    def add_stopka_to_box(self):
        x = self.stopka.copy()
        self.stopka.clear()
        self.box_stopok.append(x)
        return self.box_stopok

    def main(self):
        while len(self.stopka) <= 3:
            if len(self.stopka) == 3:
                self.add_stopka_to_box()
            if len(self.box_stopok) == 4:
                print('Всего в коробке стопок: ', len(self.box_stopok))
                break
            x = input('Положить тарелку в стопку?')
            if x == 'y':
                self.tarelka_add()
                print('тарелок в стопке', len(self.stopka), '\n' 'в коробке стопок ', len(self.box_stopok))


x = StackStopok()
