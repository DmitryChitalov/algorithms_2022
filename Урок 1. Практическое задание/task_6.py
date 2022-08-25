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
        self.elems = []

    def is_empty(self):
        self.elems = []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class QueueTask:
    def __init__(self):
        self.base_task = QueueClass()
        self.modify_task = QueueClass()
        self.solved_task = QueueClass()

    def base_to_solved(self):
        task = self.base_task.from_queue()
        self.solved_task.to_queue(task)

    def base_to_modify(self):
        task = self.base_task.from_queue()
        self.modify_task.to_queue(task)

    def input_base_task(self, item):
        self.base_task.to_queue(item)

    def clear_base_task(self):
        self.base_task.is_empty()

    def modify_to_solved(self):
        task = self.modify_task.from_queue()
        self.solved_task.to_queue(task)

    def modify_to_base(self):
        task = self.modify_task.from_queue()
        self.base_task.to_queue(task)

    def solved_to_modify(self):
        task = self.solved_task.from_queue()
        self.modify_task.to_queue(task)

    def size_base(self):
        return self.base_task.size()

    def size_modify(self):
        return self.modify_task.size()

    def size_solved(self):
        return self.solved_task.size()

    def current_base_task(self):
        if len(self.base_task.elems) == 0:
            return None
        else:
            return self.base_task.elems[len(self.base_task.elems) - 1]

    def current_modify_task(self):
        if len(self.modify_task.elems) == 0:
            return None
        else:
            return self.modify_task.elems[len(self.modify_task.elems) - 1]

    def current_solved_task(self):
        if len(self.solved_task.elems) == 0:
            return None
        else:
            return self.solved_task.elems[len(self.solved_task.elems) - 1]


if __name__ == '__main__':
    task_list = QueueTask()
    task_list.input_base_task("Задача1")
    task_list.input_base_task("Задача2")
    task_list.input_base_task("Задача3")
    task_list.input_base_task("Задача4")
    task_list.input_base_task("Задача5")
    task_list.input_base_task("Задача6")
    task_list.input_base_task("Задача7")
    task_list.input_base_task("Задача8")
    print(task_list.base_task.elems)
    print(task_list.size_base())
    print(task_list.size_modify())
    print(task_list.size_solved())
    print(task_list.current_base_task())
    print(task_list.current_modify_task())
    print(task_list.current_solved_task())
    task_list.base_to_solved()
    print(task_list.base_task.elems)
    print(task_list.solved_task.elems)
    task_list.base_to_modify()
    print(task_list.base_task.elems)
    print(task_list.solved_task.elems)
    print(task_list.modify_task.elems)
    task_list.base_to_modify()
    task_list.modify_to_solved()
    print(task_list.base_task.elems)
    print(task_list.solved_task.elems)
    print(task_list.modify_task.elems)
    print(task_list.size_base())
    print(task_list.size_modify())
    print(task_list.size_solved())
    task_list.clear_base_task()
    print(task_list.base_task.elems)
    print(task_list.modify_task.elems)
    print(task_list.size_base())
    print(task_list.current_base_task())


