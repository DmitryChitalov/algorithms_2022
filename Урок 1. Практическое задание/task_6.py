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
        self.tasks = []
        self.done_tasks = []

    def add_task(self, task):
        self.tasks.insert(0, task)

    def done_task(self, task):
        self.done_tasks.append(task)
        return self.tasks.remove(task)

    def show_task(self):
        print(self.tasks)
        if len(self.done_tasks) > 0:
            print(self.done_tasks)

    def size(self):
        print(len(self.tasks))


if __name__ == '__main__':
    task = TaskBoard()
    task.add_task('task1')
    task.add_task('task2')
    task.show_task()
    task.size()
    task.done_task('task1')
    task.size()
    task.show_task()
