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


class Queue:
    def __init__(self):
        self.queue = []

    def push(self, task):
        self.queue.append(task)

    def pop(self):
        if len(self.queue) == 0:
            print('Очередь пуста')
        return self.queue.pop(0)


class TaskBoard:
    def __init__(self):
        self.current = Queue()
        self.revision = Queue()
        self.solved = []

    def add_task(self, task):
        self.current.push(task)

    def resolve(self):
        self.solved.append(self.current.pop())

    def to_revision(self):
        self.revision.push(self.current.pop())

    def resolve_from_revision(self):
        self.solved.append(self.revision.pop())

    def show(self):
        print('Текущие:',self.current.queue, 'На доработке:', self.revision.queue, 'Решенные:', self.solved)
        print('----------------------------')

if __name__ == '__main__':
    tasks = TaskBoard()
    tasks.add_task('task1')
    tasks.add_task('task2')
    tasks.add_task('task3')
    print('Добавили три задачи')
    tasks.show()
    tasks.resolve()
    tasks.to_revision()
    print('Решили одну и отправили на доработку еще одну')
    tasks.show()
    tasks.resolve_from_revision()
    print('Решили задачу из списка "На доработке"')
    tasks.show()