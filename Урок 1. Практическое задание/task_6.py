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


class QueueTasks:
    def __init__(self):
        self.tasks = []

    def is_empty(self):
        return self.tasks == []

    def to_queue(self, task):
        self.tasks.insert(0, task)

    def from_queue(self):
        return self.tasks.pop()

    def size(self):
        return len(self.tasks)


# Реализуем структуру "Доска задач", состоящую из трех очередей задач
class TaskBoard:
    # Три очереди задач: текущая, на доработку и выполненные:
    def __init__(self):
        self.current_tasks = QueueTasks()
        self.revision_tasks = QueueTasks()
        self.ready_tasks = []

    # Добавление задачи в текущие
    def to_current_queue(self, task):
        self.current_tasks.to_queue(task)

    # Просмотр текущей задачи в работе:
    def get_current_task(self):
        return self.current_tasks.tasks[len(self.current_tasks.tasks) - 1]

    # Просмотр текущей задачи в доработке:
    def get_current_revision(self):
        return self.revision_tasks.tasks[len(self.revision_tasks.tasks) - 1]

    # Перенос текущей задачи в категорию выполненных:
    def to_ready_tasks(self):
        task = self.current_tasks.from_queue()
        self.ready_tasks.append(task)

    # Перенос текущей задачи на доработку:
    def to_revision_tasks(self):
        task = self.current_tasks.from_queue()
        self.revision_tasks.to_queue(task)

    # Перенос задачи из доработки обратно в текущие
    def from_revision_tasks(self):
        task = self.revision_tasks.from_queue()
        self.current_tasks.to_queue(task)

    # Перенос задачи из доработки в категорию выполненных:
    def from_revision_to_ready_tasks(self):
        task = self.revision_tasks.from_queue()
        self.ready_tasks.append(task)


if __name__ == '__main__':
    # Создадим новую доску задач:
    new_task_board = TaskBoard()

    # Добавим на нее задачи:
    new_task_board.to_current_queue('Task1')
    new_task_board.to_current_queue('Task2')
    new_task_board.to_current_queue('Task3')
    new_task_board.to_current_queue('Task4')
    new_task_board.to_current_queue('Task5')

    # Посмотрим список текущих задач:
    print(new_task_board.current_tasks.tasks)
    print()
    # Посмотрим активную задачу (убедимся, что сохраняется принцип FIFO):
    print(new_task_board.get_current_task())
    print()

    # Перенесем одну задачу в категорию выполненных, две - на доработку:
    new_task_board.to_ready_tasks()
    new_task_board.to_revision_tasks()
    new_task_board.to_revision_tasks()

    # Посмотрим список текущих задач:
    print(new_task_board.current_tasks.tasks)
    print()
    # Посмотрим активную задачу, задачи в доработке и выполненные задачи (убедимся, что сохраняется принцип FIFO):
    print(new_task_board.current_tasks.tasks)
    print(new_task_board.get_current_task())
    print(new_task_board.revision_tasks.tasks)
    print(new_task_board.ready_tasks)
    print()

    # Перенесем из доработки одну задачу в текущие, одну в категорию выполненных:
    new_task_board.from_revision_tasks()
    new_task_board.from_revision_to_ready_tasks()
    # Снова активную задачу, задачи в доработке и выполненные задачи (убедимся, что сохраняется принцип FIFO):
    print(new_task_board.current_tasks.tasks)
    print(new_task_board.get_current_task())
    print(new_task_board.revision_tasks.tasks)
    print(new_task_board.ready_tasks)
    print()

    # Структура исправно отрабатывает все сценарии
