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


class TaskBoardClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def remove(self, other, item):
        other.elems.insert(0, item.from_queue)
        self.elems.pop()


if __name__ == '__main__':
    basic_task = TaskBoardClass()
    modification_task = TaskBoardClass()
    solved_task = TaskBoardClass()
    print(basic_task.is_empty())

    # помещаем обЪекты в базовую очередь
    basic_task.to_queue('first')
    basic_task.to_queue('second')
    basic_task.to_queue('third')
    basic_task.to_queue('fourth')
    basic_task.to_queue('fifth')
    print(basic_task.is_empty())
    print(basic_task.size())
    print(modification_task.is_empty())
    print(solved_task.is_empty())

    # отправляем задания на доработку
    basic_task.remove(modification_task, basic_task)
    print(basic_task.size())
    print(modification_task.size())
    basic_task.remove(modification_task, basic_task)
    print(basic_task.elems)

    # отправляем задания в список решенных задач
    basic_task.remove(solved_task, basic_task)
    print(basic_task.size())
    print(solved_task.size())

    # задание доработали, отправили в решенное
    modification_task.remove(solved_task, modification_task)
    print(basic_task.size())
    print(modification_task.size())
    print(solved_task.size())

