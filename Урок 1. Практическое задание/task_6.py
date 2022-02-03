"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClassForTasks:
    def __init__(self):
        self.source_of_tasks = []
        self.solved_tasks = []
        self.tasks_for_revision = []


    def is_empty(self):
        return self.source_of_tasks == []

    def to_queue(self, item):
        self.source_of_tasks.insert(0, item)

    def from_queue(self):
        return self.source_of_tasks.pop()

    def to_solved(self):
        self.solved_tasks.insert(0, self.source_of_tasks.pop())

    def to_revision(self):
        self.tasks_for_revision.insert(0, self.source_of_tasks.pop())

    def return_from_revision_to_source_of_tasks(self):
        self.source_of_tasks.insert(0, self.tasks_for_revision.pop())

    def size(self):
        return len(self.source_of_tasks)


if __name__ == '__main__':
    object_of_implementing_queues_for_tasks = QueueClassForTasks()

    object_of_implementing_queues_for_tasks.to_queue('erett')
    object_of_implementing_queues_for_tasks.to_queue('ertet456')
    object_of_implementing_queues_for_tasks.to_queue(True)
    object_of_implementing_queues_for_tasks.to_queue(646546)
    object_of_implementing_queues_for_tasks.to_queue(False)
    object_of_implementing_queues_for_tasks.to_queue(56.89)


    print(object_of_implementing_queues_for_tasks.source_of_tasks)
    print(object_of_implementing_queues_for_tasks.solved_tasks)
    # Метод  to_solved вынимает решённую задачу и показывает все исходные задачи:
    object_of_implementing_queues_for_tasks.to_solved()
    print(object_of_implementing_queues_for_tasks.solved_tasks)
    # Метод to_revision помещает задачу в очередь для исправления:
    object_of_implementing_queues_for_tasks.to_revision()
    print(object_of_implementing_queues_for_tasks.source_of_tasks)
    print(object_of_implementing_queues_for_tasks.tasks_for_revision)
    # Метод return_from_revision_to_source_of_tasks возвращает задачи из корректируемых в исходные:
    object_of_implementing_queues_for_tasks.return_from_revision_to_source_of_tasks()
    print(object_of_implementing_queues_for_tasks.tasks_for_revision)
    print(object_of_implementing_queues_for_tasks.source_of_tasks)

