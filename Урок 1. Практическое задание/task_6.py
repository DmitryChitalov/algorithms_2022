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


class Taskboard:
    def __init__(self):
        self.elems = []
        self.revision_queue = []
        self.log = []

    def is_empty(self):
        return self.elems == []

    def revision_task(self):
        task = self.elems.pop()
        self.revision_queue.append(task)

    def to_queue(self, item):
        self.elems.insert(0, item)

    def resolve_task(self):
        task = self.revision_queue.pop()
        self.log.append(task)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    tb_obj = Taskboard()
    print(tb_obj.elems)
    tb_obj.to_queue('Заправь постель')
    tb_obj.to_queue('Умойся')
    tb_obj.to_queue('Позавтракай')
    print(tb_obj.elems)
    tb_obj.revision_task()
    print(tb_obj.elems)
    print(tb_obj.revision_queue)
    tb_obj.resolve_task()
    print(tb_obj.log)
    tb_obj.revision_task()
    print(tb_obj.elems)
    print(tb_obj.revision_queue)
    tb_obj.resolve_task()
    print(tb_obj.log)
