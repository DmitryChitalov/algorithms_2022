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
        self.main_elems = []
        self.revision_elems = []
        self.complete_elems = []

    def is_empty(self):
        return f'{self.main_elems == [] and self.revision_elems == []} main: {len(self.main_elems)}, revision: {len(self.revision_elems)}'

    def to_queue(self, item):
        self.main_elems.insert(0, item)

    def to_revision(self):
        self.revision_elems.insert(0, self.main_elems.pop())

    def complete(self):
        self.complete_elems.insert(0, self.main_elems.pop())

    def revision_complete(self):
        self.complete_elems.insert(0, self.revision_elems.pop())

    def queue_size(self):
        return len(self.main_elems) + len(self.revision_elems)

    def complete_size(self):
        return len(self.complete_elems)

    def last_complete(self):
        return self.complete_elems[0]


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty()) # Проверям, пустая ли очередь
    qc_obj.to_queue(1) # Добавляем таск в основную очередь
    qc_obj.to_queue('name')
    print(qc_obj.is_empty())  # Проверям, пустая ли очередь
    qc_obj.to_revision() # Помещаем элементы из основной очереди в очередь на доработку
    qc_obj.to_revision()
    print(qc_obj.is_empty())
    qc_obj.to_queue(6.2)  # Добавляем задачу в основную очередь
    qc_obj.revision_complete()  # Выполняем задание из очереди на доработку
    print(qc_obj.is_empty()) # Очередь пустая
    print(qc_obj.queue_size())  # Размер очереди
    qc_obj.complete()  # Выполняем задание из основной очереди
    print(qc_obj.is_empty())
    print(qc_obj.last_complete())  # Последнее выполненое задание
    qc_obj.revision_complete()  # Выполняем задание из очереди на доработку
    print(qc_obj.is_empty())
    print(qc_obj.last_complete())