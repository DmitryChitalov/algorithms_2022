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
        self.base = []
        self.solved = []
        self.modification = []


    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def to_solved(self):
        item = self.base.pop()
        self.solved.insert(0, item)

    def to_modification(self):
        item = self.base.pop()
        self.modification.insert(0, item)

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.base)
    print(qc_obj.is_empty())  # -> False. Очередь пустая
    print(qc_obj.size())  # -> 3
    qc_obj.to_solved()  # -> отправили в список решенных
    qc_obj.to_modification()  # -> отправили на доработку
    print(qc_obj.size())  # -> 1

    print(qc_obj.base)  # -> осталось в базовом
    print(qc_obj.solved)  # -> в решенных
    print(qc_obj.modification)  # -> на доработке
