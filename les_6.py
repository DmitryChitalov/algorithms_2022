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
        # Список базовых задач
        self.base = []
        # Список задач на доработку
        self.revision = []
        # Список решенных задач
        self.solved = []

    def is_empty(self):
        return self.base == []

    def to_queue(self, item):
        self.base.insert(0, item)

    def from_queue(self):
        return self.base.pop()

    def to_revision(self):
        self.revision.insert(0, self.base.pop())

    def to_solved(self):
        self.solved.insert(0, self.base.pop())

    def from_revision_to_solved(self):
        self.solved.insert(0, self.revision.pop())

    def size(self):
        return len(self.base)


if __name__ == '__main__':
    obj_qu = TaskBoardClass()

    obj_qu.to_queue('task 1')
    obj_qu.to_queue('task 2')
    obj_qu.to_queue('task 3')
    obj_qu.to_queue('task 4')
    obj_qu.to_queue('task 5')
    obj_qu.to_queue('task 6')
    print('Список задач', obj_qu.base)

    print()
    obj_qu.to_solved()  # Первая задача решена
    obj_qu.to_revision()  # Вторая задача на доработку
    obj_qu.to_revision()  # Третья задача на доработку
    print('Решённые задачи', obj_qu.solved)
    print('Задачи на доработке', obj_qu.revision)
    print('Список задач', obj_qu.base)

    print()
    obj_qu.from_revision_to_solved()  # Задача доработана
    print('Задачи на доработке', obj_qu.revision)
    print('Решённые задачи', obj_qu.solved)
    print('Список задач', obj_qu.base)

# Список задач ['task 6', 'task 5', 'task 4', 'task 3', 'task 2', 'task 1']
#
# Решённые задачи ['task 1']
# Задачи на доработке ['task 3', 'task 2']
# Список задач ['task 6', 'task 5', 'task 4']
#
# Задачи на доработке ['task 3']
# Решённые задачи ['task 2', 'task 1']
# Список задач ['task 6', 'task 5', 'task 4']
