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


class QueueClass:
    def __init__(self):
        self.base_tasks = []
        self.modification_tasks = []
        self.well_done_tasks = []

    def to_base_tasks(self, item):
        self.base_tasks.insert(0, item)

    def from_base_to_modification(self):
        self.modification_tasks.insert(0, self.base_tasks.pop())

    def from_modification_to_well_done(self):
        self.well_done_tasks.insert(0, self.modification_tasks.pop())

    def from_base_to_well_done(self):
        self.well_done_tasks.insert(0, self.base_tasks.pop())


if __name__ == '__main__':
    qc_obj = QueueClass()

    # помещаем объекты в базовую очередь
    qc_obj.to_base_tasks('my_obj')
    qc_obj.to_base_tasks(4)
    qc_obj.to_base_tasks('world')
    qc_obj.to_base_tasks('hello')

    # смотрим задания в базовой очереди
    print(qc_obj.base_tasks)

    # помещаем объект из базовой очереди на доработку
    # посмотрим что находится в очередях
    qc_obj.from_base_to_modification()
    print(qc_obj.base_tasks)
    print(qc_obj.modification_tasks)

    # помещаем объект из базовой очереди в выполненые
    # посмотрим что находится в очередях
    qc_obj.from_base_to_well_done()
    print(qc_obj.base_tasks)
    print(qc_obj.well_done_tasks)

    # помещаем объект из очереди на доработку в выполненые
    # посмотрим что находится в очередях
    qc_obj.from_modification_to_well_done()
    print(qc_obj.base_tasks)
    print(qc_obj.modification_tasks)
    print(qc_obj.well_done_tasks)
