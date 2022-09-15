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
        self.elems = [] # текущая очередь
        self.revision_queue = [] # очередь на доработку
        self.log = [] # завершенные
    def is_empty(self):
        """Текущие задачи"""
        return self.elems == []

    def to_revision_task(self):
        """Отправляем текущую задачу на доработку"""
        task = self.elems.pop()
        self.revision_queue.append(task)
    def to_queue(self, item):
        self.elems.insert(0, item)


    def resolve_task(self):
        """Закрываем текущую задачу и добавляем в лог"""
        task = self.revision_queue.pop()
        self.log.append(task)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.elems)
    qc_obj.to_queue('Task1')
    qc_obj.to_queue('Task2')
    qc_obj.to_queue('Task3')
    print(qc_obj.elems)
    qc_obj.to_revision_task()
    print(qc_obj.elems)
    print(qc_obj.revision_queue)
    qc_obj.resolve_task()
    print(qc_obj.log)
    qc_obj.to_revision_task()
    print(qc_obj.elems)
    print(qc_obj.revision_queue)
    qc_obj.resolve_task()
    print(qc_obj.log)
