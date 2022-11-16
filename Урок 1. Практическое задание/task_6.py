"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.base = []
        self.modification = []
        self.resolved = []


    def to_base(self, item):
        self.base.insert(0, item)

    def to_modification(self, item):
        self.modification.insert(0, item)

    def to_resolved(self, item):
        self.resolved.insert(0, item)

    def out_base(self):
        return self.base.pop()

    def out_modification(self):
        return self.modification.pop()

    def out_resolved(self):
        return self.resolved.pop()


if __name__ == '__main__':
    qc_obj = TaskBoard()
    print(qc_obj.base) # Очередь пустая
    print(qc_obj.modification)  # Очередь пустая
    print(qc_obj.resolved)  # Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_base('my_obj')
    qc_obj.to_modification(4)
    qc_obj.to_resolved(True)
    qc_obj.to_base(9)
    qc_obj.to_base(8885556)
    # получаем очередь
    print(qc_obj.base)
    print(qc_obj.modification)
    print(qc_obj.resolved)

    # получаем элементы очереди
    print(qc_obj.out_base())
    print(qc_obj.out_modification())
    print(qc_obj.out_resolved())
