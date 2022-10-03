"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.lst_elem = []
        self.lst_done = []
        self.lst_need_correct = []

    def is_empty(self):
        return self.lst_elem == []

    def to_queue(self, item):
        self.lst_elem.insert(0, item)

    def from_queue(self):
        return self.lst_elem.pop()

    def size(self):
        return len(self.lst_elem)

    def done(self):
        self.lst_done.insert(0, self.lst_elem.pop())
        return self.lst_done

    def need_correct(self):
        self.lst_need_correct.insert(0, self.lst_elem.pop())
        return self.lst_need_correct

if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)
    qc_obj.to_queue(2)

    print(qc_obj.is_empty())  # -> False. Очередь пустая
    print(qc_obj.lst_elem)  #
    print(qc_obj.done())  #
    print(qc_obj.lst_elem)
    print(qc_obj.need_correct())  #
    print(qc_obj.lst_elem)
